from pathlib import Path
def get_file_content(input_file, logger):
    sources=[]
    if Path(input_file).is_file():
        with open(input_file) as f:
            sources = f.read().splitlines()
    else:
        logger.error("Can't open the input file {}".format(input_file))
    return sources
def get_gen_kwargs(search_method, seq_length, max_outputs, num_beams, no_repeat_ngram_size, top_p, top_k, logger):
    if search_method=="greedy":
        logger.info("Using greedy search")
        gen_kwargs = {"max_length": seq_length,"num_return_sequences": 1, 'do_sample':False }
    elif search_method=="beam":
        logger.info("Using beam search")
        gen_kwargs = {"max_length": seq_length,"num_return_sequences": max_outputs, 'do_sample':False, 'num_beams':num_beams,  'no_repeat_ngram_size':no_repeat_ngram_size, 'early_stopping':True}
    elif search_method=="sampling":
        logger.info("Using sampling search")
        gen_kwargs = {"max_length": seq_length,"num_return_sequences": max_outputs, 'do_sample':True, 'top_k':top_k, 'top_p':top_p }
    return gen_kwargs
def extract_output(sources, generated_text, max_outputs, logger):
    logger.info("Extract outputs")
    targets=[]
    if max_outputs==1:
        targets = generated_text
        outputs={'source':sources, 'target':targets}
    else:
        for i in range(0, len(generated_text), max_outputs):
            translate_start_id= i
            translate_start_end= i+max_outputs
            temp=[]
            for t in range (translate_start_id, translate_start_end):
                temp.append(generated_text[t])
            targets.append(temp)
        outputs={'source':sources, str(max_outputs)+'_targets':targets}
    return outputs