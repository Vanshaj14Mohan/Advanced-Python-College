import streamlit as st

st.title("Streamlit form")

st.write("Fill form and click submit")

with st.form("user_form"):
    name = st.text_input("Name:")
    email = st.text_input("Email:")
    age = st.number_input("Age:", min_value=18, max_value=100)
    feedback = st.text_area("Your Feedback")

    submitted = st.form_submit_button("Submit")

if submitted:
    st.success("Form Submitted Successfully")
    st.write(f"**Name:** {name}")
    st.write(f"**Email:** {email}")
    st.write(f"**Age:** {age}")
    st.write(f"**Feedback:** {feedback}")


