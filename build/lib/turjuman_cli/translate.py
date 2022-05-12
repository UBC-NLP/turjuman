#!/usr/bin/env python3
# Copyright (c) Copyright 2021, University of British Columbia (UBC), NLP Lab.
"""
Normalize a file using the multilingual normalizer.
"""

import argparse
import os
import sys
import logging
from turjuman.turjuman import *
logging.basicConfig(
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    level=os.environ.get("LOGLEVEL", "INFO").upper(),
    stream=sys.stdout,
)
logger = logging.getLogger("turjuman.translate_cli")



def get_parser():
    parser = argparse.ArgumentParser(
        description="Turjuman Translate CLI"
    )
    # fmt: off
    parser.add_argument('-m', '--search_method', required=True, type=str, help='Torjuman translatation cli search method')
    parser.add_argument('-t', '--text', type=str, help='The input source text')
    parser.add_argument('-f', '--input_file', type=str, help='The source text input file path')
    parser.add_argument('-s', '--seq_length', type=int, help='seq_length value, default vlaue is 512')
    parser.add_argument('-o', '--max_outputs', default=1, type=int, help='the maxmuim of the output tanslations, default vlaue is 1')
    parser.add_argument('-b', '--num_beams', default=5, type=int, help='Number of beams, default vlaue is 1')
    parser.add_argument('-n', '--no_repeat_ngram_size', default=2, type=int, help='Number of n-gram that doesn\'t appears twice, default vlaue is 2')
    parser.add_argument('-k', '--top_k', default=50, type=int, help='top_k value, default vlaue is 50')
    parser.add_argument('-p', '--top_p', default=0.95, type=float, help='top_p value, default vlaue is 0.95')

    # parser.add_argument('-t', '--text', required=True, type=str, help='The input source text')
    # parser.add_argument('-sc', '--source', default="English", type=str, help='The source langauage, default vlaue is English')
    # parser.add_argument('-tg', '--target', default="French", type=str, help='The target langauage, default vlaue is French')
    # parser.add_argument('-seq', '--seq_length', default=128, type=int, help='seq_length value, default vlaue is 128')
    
    # 

    # fmt: on
    return parser


def translate_cli():
    search_methods = ['greedy', 'beam', 'sampling']
    parser = get_parser()
    args = parser.parse_args()
    #-------------------------
    
    logger.addHandler(
        logging.FileHandler(
            filename="turjuman_translate_cli.log",
        )
    )
    if args.search_method not in search_methods:
        logger.info("[Error] Translation search method  should be one of the follows ["+",".join(search_methods)+"]")
        return None
    # Print args
    input_source=None
    if args.text is not None and args.input_file is None:
        logger.info("Translate from input sentence")
        input_source="text"
    elif args.input_file is not None and args.text is None:
        if Path(args.input_file).is_file():
            logger.info("Translate from input file {}".format(args.input_file))
            input_source="file"
        else:
            logger.info("[Error] Can't open the input file {}".format(args.input_file))
            return None
    else:
        logger.info("[Error] You should one of the following option --text or --input_file")
        return None
    

    torj = turjuman(logger)
    if input_source=="text":
        torj.translate_from_text (args.text, args.search_method, args.seq_length, args.max_outputs, args.num_beams, args.no_repeat_ngram_size, args.top_p, args.top_k)
    elif input_source=="file":
        torj.translate_from_file (args.input_file, args.search_method, args.seq_length, args.max_outputs, args.num_beams, args.no_repeat_ngram_size, args.top_p, args.top_k)

    # if args.search_method == 'greedy':
    #     logger.info("Using greedy search")
    #     if input_source=="text":
    #         return torj.translate_sentence (args.text, args.search_method, args.seq_length, args.max_outputs, args.num_beams, args.no_repeat_ngram_size)
    #         # return torj.translate_sentence_greedy(args.text, args.seq_length, args.max_outputs)
    #     elif input_source=="file":
    #         logger.info("Translate from input file")
    #         return torj.translate_file_greedy(args.input_file, args.seq_length)

    
    # print ("Source ("+args.source+") text: "+args.text)
    # # print (args.text, args.source, args.target)
    # # translate (self, text, source, target, seq_length=512, k=120, p=0.95, max_outputs=1):
    # print ("Target ("+args.target+") translation(s): ")
    # outputs = torj.translate(text=args.text, source=args.source, target=args.target, seq_length=args.seq_length, k=args.top_k,p=args.top_p,max_outputs=args.max_outputs)
    # if args.max_outputs==1:
    #     print (outputs[0])
    # else:
    #     for id, output in enumerate(outputs):
    #         print ("   |-- translate (#"+str(id+1)+")",output)
    




if __name__ == "__main__":
    translate_cli()