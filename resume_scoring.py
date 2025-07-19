# resume_scoring.py
import PyPDF2
from fpdf import FPDF


def extract_text_from_pdf(uploaded_file):
    pdf_reader = PyPDF2.PdfReader(uploaded_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text


def get_keywords_for_role():
    return {
        "Machine Learning Engineer": ["machine learning", "deep learning", "tensorflow", "pytorch", "sklearn", "nlp", "model", "dataset"],
        "Data Scientist": ["python", "statistics", "machine learning", "data analysis", "modeling", "eda", "scikit-learn", "pandas"],
        "Data Analyst": ["sql", "excel", "power bi", "tableau", "data visualization", "dashboards", "statistics", "google sheets"],
        "Frontend Developer": ["html", "css", "javascript", "react", "next.js", "tailwind", "ui", "responsive"],
        "Backend Developer": ["node.js", "express", "django", "flask", "api", "rest", "authentication", "database", "mongodb", "postgres"],
        "Full Stack Developer": ["frontend", "backend", "react", "node.js", "express", "mongo", "rest api", "full stack", "typescript"],
        "DevOps Engineer": ["docker", "kubernetes", "ci/cd", "jenkins", "terraform", "linux", "bash", "ansible"],
        "Cloud Engineer": ["aws", "gcp", "azure", "cloudformation", "s3", "lambda", "iam", "cloud architecture"],
        "AI Researcher": ["transformers", "research paper", "huggingface", "bert", "gpt", "theory", "paperswithcode"],
        "Mobile App Developer": ["flutter", "react native", "android", "ios", "dart", "mobile ui", "cross-platform", "firebase"]
    }


def score_resume(text, selected_role):
    score = 0

    sections = ["education", "experience", "projects", "skills", "contact", "summary", "certification"]
    found_sections = sum(1 for section in sections if section in text.lower())
    score += found_sections * 10

    word_count = len(text.split())
    if word_count > 200:
        score += 10
    elif word_count < 100:
        score -= 10

    all_keywords = get_keywords_for_role()
    role_keywords = all_keywords.get(selected_role, [])
    matched = [kw for kw in role_keywords if kw.lower() in text.lower()]
    missing = list(set(role_keywords) - set(matched))

    score += len(matched) * 3
    score = min(score, 100)

    return score, matched, missing


def highlight_keywords(text, keywords):
    for kw in keywords:
        text = text.replace(kw, f"**🟩{kw}**")
        text = text.replace(kw.title(), f"**🟩{kw.title()}**")
    return text


def generate_pdf_report(score, matched, missing, role):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, "Resume Quality Report", ln=True, align="C")
    pdf.set_font("Arial", size=12)
    pdf.ln(10)

    pdf.cell(0, 10, f"Role: {role}", ln=True)
    pdf.cell(0, 10, f"Score: {score}/100", ln=True)
    pdf.ln(5)

    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 10, "Matched Keywords:", ln=True)
    pdf.set_font("Arial", size=12)
    for kw in matched:
        pdf.cell(0, 10, f"- {kw}", ln=True)

    pdf.ln(5)
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 10, "Missing Keywords (Tips):", ln=True)
    pdf.set_font("Arial", size=12)
    for kw in missing:
        pdf.cell(0, 10, f"- {kw}", ln=True)

    return pdf.output(dest='S').encode('latin1')
