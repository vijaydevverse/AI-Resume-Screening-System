import streamlit as st
from resume_parser import extract_text
from ats_engine import calculate_similarity
from keyword_matcher import extract_missing_skills
from feedback_engine import generate_feedback

st.set_page_config(page_title="AI Resume Checker", layout="wide")

st.title("📊 Enhancv-like AI Resume Checker")

resume_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])
job_desc = st.text_area("Paste Job Description")

if st.button("Analyze Resume"):

    if resume_file and job_desc:

        resume_text = extract_text(resume_file)

        score = calculate_similarity(resume_text, job_desc)

        missing_skills = extract_missing_skills(resume_text)

        feedback = generate_feedback(missing_skills)

        st.subheader("📊 ATS Score")
        st.metric("Match %", f"{score}%")

        st.subheader("⚠ Missing Skills")
        st.write(missing_skills)

        st.subheader("💡 Feedback")
        st.write(feedback)

        if score > 75:
            st.success("Strong Match ✅")
        elif score > 50:
            st.warning("Moderate Match ⚠️")
        else:
            st.error("Weak Match ❌")

    else:
        st.error("Upload resume and job description")