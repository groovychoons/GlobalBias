## Who is better at math, Jenny or Jingzhen? Exploring Intersectional Biases in Large Language Models
<!-- 
This paper  -->

### Installation and setup

After you clone this repository:

- Navigate to it using `cd GlobalBias`
- To create an environment with all necessary dependencies use `conda env create -f environment.yml`
- Activate the environment with `conda activate globalbias`

### Reproducibility

You can build the GlobalBias dataset using:

`python code/0_build_globalbias.py`

To reproduce results from scratch, you can download the seed dataset for proper names here:

[Torvik, Vetle (2018): Genni + Ethnea for the Author-ity 2009 dataset.](https://databank.illinois.edu/datasets/IDB-9087546)

Everything else you need is in the code and data folders.

### Explanation of repo

<< Coming soon >>
<!-- 
### Why are we doing it?

Research questions:
- Can we better represent bias for intersectional identities using phrases (instead of single words/names) within word embedding models?
- Can we better understand intersectional stereotypes through the use of these phrases?
- Can we understand intersectional biases for more groups of people?

Novel contributions:
- Using phrases, allows us to look at identities previously not able to
- Detecting intersectional bias for Asian and Middle Eastern Americans
- Using a one-versus-rest methodology instead of comparing two groups directly
    - Used in Guo/Caliskan for validation experiments but not for the bias detection



We evaluate whether more bias is detected using these phrases or with names (e.g. European American and African American names) using IBD and EIBD [(Guo and Caliskan, 2021)](https://arxiv.org/abs/2006.03955) as evaluation metrics.

- [Distributional techniques for philosophical enquiry (Herbelot et. al, 2012)](https://aclanthology.org/W12-1008.pdf)
More info about this paper - first to look at phrases over multiplicative model - before SWE were a thing but compares using phrase 'black_woman' built into a word distribution, rather than taking the sum of its parts (black x woman) -->
