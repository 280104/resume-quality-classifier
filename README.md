# 🚀 Resume Quality Classifier By ASTROVEX

This app  is a powerful yet simple machine learning-based **Resume Quality Classifier** designed to help job seekers evaluate how well their resumes match specific tech roles. It analyzes the resume structure, content quality, and the presence of role-specific keywords to generate an overall **Resume Score** along with improvement tips.

---

## 🔍 What Does Resume Quality Classifier?

- 📄 **Resume Text Extraction:** Reads and processes uploaded PDF resumes.
- 🎯 **Role-Based Keyword Matching:** Compares resume content against predefined keyword sets for selected job roles.
- ✅ **Resume Scoring:** Scores your resume based on structure, keyword presence, and content length.
- 💡 **Improvement Tips:** Shows missing keywords to help users improve their resumes.
- 📥 **PDF Report Download:** Generates a clean, professional report summarizing the results.
- ✨ **Clean UI:** Powered by [Streamlit], styled to be intuitive, responsive, and easy to use.

---

## 🧠 Supported Job Roles
- Machine Learning Engineer  
- Data Scientist  
- Data Analyst  
- Frontend Developer  
- Backend Developer  
- Full Stack Developer  
- DevOps Engineer  
- Cloud Engineer  
- AI Researcher  
- Mobile App Developer  

---

## ⚙️ How It Works

1. Choose your desired role from the dropdown.
2. Upload your resume (PDF only).
3. ASTROVEX analyzes your resume and returns:
   - A score out of 100.
   - Matched keywords.
   - Missing keywords to improve.
4. Download a full report as PDF.

---

## 📦 Built With

- 🐍 Python
- 📘 Streamlit
- 📄 PyPDF2
- 🖨️ fpdf
- 💡 Custom logic for role-based scoring

---

## 🌐 Live Demo

Coming soon... (Once deployed via [Streamlit Cloud](https://streamlit.io/cloud))

---

## 📥 How to Run Locally

```bash
git clone https://github.com/your-username/astrovex-resume-classifier.git
cd astrovex-resume-classifier
pip install -r requirements.txt
streamlit run app.py
