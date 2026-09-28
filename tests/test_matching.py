from App.models import Canadidate,Job
from App.matching import match_candidate
def test_match_candidate():
    candidate=Canadidate(id=1,name="Ali",skills=["Python","Django","Postgre SQL"],experience=2,education="BSCS")
    job=Job(id=1,title="Backend Developer",required_skills=[ "Python","Django","PostgreSQL", "Docker",],minimum_experience=2,location="Remote")
    result=match_candidate(candidate,job)
    assert result["skill_score"]==75
    assert result["experience"]==100
    assert result["status"]=="Qualified"