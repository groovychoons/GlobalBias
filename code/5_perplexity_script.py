## This script was run with 2 A100 GPUs with 40GB RAM each

import pandas as pd
import lmppl
from tqdm import tqdm
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--model_name', type=str, help='Name of the model')
parser.add_argument('--model_type', type=str, help='Type of model')
parser.add_argument('--num_gpus', type=int, help='Number of GPUs available')

args = parser.parse_args()


filename = '../data/4b_gp_templates.csv'  ## or '../data/4a_full_templates.csv'
df = pd.read_csv(filename, on_bad_lines='warn')

df = df.drop(columns=['Unnamed: 0'])
print(df.head())


if args.model_type == 'MaskedLM':
    scorer = lmppl.MaskedLM(args.model_name, num_gpus=args.num_gpus, max_length=22)
elif args.model_type == 'EncoderDecoderLM':
    scorer = lmppl.EncoderDecoderLM(
        args.model_name, 
        num_gpus=args.num_gpus, 
        device_map="auto", 
        low_cpu_mem_usage=True
        )
elif args.model_type == 'LM':
    scorer = lmppl.LM(
        args.model_name, 
        num_gpus=args.num_gpus,
        device_map="auto", 
        low_cpu_mem_usage=True
        )


# Function to get the perplexity value for a given template
def get_perplexity(template):
    results = scorer.get_perplexity(template)
    return results

def get_encdec_perplexity(row, i):
    outputs = row[f'partial_{i}'] + "."
    if i == 1:
        inputs = row['input_1']
    else:
        inputs = row['firstname'] + ' '
    return scorer.get_perplexity(input_texts=inputs, output_texts=outputs)


tqdm.pandas()
for i in range(1,4):
    if args.model_type == 'EncoderDecoderLM':
        df[f'perplexity_{i}'] = df.progress_apply(lambda row: get_encdec_perplexity(row, i), axis=1)
    else:     
        df[f'perplexity_{i}'] = df[f'template_{i}'].progress_apply(get_perplexity)

modified_name = (args.model_name).replace("/", "_")

df.to_csv(f'../results/1_{modified_name}_results.csv', index=False)

print(df.head())

