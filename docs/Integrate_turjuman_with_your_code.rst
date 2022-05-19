Integrate turjuman with your python code
=========================================

.. container:: cell markdown

   .. rubric:: (1) Install Turjuman
      :name: 1-install-turjuman

.. code-block:: console

      pip install git+https://github.com/UBC-NLP/turjuman.git --q

.. container:: cell markdown

(1) Initial turjuman object
----------------------------
Import related packges 

.. code:: python

      import logging
      import os
      from turjuman import turjuman

Inital the logger and set ``cache_dir``

 .. code:: python

      logging.basicConfig(
          format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
          datefmt="%Y-%m-%d %H:%M:%S",
          level=os.environ.get("LOGLEVEL", "INFO").upper(),
      )
      logger = logging.getLogger("turjuman.translate")
      cache_dir="/content/mycache"

Create turjuman object

.. code:: python

      torj = turjuman.turjuman(logger, cache_dir)

The output

.. code-block:: console

         2022-05-18 19:00:11 | INFO | turjuman.translate | Loading model from UBC-NLP/turjuman


Translate using beam search (default)
-------------------------------------
``Beam search`` is the ``default`` generation method on Turjuman
   -  Beam search default setting:

      -  ``-s`` or ``--seq_length``: The maximum sequence length value, (``default vlaue is 300``)
      -  ``-o`` or ``--max_outputs``: The maxmuim of the output tanslations (``default vlaue is 1``)
      -  ``-b`` or ``--num_beams NUM_BEAMS``: Number of beams (``default vlaue is 1``)
      -  ``-n`` or ``--no_repeat_ngram_size``: Number of n-gram that doesn't appears twice (``default vlaue is 2``)


.. code:: python

      beam_options = {"search_method":"beam", "seq_length": 300, "num_beams":5, "no_repeat_ngram_size":2, "max_outputs":1}
      target = torj.translate("As US reaches one million COVID deaths, how are Americans coping?",**beam_options)
      print (target)

.. code-block:: console
         2022-05-18 19:02:59 | INFO | turjuman.translate | Using beam search
         2022-05-18 19:03:02 | INFO | turjuman.translate | Extract outputs

.. code-block:: console

         {'source': 'As US reaches one million COVID deaths, how are Americans coping?', 'target': ['وبينما تصل الولايات المتحدة إلى مليون حالة وفاة من فيروس كوفيد-19 ، كيف يتعامل الأمريكيون مع ذلك ؟']}

Translate using greedy search
-----------------------------------
 ``Greedy search`` default setting:
   -  ``-s`` or ``--seq_length``: The maximum sequence length value, (``default vlaue is 300``)
.. code:: python

      greedy_options = {"search_method":"greedy", "seq_length": 300}
      target = torj.translate("As US reaches one million COVID deaths, how are Americans coping?",**greedy_options)
      print (target)

.. code-block:: console

         2022-05-18 19:04:37 | INFO | turjuman.translate | Using greedy search
         2022-05-18 19:04:39 | INFO | turjuman.translate | Extract outputs

.. code-block:: console

         {'source': 'As US reaches one million COVID deaths, how are Americans coping?', 'target': ['وبما أن الولايات المتحدة تصل إلى مليون حالة وفاة من فيروس كوفيد-19 ، كيف يمكن للولايات المتحدة أن تتصدى لهذا ؟']}

Translate using sampling search
------------------------------------

``Sampling search`` default setting:

      -  ``-s`` or ``--seq_length``: The maximum sequence length value, (``default vlaue is 300``)
      -  ``-o`` or ``--max_outputs``: The maxmuim of the output tanslations (``default vlaue is 1``)
      -  ``-k`` or ``--top_k``: Sample from top K likely next words instead of all words (``default vlaue is 50``)
      -  ``-p`` or ``--top_p``: Sample from the smallest set whose cumulative probability mass exceeds p for next words (``default vlaue is 0.95``)

.. code:: python

      sampling_options = {"search_method":"sampling", "seq_length": 300, "max_outputs":1, "top_p":0.95, "top_k":50}
      target = torj.translate("As US reaches one million COVID deaths, how are Americans coping?",**sampling_options)
      print (target)

.. code-block:: console

         2022-05-18 19:09:12 | INFO | turjuman.translate | Using sampling search
         2022-05-18 19:09:14 | INFO | turjuman.translate | Extract outputs

.. code-block:: console

         {'source': 'As US reaches one million COVID deaths, how are Americans coping?', 'target': ['وبما أن الولايات المتحدة تصل إلى مليون حالات وفاة بسبب كوفيد-19 ، كيف يعالج الأميركيون الأمر ؟']}

Read and translate text from file
--------------------------------------

   -  ``-f`` or ``--input_file``: import the text from file. The translation will saved on the JSON format file
   -  ``-bs`` or ``--batch_size``: The maximum number of source examples utilized in one iteration (``default value is 25``)
   - ``gen_options``: Generation options

.. code:: python

      gen_options = {"search_method":"beam", "seq_length": 300, "num_beams":5, "no_repeat_ngram_size":2, "max_outputs":1}
      torj.translate_from_file("samples.txt", batch_size=25, **gen_options)


Google Colab Link
-----------------

You can find the full examples on the Google Colab on the following link
https://colab.research.google.com/github/UBC-NLP/turjuman/blob/main/examples/Integrate_turjuman_with_your_code.ipynb
