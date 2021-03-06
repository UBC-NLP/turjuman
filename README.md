<p align="center">
    <br>
    <img src="./images/turjuman_logo.png"/>
    <br>
<p>

<p align="center">
<a href="https://github.com/UBC-NLP/turjuman/releases">
        <img alt="GitHub release" src="https://img.shields.io/github/release/UBC-NLP/turjuman.svg">
    </a>

<a href="https://demos.dlnlp.ai/turjuman">
        <img alt="Documentation" src="https://img.shields.io/website.svg?down_color=red&down_message=offline&up_message=online&url=https://demos.dlnlp.ai/turjuman">
    </a>
<a href="https://github.com/UBC-NLP/turjuman/blob/main/LICENSE"><img alt="GitHub license" src="https://img.shields.io/github/license/UBC-NLP/turjuman?logoColor=blue"></a>
<a href='https://turjuman.readthedocs.io/en/latest/?badge=latest'><img src='https://readthedocs.org/projects/turjuman/badge/?version=latest' alt='Documentation Status' /></a>
<a href="https://github.com/UBC-NLP/turjuman/stargazers"><img alt="GitHub stars" src="https://img.shields.io/github/stars/UBC-NLP/turjuman"></a>
<a href="https://github.com/UBC-NLP/turjuman/network"><img alt="GitHub forks" src="https://img.shields.io/github/forks/UBC-NLP/turjuman"></a>

</p>
 

<img src="./images/turjuman.png" alt="AraT5" width="55%" height="55%" align="right"/>

Turjuman is a neural machine translation toolkit. It translates from 20 languages into Modern Standard Arabic (MSA). Turjuman is described in this paper: 
[**TURJUMAN: A Public Toolkit for Neural Arabic Machine Translation**](https://arxiv.org/abs/2206.03933).

Turjuman exploits our [AraT5 model](https://github.com/UBC-NLP/araT5). This endows Turjuman with a powerful ability to decode into Arabic. The toolkit offers the possibility of employing a number of diverse decoding methods, making it suited for acquiring paraphrases for the MSA translations as an added value.

<br>

## Requirements and Installation
- To install turjuman and develop directly using pip:
```shell
    pip install -U turjuman
```
- To install turjuman and develop directly GitHub repo using pip:
```shell
    pip install -U git+https://github.com/UBC-NLP/turjuman.git
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
### (1) Command Line Interface
<table style='border:1px red;' width='100%'>
<tr><td><b>Command</b></td><td> <b>Content</b></td><td><b>Colab link</b></td></tr>
<tr>
<td>turjuman_translate</td>
<td>
    <ul>
        <li> Usage and Arguments </li>
        <li> Translate using greedy search</li>
        <li> Translate using beam search (default)</li>
        <li> Translate using sampling search</li>
        <li> Read and translate text from file</li>
    </ul>
</td>
<td>
<a href="https://colab.research.google.com/github/UBC-NLP/turjuman/blob/main/examples/turjuman_translate_cli.ipynb"><img alt="colab" src="https://colab.research.google.com/assets/colab-badge.svg"></a>

 </td>
</tr>
<tr>
<td>turjuman_interactive</td>
<td>
    <ul>
        <li> Usage and Arguments </li>
        <li> Examples</li>
    </ul>
</td>
<td> <a href="https://colab.research.google.com/github/UBC-NLP/turjuman/blob/main/examples/turjuman_interactive_cli.ipynb"><img alt="colab" src="https://colab.research.google.com/assets/colab-badge.svg"></td>
</tr>
<tr>
<td>turjuman_score</td>
<td>
    <ul>
        <li> Usage and Arguments </li>
        <li> Input files format</li>
        <li> Example</li>
    </ul>
</td>
<td> <a href="https://colab.research.google.com/github/UBC-NLP/turjuman/blob/main/examples/turjuman_score_cli.ipynb"><img alt="colab" src="https://colab.research.google.com/assets/colab-badge.svg"></a></td>
</tr>

</table>

### (2) Integrate Turjuman with your python code
<table style='border:1px red;' width='100%'>
<tr><td><b>Functions</b></td><td> <b>Content</b></td><td><b>Colab link</b></td></tr>
<td>translate <br> translate_from_file</td>
<td>
    <ul>
        <li> Install Turjuman </li>
        <li> Initial turjuman object </li>
        <li> Translate using greedy search</li>
        <li> Translate using beam search (default)</li>
        <li> Translate using sampling search</li>
        <li> Read and translate text from file</li>
    </ul>
</td>
<td> <a href="https://colab.research.google.com/github/UBC-NLP/turjuman/blob/main/examples/Integrate_turjuman_with_your_code.ipynb"><img alt="colab" src="https://colab.research.google.com/assets/colab-badge.svg"></td>
</tr>
</table>

## License
turjuman(-py) is Apache-2.0 licensed. The license applies to the pre-trained models as well.

## Citation
If you use TURJUMAN toolkit or the pre-trained models for your scientific publication, or if you find the resources in this repository useful, please cite our paper as follows (to be updated):
```
@inproceedings{nagoudi-osact5-2022-turjuman,
  title={TURJUMAN: A Public Toolkit for Neural Arabic Machine Translation},
  author={Nagoudi, El Moatez Billah and Elmadany, AbdelRahim and Abdul-Mageed, Muhammad},
  booktitle = "Proceedings of the 5th Workshop on Open-Source Arabic Corpora and Processing Tools (OSACT5)",
  month = "June",
  year = "2022",
  address = "Marseille, France",
  publisher = "European Language Resource Association",
}

```



## Acknowledgments
We gratefully acknowledge support from the Natural Sciences and Engineering Research Council of Canada (NSERC; RGPIN-2018-04267), the Social Sciences and Humanities Research Council of Canada (SSHRC; 435-2018-0576; 895-2020-1004; 895-2021-1008), Canadian Foundation for Innovation (CFI; 37771), [ComputeCanada (CC)](www.computecanada.ca),   [UBC ARC-Sockeye](https://doi.org/10.14288/SOCKEYE) and Advanced Micro Devices, Inc. (AMD). Any opinions, conclusions or recommendations expressed in this material are those of the author(s) and do not necessarily reflect the views of NSERC, SSHRC, CFI, CC, AMD, or UBC ARC-Sockeye. 
