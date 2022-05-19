Turjuman Toolkit Documentation
=====================
.. raw:: html

   <p align="center">
    <br>
    <img src="../images/turjuman_logo.png"/>
    <br>
   <p>

.. raw:: html

   <img src="../images/turjuman.png" alt="AraT5" width="65%" height="65%" align="right"/>


TURJUMAN TURJUMAN, a neural toolkit for translating from 20 languages into Modern Standard Arabic (MSA). TURJUMAN exploits the recently-introduced text-to-text Transformer `AraT5 model <https://github.com/UBC-NLP/araT5>`__ (Nagoudi et al., 2022), endowing it with a powerful ability to decode into Arabic. The toolkit offers the possibility of employing a number of diverse decoding methods, making it suited for acquiring paraphrases for the MSA translations as an added value. To train TURJUMAN, we sample from publicly available parallel data employing a simple semantic similarity method to ensure data quality.

   
   
.. toctree::
    :maxdepth: 1
    :caption: Command Line Interfaces

    installation
    turjuman_translate_cli