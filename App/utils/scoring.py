def calculate_skill_score(
        candidate_skills:list[str],
        required_skills:list[str],
)->float:
    if not required_skills:
        return 0.0
    candidate_skills_lower={
        skill.strip.lower()
        for skill in candidate_skills
    }
    matched=0
    for skill in required_skills:
        if skill.strip().lower in candidate_skills_lower:
            matched+=1
    return (matched/len(required_skills)*100)
def calcualte_experience_score(candidate_experience:int,minimum_experience:int,)->float:
    if candidate_experience<0:
        raise ValueError("Candidate experience cannot be negative: ")
    if minimum_experience<0:
        raise ValueError("Minimum experience cannot be negative.")
    if minimum_experience==0:
        return 100.0
    if candidate_experience>=minimum_experience:
        return 100.0
    return (candidate_experience/minimum_experience)*100
def calcualte_final_score(skill_score:float,experiene_score:float,)->float:
    SKILL_WEIGHT=0.70
    EXPERIENCE_WEIGHT=0.30
    return (
        skill_score * SKILL_WEIGHT+experiene_score*EXPERIENCE_WEIGHT
    )
