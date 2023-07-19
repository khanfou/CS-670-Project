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

#from google.colab import data_table
#data_table.enable_dataframe_formatter()
df = pd.DataFrame.from_dict(dataset_dict["train"])
df = pd.DataFrame(df,columns =['patent_number','decision', 'abstract', 'claims','filing_date'])
#st.dataframe(df)
PAN = df['patent_number'].drop_duplicates()
make_choice = st.sidebar.selectbox('Select the Patent Application Number:', PAN)

form = st.form(key='patent-form')


#loooong_text = ' '.join(["abcd efg hijk lmnop lmnop qrst uvw xyz"]*1_000)
#abstract = df["abstract"].loc[df["patent_number"] == make_choice]
#abstract = ''.join([abstract]*1_000)
#st.markdown("st.markdown : " + loooong_text)
#st.markdown("Publication abstract is: " + abstract)

abstract = df["abstract"].loc[df["patent_number"] == make_choice]
st.write(abstract.to_html(), unsafe_allow_html=True)
#st.markdown(f"Publication abstract is **{abstract}** 🎈")


claims = df["claims"].loc[df["patent_number"] == make_choice]
st.markdown(f"Publication abstract is **{claims}** 🎈")

