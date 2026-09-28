import pytest
from App.models import Canadidate,Job
from App.aysnc_processor import process_match
@pytest.mark.asyncio
async def test_process_match():
    candidate=Canadidate(id=1,name="Ali",skills=["python","Django"],experience=2,education="BSCS")
    job=Job(id=1,title="Backend Developer",required_skills=["Python","Django"],minimum_experience=2,location="Remote")
    result=await process_match(candidate,job)
    assert result["candidate"]=="Ali"
    assert result["job"]=="Backend Developer"
    assert result["final_score"]==100