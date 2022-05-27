import sacrebleu



def bleu_score(hyp_file, ref_file):
    decoded_preds = open(hyp_file,'r').read().splitlines()
    decoded_labels = open(ref_file,'r').read().splitlines()
    if len(decoded_preds) != len(decoded_labels):
        print ("[Error] The number of hypothesis (predicted) and references (labels) samples should be equaled " )
    else:
        bleu_results = sacrebleu.corpus_bleu(decoded_preds, [decoded_labels])
        bleu_score = bleu_results.score
        result = {"bleu": bleu_score}
        return result

