Score Command Line
=====================



Turjuman score cli ``turjuman_score`` computes the bleu score between two files:

   -  ``-h`` or ``--hyp_file``: The hypothesis (predicted/generated translation) file path.
   -  ``-g`` or ``--ref_file``: The references (gold translation) file path.
   
Usage and Arguments
-------------------

.. code-block:: console

      turjuman_score -h


.. code-block:: console

         usage: turjuman_score [-h] -p HYP_FILE -g REF_FILE

         Turjuman Score CLI

         optional arguments:
           -h, --help            show this help message and exit
           -p HYP_FILE, --hyp_file HYP_FILE
                                 The hypothesis file path (predicted data)
           -g REF_FILE, --ref_file REF_FILE
                                 The references file path (gold data)

Input files format
---------------------

   -  ``hyp_file`` is a line-based text file where each line represents one translated sentence.
   -  ``ref_file`` is a line-based text file where each line represents the one gold sentence.


Example
---------

.. code-block:: console

      wget https://raw.githubusercontent.com/UBC-NLP/turjuman/main/examples/translated_targets.txt
      wget https://raw.githubusercontent.com/UBC-NLP/turjuman/main/examples/gold_targets.txt

.. code-block:: console

      turjuman_score -p translated_targets.txt -g gold_targets.txt

The output:

.. code-block:: console

         2022-05-18 00:14:50 | INFO | turjuman.score_cli | Namespace(hyp_file='translated_targets.txt', ref_file='gold_targets.txt')
         {'bleu': 43.573826221233, 'hyp_file': 'translated_targets.txt', 'ref_file': 'gold_targets.txt'}


Google Colab Link
-----------------
You can find the full examples on the Google Colab on the following link
https://colab.research.google.com/github/UBC-NLP/turjuman/blob/main/examples/turjuman_score_cli.ipynb
