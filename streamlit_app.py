import streamlit as st
import pandas as pd

st.title('Machine Learning App')
st.info('This is an app for machine learning model')

with st.expander('Data'):
  st.write('**Raw Data**')

  df = pd.read_csv('https://raw.githubusercontent.com/alexsbekele/data/main/penguins_cleaned%20(1).csv')
  df
