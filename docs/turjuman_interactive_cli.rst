Interactive Command Line
=====================
   -  Turjuman interactive cli ``turjuman_interactive`` support only beam search with the following default setting:

      -  ``-s`` or ``--seq_length``: The maximum sequence length value, (``default vlaue is 300``)
      -  ``-o`` or ``--max_outputs``: The maxmuim of the output tanslations (``default vlaue is 1``)
      -  ``-b`` or ``--num_beams NUM_BEAMS``: Number of beams (``default vlaue is 1``)
      -  ``-n`` or ``--no_repeat_ngram_size``: Number of n-gram that doesn't appears twice (``default vlaue is 2``)

   -  ``turjuman_interactive`` command asks you you to input translate your input text. Moreover, you can write q to exsit as shown in the following image.

.. raw:: html

   <img src="https://raw.githubusercontent.com/UBC-NLP/turjuman/main/examples/turjuman_interactive.jpg" alt="turjuman_interactive"/>



Usage and Arguments
-------------------
.. code-block:: console

      turjuman_interactive -h

.. code-block:: console
         usage: turjuman_interactive [-h] [-c CACHE_DIR]

         Turjuman Interactive CLI

         optional arguments:
           -h, --help            show this help message and exit
           -c CACHE_DIR, --cache_dir CACHE_DIR
                                 The cache directory path, default vlaue is
                                 turjuman_cache directory

(2) Turjuman Interactive
---------------------------
      :name: 2-turjuman-interactive

.. code-block:: console

      !turjuman_interactive

.. code-block:: console

         2022-05-18 16:51:42 | INFO | turjuman.interactive_cli | Namespace(cache_dir='./turjuman_cache')
         2022-05-18 16:51:42 | INFO | turjuman.interactive_cli | Loading model from UBC-NLP/turjuman
         Downloading: 100% 1.85k/1.85k [00:00<00:00, 1.31MB/s]
         Downloading: 100% 565/565 [00:00<00:00, 453kB/s]
         Downloading: 100% 2.32M/2.32M [00:00<00:00, 5.38MB/s]
         Downloading: 100% 1.74k/1.74k [00:00<00:00, 1.07MB/s]
         Downloading: 100% 565/565 [00:00<00:00, 475kB/s]
         Downloading: 100% 1.05G/1.05G [00:20<00:00, 56.1MB/s]
         Type your source text or (q) to STOP: As US reaches one million COVID deaths, how are Americans coping?
         2022-05-18 16:52:25 | INFO | turjuman.interactive_cli | Using beam search
         2022-05-18 16:52:29 | INFO | turjuman.interactive_cli | Extract outputs
         target: وبينما تصل الولايات المتحدة إلى مليون حالة وفاة من فيروس كوفيد-19 ، كيف يتعامل الأمريكيون مع ذلك ؟
         Type your source text or (q) to STOP: Это список суверенных государств и зависимых территорий в Азии .
         2022-05-18 16:54:31 | INFO | turjuman.interactive_cli | Using beam search
         2022-05-18 16:54:34 | INFO | turjuman.interactive_cli | Extract outputs
         target: هذه قائمة الدول ذات السيادة والأقاليم التابعة في آسيا.
         Type your source text or (q) to STOP: क्या तुम्हें यकीन है कि वही है ?
         2022-05-18 16:54:49 | INFO | turjuman.interactive_cli | Using beam search
         2022-05-18 16:54:51 | INFO | turjuman.interactive_cli | Extract outputs
         target: هل أنت واثق من ذلك ؟
         Type your source text or (q) to STOP: q

