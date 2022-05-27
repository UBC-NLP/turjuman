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
    parser.add_argument('-c', '--cache_dir', default="./turjuman_cache", type=str, help='The cache directory path, default vlaue is turjuman_cache directory')


    return parser



def interactive_cli():
    parser = get_parser()
    args = parser.parse_args()
    #-------------------------

    logger.info(args)
    torj = turjuman(logger, "./turjuman_cache")
    source=""
    while source !='q':
        source = input("Type your source text or (q) to STOP: ")
        if source !='q':
            if len(regex.sub('\s+','',source))<1:
                logger.info("Source should be at least 2 characters")
                continue
            torj.translate_from_text (source, search_method="beam")



if __name__ == "__main__":
    interactive_cli()