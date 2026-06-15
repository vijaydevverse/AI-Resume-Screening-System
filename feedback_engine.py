def generate_feedback(missing_skills):
    if len(missing_skills) == 0:
        return "Excellent! Your resume matches most job requirements."

    feedback = "Improve your resume by adding:\n"

    for skill in missing_skills:
        feedback += f"- {skill}\n"

    return feedback