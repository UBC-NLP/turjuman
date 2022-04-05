
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

class tojuman():
    def __init__(self, model_path=None):
        self.model, self.tokatokenizer = self.load_model(model_path)
    
    def load_model(self, model_path):
        model_path = model_path if model_path else "UBC-NLP/AraT5-base-title-generation"
        print ("loading model from", model_path)
        tokenizer = AutoTokenizer.from_pretrained(model_path)  
        model = AutoModelForSeq2SeqLM.from_pretrained(model_path)
        return model, tokenizer
    def translate (self, text, source="xx", target="ar"):
        encoding = self.tokenizer.encode_plus(text,pad_to_max_length=True, return_tensors="pt")
        input_ids, attention_masks = encoding["input_ids"], encoding["attention_mask"]

        outputs = self.model.generate(
        input_ids=input_ids, attention_mask=attention_masks,
        max_length=512,
        do_sample=True,
        top_k=120,
        top_p=0.95,
        early_stopping=True,
        num_return_sequences=1
        )

        return self.tokenizer.decode(outputs[0], skip_special_tokens=True,clean_up_tokenization_spaces=True)


t = tojuman()
print (t.translate("this is my life"))