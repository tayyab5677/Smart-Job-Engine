from App.models import Canadidate
from App.generators import (candidate_generator,experienced_candidates)
def test_candidate_generator():
    candidates=[
        Canadidate(id=1,name="Ali",skills=["Python"],experience=2,education="BSCS",),
        Canadidate(id=2,name="Sara",skills=["React"],experience=1,education="BSCS"),
    ]
    result=list(candidate_generator(candidates))
    assert len(result)==2
    def test_experienced_candidates():
        candidates=[
            Canadidate(id=1,name="Ali",skills=["Python"],experience=3,education="BSCS"),
            Canadidate(id=2,name="Sara",skills=["React"],experience=1,education="BSCS"),
        ]
        result=list(experienced_candidates(candidates,2))
        assert len(result)==1
        assert result[0].name=="Ali"