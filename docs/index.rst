Turjuman documentation
=======================
.. raw:: html

   <p align="center">
    <br>
    <img src="https://github.com/UBC-NLP/turjuman/raw/master/images/turjuman_logo.png"/>
    <br>
   <p>

.. raw:: html

   <img src="https://github.com/UBC-NLP/turjuman/raw/master/images/turjuman.png" alt="AraT5" width="50%" height="50%" align="right"/>



Turjuman is a neural machine translation toolkit. It translates from 20 languages into Modern Standard Arabic (MSA). Turjuman is described in this paper: `TURJUMAN: A Public Toolkit for Neural Arabic Machine Translation <https://arxiv.org/abs/2206.03933>`__.

Turjuman exploits our `AraT5 model <https://github.com/UBC-NLP/araT5>`__. This endows Turjuman with a powerful ability to decode into Arabic. The toolkit offers the possibility of employing a number of diverse decoding methods, making it suited for acquiring paraphrases for the MSA translations as an added value.
   
:github: https://github.com/UBC-NLP/turjuman
:demo: https://demos.dlnlp.ai/turjuman
:paper: https://arxiv.org/abs/2206.03933

 
.. toctree::
    :maxdepth: 1
    :caption: Command Line Interfaces

    installation
    turjuman_translate_cli
    turjuman_interactive_cli
    turjuman_score_cli

.. toctree::
    :maxdepth: 1
    :caption: Integration

    Integrate_turjuman_with_your_code
