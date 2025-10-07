import streamlit as st
import pandas as pd
import numpy as np 

st.title("Day 28 : My First Streamlit Dashboard")

df = pd.DataFrame({
    'number':np.arange(1,11),
    'squared': np.arange(1,11) ** 2,
    'cubed':np.arange(1,11) **3
})

st.write("Numbers Table",df)

st.line_chart(df[['number','squared','cubed']])

multiplier = st.slider("Multiply numbers by : ",1,10,2)
st.write('Numbers multiplied: ',df['number']* multiplier)