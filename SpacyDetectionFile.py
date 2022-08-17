from flask import Flask, render_template, request
import spacy
nlp = spacy.load('en_core_web_sm')

import pandas as pd
data=pd.read_csv('Task_Heptagon.csv')
data["ptitle"] = data["ptitle"].str.replace(r"[^a-zA-Z0-9 ]+", " ").str.strip()
date_label = ['ORG','PRODUCT']

def extract(text):
    doc = nlp(text)
    results = [(ent.text, ent.label_) for ent in doc.ents if ent.label_ in date_label]
    return results

data['entities'] = data['ptitle'].apply(extract)
data.columns
data['entities'] = data['entities'].str[0].fillna("Others")
final_data=data[['ptitle','entities']]
final_data.to_csv('Entity Data.csv')