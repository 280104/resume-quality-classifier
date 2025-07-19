import streamlit as st
from resume_scoring import (
    extract_text_from_pdf,
    score_resume,
    get_keywords_for_role,
    highlight_keywords,
    generate_pdf_report
)

st.set_page_config(page_title="Resume Quality Classifier", layout="centered")

st.markdown("""
    <h1 style='text-align: center; font-size: 40px;'>RESUME QUALITY CLASSIFIER</h1>
""", unsafe_allow_html=True)

roles = list(get_keywords_for_role().keys())
selected_role = st.selectbox("Select the target job role:", roles)

uploaded_file = st.file_uploader("Upload your resume (PDF only)", type=["pdf"])

if uploaded_file:
    resume_text = extract_text_from_pdf(uploaded_file)
    score, matched_keywords, missing_keywords = score_resume(resume_text, selected_role)
    highlighted_text = highlight_keywords(resume_text, matched_keywords)

    st.markdown("---")
    st.markdown("### 🎯 Resume Score")

    score_color = "#38bdf8" if score >= 70 else "#facc15" if score >= 50 else "#f87171"

    st.markdown(f"""
    <div style='
        background-color:#111827;
        padding: 30px;
        border-radius: 12px;
        text-align: center;
        margin-bottom: 20px;
    '>
        <span style='
            font-size: 36px;
            font-weight: bold;
            color: {score_color};
        '>{score}/100</span>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### ✅ Matched Keywords")
    for kw in matched_keywords:
        st.markdown(f"<span style='display: inline-block; background-color: #bbf7d0; color: #065f46; padding: 5px 10px; border-radius: 10px; margin: 4px;'>{kw}</span>", unsafe_allow_html=True)

    st.markdown("### 💡 Tips — Missing Keywords")
    if missing_keywords:
        for kw in missing_keywords:
            st.markdown(f"<span style='display: inline-block; background-color: #fee2e2; color: #7f1d1d; padding: 5px 10px; border-radius: 10px; margin: 4px;'>{kw}</span>", unsafe_allow_html=True)
    else:
        st.success("Great! All important keywords for this role are covered.")

    st.markdown("### 📄 Download PDF Report")
    pdf_bytes = generate_pdf_report(score, matched_keywords, missing_keywords, selected_role)
    st.download_button("Download Resume Report", data=pdf_bytes, file_name="resume_scorecard.pdf", mime="application/pdf")

st.markdown("""
    <div class="footer" style="text-align: center; padding: 20px; margin-top: 40px;">
        <p style="font-size: 20px; color: #ccc;">
            🚀 Empowered by <strong style="color: #7dd3fc; font-weight: bold;">ASTROVEX</strong>
        </p>
    </div>
""", unsafe_allow_html=True)
