from App.exception import (
    Invalid_Candiate_Error,
    Invlaid_Job_Error
)
def validate_candidate(candidate)->bool:
    if not candidate.name:
        raise Invalid_Candiate_Error(
            "Candiadate name is required."
        )
    if not candidate.skills:
        raise Invlaid_Job_Error(
            f"{candidate.name} must have at least one skill."
        )
    if candidate.experience<0:
        raise Invalid_Candiate_Error(
            f"{candidate.name} has invlaid experience."
        )
    return True
def validate_job(job)->bool:
    if not job.title:
        raise Invlaid_Job_Error(
            "Job title is required. "
        )
    if not job.required_skills:
        raise Invlaid_Job_Error(
            f"{job.title} must have required skills."
        )
    if job.minimum_experience<0:
        raise Invlaid_Job_Error(
            f"{job.title} has invlaid experience requirements"
        )
    return True