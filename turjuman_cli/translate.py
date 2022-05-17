#!/usr/bin/env python3
# Copyright (c) Copyright 2021, University of British Columbia (UBC), NLP Lab.
"""
Normalize a file using the multilingual normalizer.
"""

import argparse
from ast import arg
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
        description="Turjuman Translate Command Line Interface (CLI)"
    )
    parser.add_argument('-t', '--text', type=str, help='Translate the input text')
    parser.add_argument('-f', '--input_file', type=str, help='Translate the input file')
    parser.add_argument('-m', '--search_method', type=str, default='beam', help="Turjuman translation search method should be one of the follows ['greedy', 'beam', 'sampling'], default value is beam search")
    parser.add_argument('-s', '--seq_length', type=int, default=300, help='The maximum sequence length value, default vlaue is 300')
    parser.add_argument('-o', '--max_outputs', default=1, type=int, help='The maxmuim of the output tanslations, default vlaue is 1')
    parser.add_argument('-b', '--num_beams', default=5, type=int, help='Number of beams, default vlaue is 1')
    parser.add_argument('-n', '--no_repeat_ngram_size', default=2, type=int, help='Number of n-gram that doesn\'t appears twice, default vlaue is 2')
    parser.add_argument('-k', '--top_k', default=50, type=int, help='Sample from top K likely next words instead of all words, default vlaue is 50')
    parser.add_argument('-p', '--top_p', default=0.95, type=float, help='Sample from the smallest set whose cumulative probability mass exceeds p for next words, default vlaue is 0.95')
    parser.add_argument('-c', '--cache_dir', default="./turjuman_cache", type=str, help='The cache directory path, default vlaue is turjuman_cache directory')
    parser.add_argument('-l', '--logging_file', default=None, type=str, help='The logging file path, default vlaue is None')
    parser.add_argument('-bs', '--batch_size', default=25, type=int, help='The maximum number of source examples utilized in one iteration')
    return parser


def translate_cli():
    search_methods = ['greedy', 'beam', 'sampling']
    parser = get_parser()
    args = parser.parse_args()
    if args.logging_file is not None:
        logger.addHandler(
            logging.FileHandler(
                filename=args.logging_file,
            )
        )
    logger.info("Turjuman Translate Command Line Interface")

    if args.search_method not in search_methods:
        logger.info("[Error] Translation search method  should be one of the follows ["+",".join(search_methods)+"]")
        return None
   
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
        logger.info("[Error] You chould use one of the following options to input the source: `--text` or `--input_file`")
        return None
    

    torj = turjuman(logger, args.cache_dir)
    if input_source=="text":
        torj.translate_from_text (args.text, args.search_method, args.seq_length, args.max_outputs, args.num_beams, args.no_repeat_ngram_size, args.top_p, args.top_k)
    elif input_source=="file":
        torj.translate_from_file (args.input_file, args.search_method, args.seq_length, args.max_outputs, args.num_beams, args.no_repeat_ngram_size, args.top_p, args.top_k, args.batch_size)




if __name__ == "__main__":
    translate_cli()