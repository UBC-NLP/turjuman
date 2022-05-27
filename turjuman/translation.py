import torch
from torch.utils.data import DataLoader
from accelerate import Accelerator
from transformers import default_data_collator, Seq2SeqTrainer, Seq2SeqTrainingArguments, DataCollatorForSeq2Seq
from datasets import load_dataset
from tqdm import tqdm
from turjuman.helper import *
class translate_from_file():
    def __init__(self, model, tokenizer, cache_dir, logger):
        self.logger = logger
        self.model=model
        self.tokenizer=tokenizer
        self.cache_dir=cache_dir
        self.data_collator = default_data_collator
        self.accelerator = Accelerator()
        self.gen_kwargs=None



    
    def preprocess_function(self, examples):
        input = [ex for ex in examples["text"]]
        model_inputs = self.tokenizer(input, max_length=self.gen_kwargs['max_length'], padding=True, truncation=True)
        return model_inputs

    def get_file_data(self, filepath):
        self.logger.info("Loading source text from file ({})".format(filepath))
        raw_datasets = load_dataset('text', data_files={'source': filepath}, cache_dir=self.cache_dir)
        self.logger.info("Running tokenizer on source text")
        with self.accelerator.main_process_first():
            processed_datasets = raw_datasets.map(
                self.preprocess_function,
                batched=True,
            )
        return processed_datasets["source"]
    
    def translate(self, filepath, batch_size, gen_kwargs):
        self.gen_kwargs = gen_kwargs
        sources=self.get_file_data(filepath)
        generated_text=[]
        sources_dataloader = DataLoader(sources, collate_fn=self.data_collator, batch_size=batch_size)
        device = ('cuda' if torch.cuda.is_available() else 'cpu')
        self.logger.info(">>>>>Working on {}".format(device))
        self.model.eval()
        samples_seen = 0
        num_batches = len(sources_dataloader)
        pbar = tqdm(total=num_batches, desc="translate")
        self.logger.info("Translating with batch_size {} and #samples = {}".format(batch_size, num_batches))
        for step, batch in enumerate(sources_dataloader):
            batch = {k: v.to(device) for k, v in batch.items()}
            with torch.no_grad():
                generated_tokens = self.accelerator.unwrap_model(self.model).generate(
                    batch["input_ids"],
                    attention_mask=batch["attention_mask"],
                    **gen_kwargs,
                )
                generated_tokens = self.accelerator.pad_across_processes(
                    generated_tokens, dim=1, pad_index=self.tokenizer.pad_token_id
                )
                generated_tokens = self.accelerator.gather(generated_tokens).cpu().numpy()
                decoded_preds = self.tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)
                decoded_preds = [pred.strip() for pred in decoded_preds]
                # If we are in a multiprocess environment, the last batch has duplicates
                if self.accelerator.num_processes > 1:
                    if step == len(sources_dataloader):
                        decoded_preds = decoded_preds[: len(sources_dataloader.dataset) - samples_seen]
                generated_text.extend(decoded_preds)
                pbar.update(1)
                #------------------------------------------------------------------------------
        pbar.close()
        sources_text = [src['text'] for src in sources]
        outputs = extract_output(sources_text, generated_text, gen_kwargs['num_return_sequences'], self.logger)
       
        return outputs
               
