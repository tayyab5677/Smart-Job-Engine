from App.parser import load_candidates,load_jobs
def test_load_candiates():
    candidates=load_candidates("data/candidates.json")
    assert len(candidates)==5
    assert candidates[0].name=="Ali"
def test_load_jobs():
    jobs=load_jobs("data/jobs.json")
    assert len(jobs)==3
    assert jobs[0].title=="Backend Developer"