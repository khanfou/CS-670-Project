import streamlit as st
from datasets import load_dataset

dataset_dict = load_dataset("HUPD/hupd",streaming=True)

df = pd.DataFrame.from_dict(dataset_dict["train"])

# Create a DataFrame object from list
df = pd.DataFrame(df,columns =['patent_number','decision', 'abstract', 'claims','filing_date'])
st.dataframe(df)
