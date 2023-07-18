import os
import pandas as pd
import streamlit as st
HG_DIR = '/nlp/scr/msuzgun/cache_extra/huggingface'
# Specify HG cache dirs -- currently use only for 2.7b model
os.environ['TRANSFORMERS_CACHE'] = f'{HG_DIR}/transformers'
os.environ['HF_HOME'] = HG_DIR

## Import relevant libraries and dependencies
!pip install datasets
!pip install Transformers
!pip install streamlit
# Pretty print
from pprint import pprint
# Datasets load_dataset function
from datasets import load_dataset
# Transformers Autokenizer
from transformers import AutoTokenizer
tokenizer = AutoTokenizer.from_pretrained('distilbert-base-uncased')
# Standard PyTorch DataLoader
from torch.utils.data import DataLoader



dataset_dict = load_dataset('HUPD/hupd',
    name='sample',
    data_files="https://huggingface.co/datasets/HUPD/hupd/blob/main/hupd_metadata_2022-02-22.feather", 
    cache_dir ='/u/scr/nlp/data/HUPD',
    icpr_label=None,
    train_filing_start_date='2016-01-01',
    train_filing_end_date='2016-01-31',
    val_filing_start_date='2017-01-01',
    val_filing_end_date='2017-01-31',
)

df = pd.DataFrame.from_dict(dataset_dict["train"])

# Create a DataFrame object from list
df = pd.DataFrame(df,columns =['patent_number','decision', 'abstract', 'claims','filing_date'])
st.dataframe(df)
