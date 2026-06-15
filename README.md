# 📊 AI Resume Screening & Job Matching System

An AI-powered Streamlit web application that analyzes resumes and compares them with job descriptions to generate a **match score**, extract skills, and provide hiring insights.

---

## 🚀 Features

* 📄 Upload resume (PDF format)
* 🧠 Extract text using NLP (spaCy)
* 📊 Compare resume with job description
* 🎯 Generate match score (0–100%)
* ⚡ Classify match level (Strong / Moderate / Weak)
* 📌 Display resume preview

---

## 🧱 Project Structure

```
AI-Resume-Screening-System/
│
├── app.py                  # Streamlit UI (main entry)
├── ats_engine.py          # ATS scoring logic
├── feedback_engine.py     # AI feedback generator
├── keyword_matcher.py     # Skill/keyword extraction
├── resume_parser.py       # PDF text extraction
├── skills.json            # Skill database
├── requirements.txt       # Dependencies
├── .gitignore             # Ignore venv/cache files
└── README.md              # Project documentation
```

---

## ⚙️ Installation Guide

### 1. Clone or Download the Project

git clone https://github.com/vijaydevverse/AI-Resume-Screening-System.git
cd AI-Resume-Screening-System

---

### 2. Create Virtual Environment (Recommended)

```
python -m venv venv
```

Activate it:

* Windows:

```
venv\Scripts\activate
```

* Mac/Linux:

```
source venv/bin/activate
```

---

### 3. Install Dependencies

```
pip install -r requirements.txt
```

---

### 4. Install spaCy Model

```
python -m spacy download en_core_web_sm
```

---

## ▶️ Run the Application

```
streamlit run app.py
```

Then open in browser:

```
http://localhost:8501
```

---

## 🧠 How It Works

1. User uploads a resume (PDF)
2. System extracts text using PyPDF2
3. Text is cleaned using NLP (spaCy)
4. Job description is entered manually
5. TF-IDF vectorization is applied
6. Cosine similarity calculates match score
7. Final ATS-style score is displayed

---

## 🛠️ Technologies Used

* Python 🐍
* Streamlit ⚡
* spaCy 🧠
* scikit-learn 📊
* PyPDF2 📄

---

## 📌 Future Improvements

* Skill extraction engine (Python, SQL, ML, etc.)
* Missing skill detection
* AI-powered feedback system
* Multi-resume ranking system
* PDF report generation
* Advanced ATS scoring system

---

## 👨‍💻 Author

**Vijay Krishnan P.M**

---

## 📜 License

This project is for educational and portfolio purposes.
