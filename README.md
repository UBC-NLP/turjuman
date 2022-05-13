<p align="center">
    <br>
    <img src="./images/turjuman_logo.png"/>
    <br>
<p>

<p align="center">
<a href="https://turjuman.dlnlp.ai">
        <img alt="Documentation" src="https://img.shields.io/website.svg?down_color=red&down_message=offline&up_message=online&url=https://turjuman.dlnlp.ai">
    </a>
    
<a href="https://github.com/UBC-NLP/turjuman/blob/main/LICENSE"><img alt="GitHub license" src="https://img.shields.io/github/license/UBC-NLP/turjuman?logoColor=blue"></a>

<a href="https://github.com/UBC-NLP/turjuman/stargazers"><img alt="GitHub stars" src="https://img.shields.io/github/stars/UBC-NLP/turjuman"></a>

<a href="https://github.com/UBC-NLP/turjuman/network"><img alt="GitHub forks" src="https://img.shields.io/github/forks/UBC-NLP/turjuman"></a>


</p>
 
<img src="./images/turjuman.png" alt="AraT5" width="55%" height="45%" align="right"/>

TURJUMAN, a neural toolkit for translating from 20 languages into Modern Standard Arabic (MSA). TURJUMAN exploits the recently-introduced text-to-text Transformer [AraT5 model](https://github.com/UBC-NLP/araT5) (Nagoudi et al., 2022), endowing it with a powerful ability to decode into Arabic. The toolkit offers the possibility of employing a number of diverse decoding methods, making it suited for acquiring paraphrases for the MSA translations as an added value. To train TURJUMAN, we sample from publicly available parallel data employing a simple semantic similarity method to ensure data quality.

## Requirements and Installation
- To install turjuman and develop directly using pip:
 ```shell
    pip install turjuman
    or 
    pip install git+https://github.com/UBC-NLP/turjuman.git
 ```
- To install turjuman and develop locally:
 ```shell
    git clone https://github.com/UBC-NLP/turjuman.git
    cd turjuman
    pip install .
```
## Getting Started
The [full documentation](https://turjuman.readthedocs.io/en/latest/) contains instructions for getting started, translation using diffrent methods, intergrate Turjuman with your code, and provides more examples.

## Colab Examples
| Command 	| Description 	| Example Link 	|
|---------	|-------------	|--------------	|
| turjuman_translate |             	| [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/UBC-NLP/turjuman/blob/main/examples/turjuman_translate_cli.ipynb) |
|    turjuman_interactive     	|             	|              	|
|    turjuman_score     	|             	|              	|
-
## License
turjuman(-py) is MIT-licensed. The license applies to the pre-trained models as well.
## Citation
If you use TURJUMAN toolkit for your scientific publication, or if you find the resources in this repository useful, please cite our paper as follows (to be updated):
```


```



## 7. Acknowledgments
We gratefully acknowledge support from the Natural Sciences and Engineering Research Council  of Canada, the  Social  Sciences and  Humanities  Research  Council  of  Canada, Canadian  Foundation  for  Innovation,  [ComputeCanada](www.computecanada.ca) and [UBC ARC-Sockeye](https://doi.org/10.14288/SOCKEYE). We  also  thank  the  [Google TensorFlow Research Cloud (TFRC)](https://www.tensorflow.org/tfrc) program for providing us with free TPU access.