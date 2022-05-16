import argparse
import os
import sys
import logging
from turjuman.turjuman import *
import regex
logging.basicConfig(
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    level=os.environ.get("LOGLEVEL", "INFO").upper(),
    stream=sys.stdout,
)
logger = logging.getLogger("turjuman.interactive_cli")

def get_parser():
    parser = argparse.ArgumentParser(
        description="Turjuman Interactive CLI"
    )
    # fmt: off
    # parser.add_argument('-p', '--hyp_file', required=True, type=str, help='The hypothesis file path (predicted data) ')
    # parser.add_argument('-g', '--ref_file', required=True, type=str, help='The references file path (gold data)' )
    
    # fmt: on
    return parser



def interactive_cli():
    parser = get_parser()
    args = parser.parse_args()
    #-------------------------
    
    logger.addHandler(
        logging.FileHandler(
            filename="torjuman_interactive_cli.log",
        )
    )
    # Print args
    logger.info(args)
    torj = turjuman(logger)
    source=""
    while source !='q':
        # print ("source", source)
        source = input("Type your source text or (q) to STOP: ")
        if len(regex.sub('\s+','',source))<2:
            logger.info("source should be at least 2 characters")
            continue
        torj.translate_from_text (source, search_method="beam")



if __name__ == "__main__":
    interactive_cli()