import streamlit as st
import os
from resume_parser import ResumeParser

st.set_page_config(page_title="Resume Parser", layout="centered")

st.title("📄 Resume Parser")
st.write("Upload your resume PDF to extract details")

uploaded_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])

if uploaded_file:
    save_path = os.path.join("uploads", uploaded_file.name)
    os.makedirs("uploads", exist_ok=True)

    with open(save_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    parser = ResumeParser(save_path)
    data = parser.parse()

    st.success("Resume Parsed Successfully!")

    st.subheader("Extracted Information")
    st.write("📧 Email:", data["email"])
    st.write("📱 Phone:", data["phone"])
    st.write("🧠 Skills:", ", ".join(data["skills"]))
    
    with st.expander("Show Raw Text"):
        st.text(data["raw_text"])
