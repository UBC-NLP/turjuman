from turjuman.copyright import *
from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

from setuptools import setup

setup(name='turjuman',
      version=version,
      description=description,
      long_description=readme,
      url='https://github.com/UBC-NLP/turjuman',
      author=author,
      author_email=email,
      license=license,
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
          'sacrebleu',
          'dask',
          'dask[dataframe]',
          'psutil',
          'hurry.filesize',
          'tqdm'
        ],
      entry_points={
            "console_scripts": [
                "turjuman_translate = turjuman_cli.translate:translate_cli",
                "turjuman_score = turjuman_cli.score:score_cli",
                "turjuman_interactive = turjuman_cli.interactive:interactive_cli",
            ],
        },
      
      )
