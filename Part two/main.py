import streamlit as st
st.title("Web Application")
st.header("My First Header")
st.text("Good Morning Hello")
st.markdown("# Hello") #h1
st.markdown("## Hello") #h2
st.markdown("### Hello") #h3
st.markdown("**Hello**") #Used 2 stars to make it bold
st.markdown("*Hello all, good morning*") #Used 1 star to make it italic

st.markdown("<h1 style='text-align: center;'>This is Header 1 </h1>", unsafe_allow_html=True)
st.markdown("<p style='color: red;'> This is red text</p>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; color: red'>Centered and Colored Heading </h1>", unsafe_allow_html=True)

st.text("Writing")

st.info("This is for your information")
st.warning("Check before you upload")
st.error("Division by zero")
st.success("Great")

ch = st.radio("Pick a color", ["Black", "White", "Red", "Green"]) #Can give indexing to it.
st.write("You choosed", ch)

hobby = st.multiselect("Hobbies:", ["Dancing", "Reading", "Swimming", "Coding"])

for h in hobby:
    st.write("Your hobby is", h)

x = st.button("Click me")
if x:
    st.write("You click me")
if(st.button("About")):
    st.text("Welcome to about tab")

name = st.text_input("Enter your name")
b = st.button("Submit")
if b:
    st.write("Hello", name)
    # result = name
    # st.success(result)

agree = st.checkbox("I agree")

if agree:
    st.write("You agreed!")
else:
    st.write("You don't agree.")