import streamlit as st
import pandas as pd 
import numpy as np 


### Title of the application 
st.title ("hello")

## Display a simple text 

st.write("this is a simple text")

## dataframe

df = pd.DataFrame({
  'first column': [1,2,3]
  '2nd column': [10,20,30]
})

## display df

st.write("here is the dataframe")

st.write(df)

## create a line chart

chart_data=pd.DataFrame(
  np.random.randm(20,3), columns=['a','b','c']
)
st.line_chart(chart_data)














