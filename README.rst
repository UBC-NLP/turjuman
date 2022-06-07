Turjuman, a neural toolkit for translating from 20 languages into Modern
Standard Arabic (MSA) that described in our OSACT5 2022 paper `TURJUMAN:
A Public Toolkit for Neural Arabic Machine Translation`.

TURJUMAN exploits the recently-introduced our text-to-text Transformer
`AraT5 model <https://github.com/UBC-NLP/araT5>`__ , endowing it with a powerful ability to decode into Arabic. The
toolkit offers the possibility of employing a number of diverse decoding
methods, making it suited for acquiring paraphrases for the MSA
translations as an added value. To train TURJUMAN, we sample from
publicly available parallel data employing a simple semantic similarity
method to ensure data quality.

GitHub link: `https://github.com/UBC-NLP/turjuman <https://github.com/UBC-NLP/turjuman>`__

Online demo link: `https://demos.dlnlp.ai/turjuman <https://demos.dlnlp.ai/turjuman/>`__ 


Getting Started
---------------

The `full documentation <https://turjuman.readthedocs.io/en/latest/>`__
contains instructions for getting started, translation using diffrent
methods, intergrate Turjuman with your code, and provides more examples.


License
-------

turjuman(-py) is Apache-2.0 licensed. The license applies to the
pre-trained models as well.

Citation
--------

If you use TURJUMAN toolkit or the pre-trained models for your
scientific publication, or if you find the resources in this repository
useful, please cite our paper as follows:

::

   @inproceedings{nagoudi-osact5-2022-turjuman,
     title={TURJUMAN: A Public Toolkit for Neural Arabic Machine Translation},
     author={Nagoudi, El Moatez Billah and Elmadany, AbdelRahim and Abdul-Mageed, Muhammad},
     booktitle = "Proceedings of the 5th Workshop on Open-Source Arabic Corpora and Processing Tools (OSACT5)",
     month = "June",
     year = "2022",
     address = "Marseille, France",
     publisher = "European Language Resource Association",
   }

7. Acknowledgments
------------------

We gratefully acknowledge support from the Natural Sciences and Engineering Research Council of Canada (NSERC; RGPIN-2018-04267), the Social Sciences and Humanities Research Council of Canada (SSHRC; 435-2018-0576; 895-2020-1004; 895-2021-1008),  `ComputeCanada (CC) <www.computecanada.ca>`__ and `UBC
ARC-Sockeye <https://doi.org/10.14288/SOCKEYE>`__ and Advanced Micro Devices, Inc. (AMD). Any opinions, conclusions or recommendations expressed in this material are those of the author(s) and do not necessarily reflect the views of NSERC, SSHRC, CFI, CC, AMD, or UBC ARC-Sockeye. 
