import streamlit as st

st.title("Web Application")
st.text("Good Morning Hello")
st.markdown("# Hello")   
st.markdown("**Hello**")  
st.markdown("*Hello all, good morning*") 

st.markdown("<h1 style='text-align: center;'>This is Header 1 </h1>", unsafe_allow_html=True)
st.markdown("<p style='color: blue;'> This is blue text</p>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; color: red'>Centered and Colored Heading </h1>", unsafe_allow_html=True)

st.text("Writing")

st.info("This is for your information")
st.warning("Check before you upload")
st.error("Division by zero")
st.success("Great")

ch = st.radio("Pick a color", ["Black", "White", "Red", "Green"]) 
st.write("You choosed", ch)

agree = st.checkbox("I agree")
if agree:
    st.write("You agreed!")
else:
    st.write("You don't agree.")

# Additional Features:
st.subheader("User Input Section")

name = st.text_input("Enter your name")
age = st.number_input("Enter your age", min_value=0, max_value=120, step=1)
email = st.text_input("Enter your email")

subscribe = st.checkbox("Subscribe to our channel")
terms = st.checkbox("Accept Terms and Conditions")

if subscribe:
    st.write("You are subscribed to our channel")

if terms:
    st.write("You have accepted the terms and conditions.")

option = st.selectbox("Select your country", ["India", "USA", "UK", "Canada", "Australia"])
st.write("You selected:", option)


feedback = st.text_area("Enter your feedback", height=80)
if feedback:
    st.write("Thanks for your feedback!")

st.button("Submit")