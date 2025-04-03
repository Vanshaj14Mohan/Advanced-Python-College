import streamlit as st

form = st.form("my_form")

name = form.text_input("Enter your name")
age = form.number_input("Enter your age", min_value=0, max_value=100)
submitted = form.form_submit_button("Submit")

if submitted:
    st.write(f"Hello, {name} You are {age} old")