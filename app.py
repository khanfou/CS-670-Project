import streamlit as st
from datasets import load_dataset
from transformers import pipeline
import pandas as pd
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline
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
#make_choice = st.sidebar.selectbox('Select the Patent Application Number:', PAN)

#####NEW
with st.form("patent-form"):
    make_choice = st.selectbox('Select the Patent Application Number:', PAN)
    submitted = st.form_submit_button(label='submit')
    
    if submitted:
        #st.write("Outside the form")
        model_name = "distilbert-base-uncased-finetuned-sst-2-english"
        model = AutoModelForSequenceClassification.from_pretrained(model_name)
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        classifier = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)
        abstract = df['abstract'].loc[df['patent_number'] == make_choice].astype("string")
        #X_train = df['id'].astype("string")
        #X_train = abstract.values.tolist()
        results = classifier(abstract, truncation=True)
        #result = hupd_model(make_choice)[0]
        score = result['score']
        st.write("The Patentability Score is:", score)

        
######NEW

pd.options.display.max_colwidth = 100000

abstract = df["abstract"].loc[df["patent_number"] == make_choice]
st.subheader(':red[Patent Application]')
st.subheader(':red[Abstract:]')
st.info(abstract)
#st.markdown(f"Publication abstract is **{abstract}** 🎈")


claims = df["claims"].loc[df["patent_number"] == make_choice]
st.subheader(':red[Claim:]')
st.info(claims)
#st.markdown(f"Publication Claim is **{claims}** 🎈")

#form = st.form(key='patent-form')
#submit = form.sidebar.form_submit_button('Submit')

