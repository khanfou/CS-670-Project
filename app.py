import streamlit as st
from datasets import load_dataset

dataset_dict = load_dataset("HUPD/hupd",streaming=True, train_filing_start_date='2016-01-01',train_filing_end_date='2016-01-31',val_filing_start_date='2017-01-01',val_filing_end_date='2017-01-31')

df = pd.DataFrame.from_dict(dataset_dict["train"])

# Create a DataFrame object from list
df = pd.DataFrame(df,columns =['patent_number','decision', 'abstract', 'claims','filing_date'])
st.dataframe(df)
