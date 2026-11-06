import streamlit as st

st.set_page_config(
    page_title="Sanika Naik | Data Scientist",
    page_icon="🤖",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        color: #4F7BD0;
        text-align: center;
    }
    .sub-header {
        font-size: 1.2rem;
        color: inherit;
        text-align: center;
        margin-bottom: 2rem;
    }
    .section-header {
        font-size: 1.8rem;
        font-weight: bold;
        color: #4F7BD0;
        border-bottom: 3px solid #4F7BD0;
        padding-bottom: 0.5rem;
        margin-top: 2rem;
    }
    .project-card {
        background-color: #e8f0fe;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 5px solid #1F3864;
        margin-bottom: 1rem;
        color: #1a1a1a;
    }
    .project-card h3 {
        color: #1F3864;
    }
    .project-card p {
        color: #1a1a1a;
    }
    .skill-badge {
        background-color: #1F3864;
        color: white;
        padding: 0.3rem 0.8rem;
        border-radius: 20px;
        margin: 0.2rem;
        display: inline-block;
        font-size: 0.9rem;
    }
    .contact-bar {
        background-color: #e8f0fe;
        padding: 1rem;
        border-radius: 10px;
        text-align: center;
        color: #1a1a1a;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown('<p class="main-header">Sanika Prasad Naik</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">MSc Data Science | Machine Learning | Generative AI | RAG | Agentic AI | Python</p>', unsafe_allow_html=True)

# Contact links
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown("📧 naiksanika70@gmail.com")
with col2:
    st.markdown("💼 [LinkedIn](https://linkedin.com/in/sanikanaik1308)")
with col3:
    st.markdown("🐱 [GitHub](https://github.com/sanikanaik456)")
with col4:
    st.markdown("📍 Birmingham, UK")

st.divider()

# CV download
try:
    with open("Sanika_CV.pdf", "rb") as cv_file:
        st.download_button(
            label="📄 Download my CV (PDF)",
            data=cv_file,
            file_name="Sanika_Naik_CV.pdf",
            mime="application/pdf",
        )
except FileNotFoundError:
    st.caption("CV download coming soon.")

st.divider()

# About Me
st.markdown('<p class="section-header">👤 About Me</p>', unsafe_allow_html=True)
st.write("""
I am a recent MSc Data Science graduate from the University of Birmingham with hands-on experience 
building machine learning models, generative AI applications, and RAG pipelines. My dissertation 
focused on Explainable Deep Learning for Credit Risk Prediction, reaching a test AUC of 0.856 on 
150,000 financial records, and detecting and mitigating age bias.

I am passionate about applying AI and data science to solve real-world problems responsibly, 
with a particular interest in explainable AI, agentic systems, and making data accessible to everyone.

✅ Graduate Route visa — full right to work in the UK for 2 years from December 2026, no sponsorship required.
""")

st.divider()

# Projects
st.markdown('<p class="section-header">🛠️ Projects</p>', unsafe_allow_html=True)

# Project 1 - DocuChat
st.markdown("""
<div class="project-card">
<h3>🤖 DocuChat — RAG-Powered PDF Question Answering</h3>
<p>Upload any PDF and ask questions in natural language. Answers are grounded in real document 
content using a RAG pipeline, which reduces unsupported answers.</p>
<p><b>Tech:</b> Python, Streamlit, Google Gemini API, PyPDF2</p>
<p><b>Key feature:</b> Grounding LLM outputs in retrieved context reduces unsupported answers</p>
</div>
""", unsafe_allow_html=True)
st.markdown("🔗 [View on GitHub](https://github.com/sanikanaik456/docuchat)")

st.markdown("---")

# Project 2 - Dissertation
st.markdown("""
<div class="project-card">
<h3>💳 Explainable Deep Learning for Credit Risk Prediction</h3>
<p>MSc Dissertation — Built PyTorch neural networks on 150,000 credit records (test AUC 0.856 for default), 
applied SHAP and Integrated Gradients for explainability, found that borrowers under 35 were wrongly 
flagged as high risk 44.9% of the time against 11.6% for those 55 and over, reduced the gap with 
group-specific thresholds (false-positive rate equalised at 15%), and built a six-tab Streamlit 
Decision Support System.</p>
<p><b>Tech:</b> Python, PyTorch, SHAP, Captum, Streamlit, Power BI</p>
<p><b>Key finding:</b> SHAP and Integrated Gradients disagree on feature importance for the same model.</p>
</div>
""", unsafe_allow_html=True)
st.markdown("🔗 University of Birmingham GitLab (available on request)")

st.markdown("---")

# Project 3 - AI Agent
st.markdown("""
<div class="project-card">
<h3>🤖 AI Data Analysis Agent</h3>
<p>An agentic application that profiles datasets (150,000+ rows), runs automated EDA, 
produces visualisations, and answers natural-language business questions grounded in 
real computed results.</p>
<p><b>Tech:</b> Python, Streamlit, Google Gemini API</p>
<p><b>Key feature:</b> LLM outputs grounded in real computed context — not raw data</p>
</div>
""", unsafe_allow_html=True)
st.markdown("🔗 [View on GitHub](https://github.com/sanikanaik456)")

st.markdown("---")

# Project - CV Analyzer
st.markdown("""
<div class="project-card">
<h3>📄 CV Analyzer</h3>
<p>Upload a CV (PDF) and paste a job description. The app asks Google Gemini to compare them and 
returns a match score, matching and missing skills, strengths and suggestions. It retries 
automatically when the model is busy.</p>
<p><b>Tech:</b> Python, Streamlit, PyPDF2, Google Gemini API</p>
<p><b>Note:</b> The score is an AI estimate, not an objective measure</p>
</div>
""", unsafe_allow_html=True)
st.markdown("🔗 [View on GitHub](https://github.com/sanikanaik456/cv-analyzer)")

st.markdown("---")

# Project - CV Analyzer API
st.markdown("""
<div class="project-card">
<h3>🧩 CV Analyzer API</h3>
<p>A REST API built with FastAPI. It takes CV text and a job description, asks Google Gemini to 
compare them, and returns a match score, matching and missing skills, strengths and suggestions 
as JSON. It validates input, retries with a fallback model when the service is busy, and returns 
clear error codes.</p>
<p><b>Tech:</b> Python, FastAPI, pytest, Docker, Google Gemini API</p>
<p><b>Testing:</b> 8 automated tests that replace the model with a fake one, so they need no API key</p>
<p><b>Note:</b> Built and run locally in Docker; not deployed to a cloud service</p>
</div>
""", unsafe_allow_html=True)
st.markdown("🔗 [View on GitHub](https://github.com/sanikanaik456/cv-analyzer-api)")

st.markdown("---")

# Project 4 - Churn
st.markdown("""
<div class="project-card">
<h3>📊 Customer Churn Prediction</h3>
<p>End-to-end classification pipeline to predict customer churn on 7,043 telecom records. 
Feature engineering, model selection and evaluation achieving ROC-AUC of 0.842, 
outperforming random forest baseline.</p>
<p><b>Tech:</b> Python, scikit-learn, Pandas, Matplotlib</p>
<p><b>Key insight:</b> Identified top churn drivers through feature importance analysis</p>
</div>
""", unsafe_allow_html=True)
st.markdown("🔗 [View on GitHub](https://github.com/sanikanaik456)")

st.markdown("---")

# Project 5 - Survey Paper
st.markdown("""
<div class="project-card">
<h3>📝 Agentic AI Systems — Survey Paper</h3>
<p>Comprehensive 28-page survey paper covering multi-agent architectures, LangChain and 
LangGraph orchestration frameworks, LLM evaluation methodologies, and responsible AI deployment.</p>
<p><b>Topics:</b> Multi-agent systems, Tool use, RAG, LLM evaluation, Responsible AI</p>
<p><b>Coverage:</b> 84 references spanning latest research in agentic AI</p>
</div>
""", unsafe_allow_html=True)
st.markdown("📄 Available on request")

st.divider()

# Skills
st.markdown('<p class="section-header">🔧 Skills</p>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("**Languages and Databases**")
    skills1 = ["Python", "SQL", "MySQL", "PostgreSQL"]
    for s in skills1:
        st.markdown(f'<span class="skill-badge">{s}</span>', unsafe_allow_html=True)

with col2:
    st.markdown("**ML and AI**")
    skills2 = ["Machine Learning", "Deep Learning", "GenAI", "RAG", "Agentic AI", "LLMs", "PyTorch", "scikit-learn", "SHAP", "NLP", "Prompt Engineering"]
    for s in skills2:
        st.markdown(f'<span class="skill-badge">{s}</span>', unsafe_allow_html=True)

with col3:
    st.markdown("**Tools**")
    skills3 = ["Streamlit", "Docker", "Git", "Power BI", "Tableau", "Jupyter", "Matplotlib", "Seaborn"]
    for s in skills3:
        st.markdown(f'<span class="skill-badge">{s}</span>', unsafe_allow_html=True)

st.divider()

# Experience
st.markdown('<p class="section-header">💼 Experience</p>', unsafe_allow_html=True)

st.markdown("""
**Data Analyst Intern** — Faceify Labs (Formir Technologies Pvt Ltd) | Jan 2026 – Jul 2026
- Analysed real-world datasets in Python and SQL to uncover behavioural trends
- Built Power BI dashboards for stakeholder decision-making
- Developed and containerised a classification model using Docker
- Identified and resolved data quality issues in analytical pipelines

**Data Analysis Project Assistant** — Private Client | 2023 – 2025
- Delivered 14 independent data analysis projects across diverse business domains
- Generated actionable insights from complex datasets for non-technical clients
""")

st.divider()

# Education
st.markdown('<p class="section-header">🎓 Education</p>', unsafe_allow_html=True)

st.markdown("""
**MSc Data Science** — University of Birmingham, UK | 2025 – 2026
- Dissertation: Explainable Deep Learning for Credit Risk Prediction
- Survey paper: Agentic AI Systems (28 pages, 84 references)
- Key modules: Advanced AI, SQL and Databases, Large Language Models, Python

**B.E. AI and Data Science** — Savitribai Phule Pune University (SPPU), India | 2021 – 2025
- First Class with Distinction
""")

st.divider()

# Certifications
st.markdown('<p class="section-header">🏆 Certifications and Achievements</p>', unsafe_allow_html=True)
st.markdown("""
- 🏅 HackerRank SQL Advanced Certification (2026)
- 🏅 Deloitte Data Analytics Job Simulation — Forage (2026)
- ♟️ National-level Chess Player — Maharashtra State Qualifier (2018)
""")

st.divider()

# Footer
st.markdown("""
<div style='text-align: center; color: #1a1a1a; margin-top: 2rem; padding: 1rem; background-color: #e8f0fe; border-radius: 10px;'>
    <p>📧 naiksanika70@gmail.com | 
    <a href='https://linkedin.com/in/sanikanaik1308'>LinkedIn</a> | 
    <a href='https://github.com/sanikanaik456'>GitHub</a></p>
    <p>🌟 Open to Data Scientist, ML Engineer and AI roles in the UK, Singapore and Dubai.</p>
    <p>✅ Graduate Route visa — no sponsorship required from December 2026</p>
</div>
""", unsafe_allow_html=True)
