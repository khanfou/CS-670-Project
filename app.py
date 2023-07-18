import streamlit as st
from datasets import load_dataset
import pandas as pd

#dataset = load_dataset("HUPD/hupd",'sample',split='train', streaming=True)
#for example in dataset:
  #print(example)
  #break

#df = pd.DataFrame.from_dict(dataset_dict["train"])

# Create a DataFrame object from list
#df = pd.DataFrame(df,columns =['patent_number','decision', 'abstract', 'claims','filing_date'])
#st.dataframe(df)


#from datasets import load_dataset
#dataset = load_dataset('oscar-corpus/OSCAR-2201', 'en', split='train', streaming=True)

from datasets import load_dataset
dataset_dict = load_dataset('HUPD/hupd',
    name='sample',
    data_files="https://huggingface.co/datasets/HUPD/hupd/blob/main/hupd_metadata_2022-02-22.feather", 
    icpr_label=None,
    train_filing_start_date='2016-01-01',
    train_filing_end_date='2016-01-31',
    val_filing_start_date='2017-01-22',
    val_filing_end_date='2017-01-31',
)

df = pd.DataFrame.from_dict(dataset_dict["train"])
df = pd.DataFrame(df,columns =['patent_number','decision', 'abstract', 'claims','filing_date'])
st.dataframe(df)

