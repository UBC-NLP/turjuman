#!/usr/bin/env python3
# Copyright (c) Copyright 2021, University of British Columbia (UBC), NLP Lab.

import argparse
import os
import sys
import logging
from turjuman.metrics import *
logging.basicConfig(
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    level=os.environ.get("LOGLEVEL", "INFO").upper(),
    stream=sys.stdout,
)
logger = logging.getLogger("turjuman.score_cli")



def get_parser():
    parser = argparse.ArgumentParser(
        description="Turjuman Score CLI"
    )
    # fmt: off
    parser.add_argument('-p', '--hyp_file', required=True, type=str, help='The hypothesis file path (predicted data) ')
    parser.add_argument('-g', '--ref_file', required=True, type=str, help='The references file path (gold data)' )
    
    # fmt: on
    return parser


def score_cli():
    parser = get_parser()
    args = parser.parse_args()
    #-------------------------
    
    logger.addHandler(
        logging.FileHandler(
            filename="torjuman_score_cli.log",
        )
    )
    # Print args
    
    logger.info(args)
    results = bleu_score(args.hyp_file, args.ref_file)
    results['hyp_file']=args.hyp_file
    results['ref_file']=args.ref_file

    print (results)
    
    




if __name__ == "__main__":
    score_cli()