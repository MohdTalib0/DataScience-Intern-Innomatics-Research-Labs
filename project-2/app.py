import streamlit as st
import pandas as pd
st.title("Welcome to CodeSpaze")
st.header("My Self Mohd Talib")
st.subheader("I am a Data Scientist:sunglasses:")
CODE = '''print("hello world")'''
st.code(CODE,language= "python")
st.latex(st.latex(r'''
...     a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
...     \sum_{k=0}^{n-1} ar^k =
...     a \left(\frac{1-r^{n}}{1-r}\right)
...     '''))