
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("📕 Data Visualization Web App")

data = pd.read_csv("E:\Advanced Python\Part two\Cardata.xlsx")

st.subheader("5 rows of the dataset")
st.write(data.head(5))

st.subheader("📓 Data Summary")
st.write(data.describe())