Translate Command Line
=====================
:colab_example_url: https://colab.research.google.com/github/UBC-NLP/turjuman/blob/main/examples/turjuman_translate_cli.ipynb

Usage and Arguments
-------------------

.. code-block:: console

       turjuman_translate -h

Turjuman Command Line Interface (CLI) Turjuman cli ``turjuman_translate_cli`` support two types of inputs:

   -  ``-t`` or ``--text``: Write you input text directly on the command line. The translation will display directly on the terminal.
   -  ``-f`` or ``--input_file``: import the text from file. The translation will saved on the JSON format file.

``turjuman_translate_cli`` has the following optional arguments.

.. code-block:: console

         usage: turjuman_translate [-h] [-t TEXT] [-f INPUT_FILE] [-m SEARCH_METHOD]
                                   [-s SEQ_LENGTH] [-o MAX_OUTPUTS] [-b NUM_BEAMS]
                                   [-n NO_REPEAT_NGRAM_SIZE] [-k TOP_K] [-p TOP_P]
                                   [-c CACHE_DIR] [-l LOGGING_FILE] [-bs BATCH_SIZE]

         Turjuman Translate Command Line Interface (CLI)

         optional arguments:
           -h, --help            show this help message and exit
           -t TEXT, --text TEXT  Translate the input text
           -f INPUT_FILE, --input_file INPUT_FILE
                                 Translate the input file
           -m SEARCH_METHOD, --search_method SEARCH_METHOD
                                 Turjuman translation search method should be one of
                                 the follows ['greedy', 'beam', 'sampling'], default
                                 value is beam search
           -s SEQ_LENGTH, --seq_length SEQ_LENGTH
                                 The maximum sequence length value, default vlaue is
                                 300
           -o MAX_OUTPUTS, --max_outputs MAX_OUTPUTS
                                 The maxmuim of the output tanslations, default vlaue
                                 is 1
           -b NUM_BEAMS, --num_beams NUM_BEAMS
                                 Number of beams, default vlaue is 5
           -n NO_REPEAT_NGRAM_SIZE, --no_repeat_ngram_size NO_REPEAT_NGRAM_SIZE
                                 Number of n-gram that doesn't appears twice, default
                                 vlaue is 2
           -k TOP_K, --top_k TOP_K
                                 Sample from top K likely next words instead of all
                                 words, default vlaue is 50
           -p TOP_P, --top_p TOP_P
                                 Sample from the smallest set whose cumulative
                                 probability mass exceeds p for next words, default
                                 vlaue is 0.95
           -c CACHE_DIR, --cache_dir CACHE_DIR
                                 The cache directory path, default vlaue is
                                 turjuman_cache directory
           -l LOGGING_FILE, --logging_file LOGGING_FILE
                                 The logging file path, default vlaue is None
           -bs BATCH_SIZE, --batch_size BATCH_SIZE
                                 The maximum number of source examples utilized in one
                                 iteration

Translate using beam search (default)
-------------------------------------
``Beam search`` is the ``default`` generation method on Turjuman
   -  Beam search default setting:

      -  ``-s`` or ``--seq_length``: The maximum sequence length value, (``default vlaue is 300``)
      -  ``-o`` or ``--max_outputs``: The maxmuim of the output tanslations (``default vlaue is 1``)
      -  ``-b`` or ``--num_beams NUM_BEAMS``: Number of beams (``default vlaue is 1``)
      -  ``-n`` or ``--no_repeat_ngram_size``: Number of n-gram that doesn't appears twice (``default vlaue is 2``)

.. code-block:: console

       turjuman_translate --text "As US reaches one million COVID deaths, how are Americans coping?"

The outputs:

.. code-block:: console

         2022-05-18 00:00:27 | INFO | turjuman.translate_cli | Turjuman Translate Command Line Interface
         2022-05-18 00:00:27 | INFO | turjuman.translate_cli | Translate from input sentence
         2022-05-18 00:00:27 | INFO | turjuman.translate_cli | Loading model from UBC-NLP/turjuman
         Downloading: 100% 1.85k/1.85k [00:00<00:00, 1.71MB/s]
         Downloading: 100% 565/565 [00:00<00:00, 460kB/s]
         Downloading: 100% 2.32M/2.32M [00:00<00:00, 12.4MB/s]
         Downloading: 100% 1.74k/1.74k [00:00<00:00, 1.54MB/s]
         Downloading: 100% 565/565 [00:00<00:00, 455kB/s]
         Downloading: 100% 1.05G/1.05G [00:22<00:00, 51.3MB/s]
         2022-05-18 00:00:57 | INFO | turjuman.translate_cli | Using beam search
         2022-05-18 00:01:01 | ERROR | turjuman.translate_cli | extract outputs
         target: وبينما تصل الولايات المتحدة إلى مليون حالة وفاة من فيروس كوفيد-19 ، كيف يتعامل الأمريكيون مع ذلك ؟

(3) Translate using greedy search
-----------------------------------
 ``Greedy search`` default setting:
   -  ``-s`` or ``--seq_length``: The maximum sequence length value, (``*``default vlaue is 300``*``)

.. code-block:: console

      turjuman_translate --search_method greedy --text "As US reaches one million COVID deaths, how are Americans coping?"

The output:

.. code-block:: console
         2022-05-18 00:01:07 | INFO | turjuman.translate_cli | Turjuman Translate Command Line Interface
         2022-05-18 00:01:07 | INFO | turjuman.translate_cli | Translate from input sentence
         2022-05-18 00:01:07 | INFO | turjuman.translate_cli | Loading model from UBC-NLP/turjuman
         2022-05-18 00:01:14 | INFO | turjuman.translate_cli | Using greedy search
         2022-05-18 00:01:16 | ERROR | turjuman.translate_cli | extract outputs
         target: وبما أن الولايات المتحدة تصل إلى مليون حالة وفاة من فيروس كوفيد-19 ، كيف يمكن للولايات المتحدة أن تتصدى لهذا ؟

(4) Translate using sampling search
------------------------------------
``Sampling search`` default setting:

      -  ``-s`` or ``--seq_length``: The maximum sequence length value, (``default vlaue is 300``)
      -  ``-o`` or ``--max_outputs``: The maxmuim of the output tanslations (``default vlaue is 1``)
      -  ``-k`` or ``--top_k``: Sample from top K likely next words instead of all words (``default vlaue is 50``)
      -  ``-p`` or ``--top_p``: Sample from the smallest set whose cumulative probability mass exceeds p for next words (``default vlaue is 0.95``)

.. code-block:: console

      turjuman_translate --search_method sampling --text "As US reaches one million COVID deaths, how are Americans coping?"

.. code-block:: console

         2022-05-18 00:01:38 | INFO | turjuman.translate_cli | Turjuman Translate Command Line Interface
         2022-05-18 00:01:38 | INFO | turjuman.translate_cli | Translate from input sentence
         2022-05-18 00:01:38 | INFO | turjuman.translate_cli | Loading model from UBC-NLP/turjuman
         2022-05-18 00:01:44 | INFO | turjuman.translate_cli | Using sampling search
         2022-05-18 00:01:47 | ERROR | turjuman.translate_cli | extract outputs
         target: وبوصول الولايات المتحدة الأمريكية إلى مليون حالة وفاة بسبب كوفيد-19 ، كيف يمكن الأميركيين أن يتعاملوا مع ذلك ؟

(5) Read and translate text from file
--------------------------------------
   -  ``-f`` or ``--input_file``: import the text from file. The translation will saved on the JSON format file
   -  ``-bs`` or ``--batch_size``: The maximum number of source examples utilized in one iteration (``default value is 25``)

.. code-block:: console

      wget https://raw.githubusercontent.com/UBC-NLP/turjuman/main/examples/samples.txt
      
      turjuman_translate --input_file samples.txt

.. code-block:: console
   
         2022-05-18 00:02:08 | INFO | turjuman.translate_cli | Turjuman Translate Command Line Interface
         2022-05-18 00:02:08 | INFO | turjuman.translate_cli | Translate from input file samples.txt
         2022-05-18 00:02:08 | INFO | turjuman.translate_cli | Loading model from UBC-NLP/turjuman
         2022-05-18 00:02:14 | INFO | turjuman.translate_cli | Using beam search
         2022-05-18 00:02:14 | INFO | turjuman.translate_cli | Loading source text from file (samples.txt)
         2022-05-18 00:02:14 | WARNING | datasets.builder | Using custom data configuration default-9c05233ea5cb76ef
         Downloading and preparing dataset text/default to ./turjuman_cache/text/default-9c05233ea5cb76ef/0.0.0/4b86d314f7236db91f0a0f5cda32d4375445e64c5eda2692655dd99c2dac68e8...
         Downloading data files: 100% 1/1 [00:00<00:00, 5419.00it/s]
         Extracting data files: 100% 1/1 [00:00<00:00, 1024.25it/s]
         Dataset text downloaded and prepared to ./turjuman_cache/text/default-9c05233ea5cb76ef/0.0.0/4b86d314f7236db91f0a0f5cda32d4375445e64c5eda2692655dd99c2dac68e8. Subsequent calls will reuse this data.
         100% 1/1 [00:00<00:00, 161.41it/s]
         2022-05-18 00:02:14 | INFO | turjuman.translate_cli | Running tokenizer on source text
         tcmalloc: large alloc 1290076160 bytes == 0x12513e000 @  0x7f01deea1615 0x592b76 0x4df71e 0x593605 0x515244 0x593dd7 0x548ae9 0x51566f 0x593dd7 0x5118f8 0x549576 0x593fce 0x5118f8 0x593dd7 0x5118f8 0x549576 0x593fce 0x5118f8 0x549576 0x4bca8a 0x59c019 0x595ef6 0x5134a6 0x549576 0x593fce 0x5118f8 0x593dd7 0x5118f8 0x549576 0x593fce 0x5118f8
         100% 1/1 [00:00<00:00, 71.95ba/s]
         translate:   0% 0/1 [00:00<?, ?it/s]2022-05-18 00:02:20 | INFO | turjuman.translate_cli | Translating with batch_size 25 and #batches = 1
         translate: 100% 1/1 [00:18<00:00, 18.90s/it]
         2022-05-18 00:02:38 | ERROR | turjuman.translate_cli | extract outputs
         2022-05-18 00:02:38 | INFO | turjuman.translate_cli | The translation are saved on samples_Turjuman_translate.json
