# TURJUMAN
<img src="./images/turjuman.png" alt="AraT5" width="55%" height="45%" align="right"/>

TURJUMAN, a neural toolkit for translating from 20 languages into Modern Standard Arabic (MSA). TURJUMAN exploits the recently-introduced text-to-text Transformer [AraT5 model](https://github.com/UBC-NLP/araT5) (Nagoudi et al., 2022), endowing it with a powerful ability to decode into Arabic. The toolkit offers the possibility of employing a number of diverse decoding methods, making it suited for acquiring paraphrases for the MSA translations as an added value. To train TURJUMAN, we sample from publicly available parallel data employing a simple semantic similarity method to ensure data quality.

## How to install
 - Using pip
 ```shell
    pip install turjuman
    or 
    pip install git+https://github.com/UBC-NLP/turjuman.git
 ```


## Citation
If you use TURJUMAN toolkit for your scientific publication, or if you find the resources in this repository useful, please cite our paper as follows (to be updated):
```


```



## 7. Acknowledgments
We gratefully acknowledge support from the Natural Sciences and Engineering Research Council  of Canada, the  Social  Sciences and  Humanities  Research  Council  of  Canada, Canadian  Foundation  for  Innovation,  [ComputeCanada](www.computecanada.ca) and [UBC ARC-Sockeye](https://doi.org/10.14288/SOCKEYE). We  also  thank  the  [Google TensorFlow Research Cloud (TFRC)](https://www.tensorflow.org/tfrc) program for providing us with free TPU access.