import streamlit as st
import pandas as pd

st.title(' Machine Learning App')

st.info('This is an app for machine learning model')
df = pd.read_csv('https://github.com/alexsbekele/data/main/penguins_cleaned(1).csv')
df
