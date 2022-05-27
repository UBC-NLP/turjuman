from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import pandas as pd
import torch.nn as nn
import torch
from turjuman.translation import translate_from_file
from turjuman.helper import *
import regex
class turjuman():
    def __init__(self, logger, cache_dir, model_path=None):
        self.logger = logger
        self.cache_dir=cache_dir
        self.model, self.tokenizer = self.load_model(model_path)

    def load_model(self, model_path):
        model_path = model_path if model_path else "UBC-NLP/turjuman"
        self.logger.info("Loading model from {}".format(model_path))
        tokenizer = AutoTokenizer.from_pretrained(model_path, cache_dir=self.cache_dir)  
        model = AutoModelForSeq2SeqLM.from_pretrained(model_path, cache_dir=self.cache_dir)
        ##### GPU check ####
        if torch.cuda.is_available():
            device="cuda"
            n_gpu = torch.cuda.device_count()
            device_ids = [i for i in range(0,n_gpu)] #GPUtil.getAvailable(limit = 8)
            if n_gpu == 1:
               self.logger.info("Run the model with one-GPU {}".format(n_gpu, str(device_ids)))
               model = model.to(device)
            else:
                self.logger.info("Run the model with {} GPUs {}".format(n_gpu, str(device_ids)))
                torch.backends.cudnn.benchmark = True
                model = model.to(device)
                model = nn.DataParallel(model, device_ids=device_ids)
        else:
            device="cpu"
            self.logger.info("Run the model with CPU")
            model = model
        return model, tokenizer
    
    def validate(self, search_method, max_outputs, num_beams):
        validattion_results=None
        if max_outputs> num_beams and search_method=="beam":
            self.logger.error("For `beam search`: `--max_outputs` has to be smaller or equal to `--num_beams`")
        elif max_outputs> 1 and search_method=="greedy":
            self.logger.error("For `greedy search`: `--max_outputs` should be 1")
        else:
            validattion_results="valid"
        
        return validattion_results
    def translate(self, sources, search_method, seq_length=300, max_outputs=1, num_beams=5, no_repeat_ngram_size=2, top_p=0.95, top_k=50):
        encoding = self.tokenizer(sources,padding=True, return_tensors="pt")
        input_ids, attention_masks = encoding["input_ids"], encoding["attention_mask"]
        gen_kwargs = get_gen_kwargs(search_method, seq_length, max_outputs, num_beams, no_repeat_ngram_size, top_p, top_k, self.logger)

        outputs = self.model.generate(
                        input_ids=input_ids, 
                        attention_mask=attention_masks,
                        **gen_kwargs,
                    )
        

        generated_text = self.tokenizer.batch_decode(outputs, skip_special_tokens=True)
        
        return outputs
    
    
    def translate_from_file(self, input_file, search_method, seq_length=300, max_outputs=1, num_beams=5, no_repeat_ngram_size=2, top_p=0.95, top_k=50, batch_size=25):
        if self.validate(search_method, max_outputs, num_beams) is None:
            return None
        sources = get_file_content(input_file, self.logger)
        if len(sources)<1:
            self.logger.error("The input file {} is empty".format(input_file))
        output_file = str(Path(input_file).with_suffix(''))+"_Turjuman_translate.json"
        #-- create batches start--#
        
        gen_kwargs = get_gen_kwargs(search_method, seq_length, max_outputs, num_beams, no_repeat_ngram_size, top_p, top_k, self.logger)
        tf = translate_from_file(self.model, self.tokenizer, self.cache_dir, self.logger)
        outputs = tf.translate(input_file, batch_size, gen_kwargs)
        df = pd.DataFrame.from_dict(outputs)
        df.to_json(output_file, orient='records', lines=True)
        self.logger.info("The translation are saved on {}".format(output_file))
        
        

    def translate_from_text(self, text, search_method, seq_length=512, max_outputs=1, num_beams=5, no_repeat_ngram_size=2, top_p=0.95, top_k=50):
        if self.validate(search_method, max_outputs, num_beams) is None:
            return None
        if len(regex.sub('\s+','',text))<1:
            self.logger.info("Source should be at least 2 characters")
            return None
        sources = [text]
        outputs = self.translate(sources, search_method, seq_length, max_outputs, num_beams, no_repeat_ngram_size, top_p, top_k)

        if max_outputs==1:
            targets = outputs['target'][0]
        else:
            targets = outputs[str(max_outputs)+'_targets'][0]
        if type(targets) == list:
            for idx, target in enumerate(targets):
                 print ("target#{}: {}".format(idx+1, target))
        else:
            print ("target: {}".format(targets))

