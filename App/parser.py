import json
from App.models import Candidate, Job


def load_candidates(filename: str) -> list[Candidate]:
    with open(filename, "r") as file:
        data = json.load(file)

    candidates = []

    for item in data:
        candidate = Candidate(
            id=item["id"],
            name=item["name"],
            skills=item["skills"],
            experience=item["experience"],
            education=item["education"],
        )

        candidates.append(candidate)

    return candidates


def load_jobs(filename: str) -> list[Job]:
    with open(filename, "r") as file:
        data = json.load(file)

    jobs = []

    for item in data:
        job = Job(
            id=item["id"],
            title=item["title"],
            required_skills=item["required_skills"],
            minimum_experience=item["minimum_experience"],
            location=item["location"],
        )

        jobs.append(job)

    return jobs