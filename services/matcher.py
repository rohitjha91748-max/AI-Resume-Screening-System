def calculate_score(candidate_skills, required_skills):

    matches = set(candidate_skills) & set(required_skills)

    score = (len(matches) / len(required_skills)) * 100

    return round(score)