from turjuman.copyright import *
from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

from setuptools import setup

setup(name='turjuman',
      version=__version__,
      description=__description__,
      long_description=readme,
      url='https://github.com/UBC-NLP/turjuman',
      author=__author__,
      author_email=__email__,
      license=__license__,
      packages=find_packages(),
      install_requires=[
          'regex',
          'torch',
          'protobuf',
          'sentencepiece',
          'transformers',
          'psutil',
          'pandas',
          'tqdm',
          'sacrebleu'
        ],
      entry_points={
            "console_scripts": [
                "turjuman_translate = turjuman_cli.translate:translate_cli",
                "turjuman_score = turjuman_cli.score:score_cli",
                "turjuman_interactive = turjuman_cli.interactive:interactive_cli",
            ],
        },
      
      )
