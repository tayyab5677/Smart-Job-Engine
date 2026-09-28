from App.models import Canadidate,Job
from App.utils.scoring import(
    calculate_skill_score,calcualte_experience_score,calcualte_final_score,
)
def match_candidate(canditate:Canadidate,job:Job,)->dict:
    skill_score=calculate_skill_score(canditate.skills,job.required_skills,)
    experience_socre=calcualte_experience_score(canditate.experience,job.minimum_experience)
    final_score=calcualte_final_score(skill_score,experience_socre)
    candidate_skills={
        skill.lower()
        for skill in canditate.skills
    }
    matched_skills=[]
    missing_skills=[]
    for skill in job.required_skills:
        if skill.lower() in candidate_skills:
            matched_skills.append(skill)
        else:
            missing_skills.append(skill)
        if skill_score>=75 and canditate.experience>=job.minimum_experience:
            status="Qualified"
        elif skill_score>0:
           status="Partially Qualified"
        else:
            status="Not Qualified"
    return{
        "candidate":canditate.name,
        "job":job.title,
        "skill_score":round(skill_score,2),
        "final_score":round(final_score,2),
        "matched_skills":matched_skills,
        "missing_skills":missing_skills,
        "status":status,
    }