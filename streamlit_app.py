import streamlit as st
import pandas as pd

st.title('Machine Learning App')
st.info('This is an app for machine learning model')

with st.expander('Data'):
  st.write('**Raw Data**')

  df = pd.read_csv('https://raw.githubusercontent.com/alexsbekele/data/main/penguins_cleaned%20(1).csv')
  df
  st.write('**X**')
  x_row = df.drop('species', axis = 1)
  x_row
  st.write('**Y**')
  y_row = df.species
  y_row
with st.expander('Data Visualization'):
  st.scatter_chart(data = df, x = 'bill_length_mm', y = 'body_mass_g', color = 'species')

  
  #Data Preparation
  with st.sidebar:
    st.header('Input Features')
    island = st.selectbox('Island',('Biscoe', 'Dream', 'Torgersen') )
    bill_length_mm = st.slider('Bill length (mm)', 32.1, 59.6, 43.9)
    bill_depth_mm = st.slider('Bill depth (mm)', 13.1, 21.5, 17.2)
    flipper_length_mm = st.slider('Flipper length (mm)', 172.0, 231.0, 201.0)
    body_mass_g = st.slider('Body mass (g)', 2700.0, 6300.0, 4207.0)
    gender = st.selectbox('Gender', ('male', 'female'))

    #Create a data frame for data input features
    data = {
      'island': island,
      'bill_length_mm': bill_length_mm,
      'bill_depth_mm': bill_depth_mm,
      'flipper_length_mm': flipper_length_mm,
      'body_mass_g': body_mass_g,
      'sex': gender
    }
  input_df = pd.DataFrame(data, index = [0])
  input_penguins = pd.concat([input_df, x_row], axis = 0)
#Encode x
encode = ['island', 'sex']
df_penguins = pd.get_dummies(input_penguins, prefix = encode)
input_row = df_penguins[:1]

#encode y
target_mapper = {
  'Adelie': 0,
  'Chinstrap': 1,
  'Gentoo': 2
}
def target_encode(value):
  return target_mapper(value)
y = y_row.apply(target_encode)
y
y_row
with st.expander('Input Features'):
  st.write('**Input Penguin**')
  input_df
  st.write('**Compined Penguin data**')
  input_penguins
  st.write('**Encoded input penguins**')
  input_row



