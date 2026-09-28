from dataclasses import dataclass


@dataclass
class Candidate:
    id: int
    name: str
    skills: list[str]
    experience: int
    education: str


@dataclass
class Job:
    id: int
    title: str
    required_skills: list[str]
    minimum_experience: int
    location: str