import streamlit as st
from datasets import load_dataset
import pandas as pd

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
#st.dataframe(df)
PAN = df['patent_number'].drop_duplicates()

st.title('Harvard USPTO Patentability Score')
#make_choice = st.sidebar.selectbox('Select the Patent Application Number:', PAN)
make_choice = st.selectbox('Select the Patent Application Number:', PAN)

form = st.form(key='patent-form')


pd.options.display.max_colwidth = 100000

abstract = df["abstract"].loc[df["patent_number"] == make_choice]
st.info(abstract)
#st.markdown(f"Publication abstract is **{abstract}** 🎈")
#st.write ("Publication Abstract", abstract)


claims = df["claims"].loc[df["patent_number"] == make_choice]
st.markdown(f"Publication Claim is **{claims}** 🎈")

