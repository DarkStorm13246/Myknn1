import streamlit as st
import pandas as pd

st.title("✖️Website Developing using Python✖️")
st.header("🍔Website Developing using Python🍿")

st.image('./img/1.jpg')
st.subheader("Thanawat Jibsamarnboon")

dt=pd.read_csv('./data/iris-3csv')
st.header()
st.write(dt.head(10))
