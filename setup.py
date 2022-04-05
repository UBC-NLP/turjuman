from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

from setuptools import setup

setup(name='torjuman',
      version='1.0.0',
      description='An Open Source Toolkit for Diverse Arabic Machine Translation',
      long_description=readme,
      url='https://github.com/UBC-NLP/torjuman',
      author='AbdelRahim Elmadany',
      author_email='a.elmadany@ubc.ca',
      license='GNU',
      packages=find_packages(),
      install_requires=[
          'regex',
          'torch',
          'sentencepiece',
          'transformers',
          'psutil',
          'pandas',
          'tqdm'
        ],
      entry_points={
            "console_scripts": [
                "torjuman = torjuman_cli.torjuman:cli_main",
            ],
        },
      
      )
