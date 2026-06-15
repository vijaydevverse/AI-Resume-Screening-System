import json

def load_skills():
    with open("data/skills.json", "r") as f:
        return json.load(f)

def extract_missing_skills(resume_text):
    skills = load_skills()
    resume_text = resume_text.lower()

    missing = [skill for skill in skills if skill.lower() not in resume_text]

    return missing