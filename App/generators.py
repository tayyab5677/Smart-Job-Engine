from App.models import Candidate, Job


def candidate_generator(candidates: list[Candidate]):
    for candidate in candidates:
        yield candidate


def job_generator(jobs: list[Job]):
    for job in jobs:
        yield job


def experienced_candidates(
    candidates,
    minimum_experience: int
):
    for candidate in candidates:
        if candidate.experience >= minimum_experience:
            yield candidate


def skilled_candidates(
    candidates,
    required_skill: str
):
    for candidate in candidates:
        if required_skill.lower() in [
            skill.lower()
            for skill in candidate.skills
        ]:
            yield candidate