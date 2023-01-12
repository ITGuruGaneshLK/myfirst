import streamlit as st
import pandas as pd

df = pd.DataFrame({'num_legs': [2, 4, 8, 0],
                   'num_wings': [2, 0, 0, 0],
                   'num_specimen_seen': [10, 2, 1, 8]},
                  index=['falcon', 'dog', 'spider', 'fish'])

st.title('A Simple Streamlit Web App First App')
name = st.text_input('Enter your name', '')
st.write(f'Hello {name}!')
x = st.slider('Select an integer x', 0, 10, 1)
y = st.slider('Select an integer y', 0, 10, 1)
#df = pd.DataFrame({'x': [x], 'y': [y] , 'x + y': [x + y]}, index = ['addition row'])
st.write(df)
