import streamlit as st
from datasets import load_dataset

dataset = load_dataset("HUPD/hupd",'sample',split='train', streaming=True)


#df = pd.DataFrame.from_dict(dataset_dict["train"])

# Create a DataFrame object from list
#df = pd.DataFrame(df,columns =['patent_number','decision', 'abstract', 'claims','filing_date'])
#st.dataframe(df)


#from datasets import load_dataset
#dataset = load_dataset('oscar-corpus/OSCAR-2201', 'en', split='train', streaming=True)
for example in dataset:
  print(example)
  break
