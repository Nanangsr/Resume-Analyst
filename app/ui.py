import streamlit as st
from typing import Tuple, Union, Dict, List
from utils.resume_parser import parse_resume
from utils.jd_parser import parse_jd
import os

def render_ui() -> Tuple[str, Union[Dict, List]]:
    """Render Streamlit UI and collect inputs"""
    st.sidebar.header("Use Cases")
    use_case = st.sidebar.radio(
        "Select Use Case",
        ["Candidate Search by Job Description", 
         "Candidate Profiling / Resume QA",
         "Compare Multiple Candidates"]
    )
    
    inputs = {}
    
    if use_case == "Candidate Search by Job Description":
        st.header("🔍 Candidate Search by Job Description")
        jd_file = st.file_uploader("Upload Job Description (PDF/DOCX)", type=["pdf", "docx"])
        if jd_file:
            jd_text = parse_jd(jd_file)
            inputs = {"jd_text": jd_text}
            
    elif use_case == "Candidate Profiling / Resume QA":
        st.header("📝 Candidate Profiling / Resume QA")
        resume_file = st.file_uploader("Upload Resume (PDF/DOCX)", type=["pdf", "docx"])
        if resume_file:
            resume_text = parse_resume(resume_file)
            inputs = {"resume_text": resume_text}
            
    elif use_case == "Compare Multiple Candidates":
        st.header("📊 Compare Multiple Candidates")
        resume_files = st.file_uploader(
            "Upload Resumes (PDF/DOCX)", 
            type=["pdf", "docx"],
            accept_multiple_files=True
        )
        if resume_files and len(resume_files) >= 2:
            resume_texts = [parse_resume(file) for file in resume_files]
            inputs = {"resume_texts": resume_texts}
            
    return use_case, inputs if inputs else None