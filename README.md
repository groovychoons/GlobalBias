## Who is better at math, Jenny or Jingzhen? Exploring Intersectional Biases in Large Language Models

Paper: https://arxiv.org/pdf/2407.06917

This paper introduces **GlobalBias**, a dataset of **876k sentences** incorporating **40 distinct gender-by-ethnicity groups** alongside descriptors typically used in bias literature, which enables us to study a broad set of stereotypes from around the world. 

We use GlobalBias to **directly probe a suite of LMs via perplexity**, which we use as a proxy to determine how certain stereotypes are represented in the model's internal representations. Following this, we **generate character profiles based on given names** and evaluate the prevalence of stereotypes in model outputs. 

### Installation and setup

After you clone this repository:

- Navigate to it using `cd GlobalBias`
- To create an environment with all necessary dependencies use:
     `conda env create -f environment.yml`
- Activate the environment with `conda activate globalbias`

### Building the GlobalBias dataset

You can build the GlobalBias dataset using:

`python code/0_build_globalbias.py`

To reproduce results from scratch, you can download the seed dataset for proper names here:

[Torvik, Vetle (2018): Genni + Ethnea for the Author-ity 2009 dataset.](https://databank.illinois.edu/datasets/IDB-9087546)

Everything else you need is in the code and data folders.

### Repo Walkthrough

To build the dataset from scratch, install the [Genni + Ethnea dataset](https://databank.illinois.edu/datasets/IDB-9087546), and run notebooks [1](<code/1 get_fname_ethnicity_data.ipynb>), [2](<code/2 get_embeddings.ipynb>), [3](<code/3 clustering.ipynb>) and [4](<code/4 full_templates.ipynb>).

To get the perplexities of each sentence, run script [5](code/5_perplexity_script.py). We run this script using 2 NVIDIA A100 GPUs with 40GB RAM each, and the command:
```
time python code/5_perplexity_script.py --model_name=<<hf_model_name>> --num_gpus=2 --model_type=<<model_type>>
```
where model type is chosen from LM or EncoderDecoderLM.

To reproduce results in section 4, run notebooks [6](<code/6 gp_evaluation.ipynb>) and [7](<code/7 gp_mrr.ipynb>). To reproduce results in section 5, run notebook [8](<code/8 hb_evaluation.ipynb>).

The generation task outputs for this paper can be found in 'data/10a_..._full.csv'. Code in notebooks [9a](<code/9a openai_generation_output.ipynb>), [9b](<code/9b llama_generation_output.ipynb>) and [9c](<code/9c claude_generation_output.ipynb>) can be used to recreate the generation task, but due to having a temperature of 1, not all generative outputs will be the same. Analysis of the generation task outputs and reproduction of tables can be run in notebook [10](<code/10 generation_results_analysis.ipynb>).

**Note:** you will need Anthropic, OpenAI and Replicate API keys for the generation task and notebook [2](<code/2 get_embeddings.ipynb>). An example can be found in [.env.example](.env.example).

### Novel Contributions

- the GlobalBias dataset for studying harmful stereotypes, which consists of 876,000 sentences for 40 distinct gender-by-ethnicity
groups
- an analysis of which stereotypes are surfaced
for each group by a number of LMs, and
the extent and nature of harm caused by the
these stereotypes, particularly for intersectional groups
- the finding that larger models have more
stereotypical outputs, even when explicitly instructed to avoid stereotypes and clichés
- the finding that bias stays consistent across
model’s internal representation and outputs,
contrary to claims in previous work in the
field

### Citing GlobalBias
If you use GlobalBias in your research, please use the following bib entry to cite the [reference paper](https://arxiv.org/abs/2407.06917).
```
@misc{siddique2024bettermathjennyjingzhen,
      title={Who is better at math, Jenny or Jingzhen? Uncovering Stereotypes in Large Language Models}, 
      author={Zara Siddique and Liam D. Turner and Luis Espinosa-Anke},
      year={2024},
      eprint={2407.06917},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2407.06917}, 
}
```

