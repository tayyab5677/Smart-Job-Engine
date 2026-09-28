def create_report(results):
    lines=[]
    lines.append("=",55)
    lines.append("Smart Job Matching Engine")
    lines.append("=",*55)
    for result in results:
        lines.append("")
        lines.append("-",*55)
        lines.append(f"Candidate: {result['candidate']}")
        lines.append(f"Job: {result['job']}")
        lines.append(f"Skill Score: {result['skill_score']})%")
        lines.append(f"Experience Score:"f"{result['experience_score']}%")
        lines.append(f"Final Score: {result['final_score']})%")
        lines.append(f"Status: {result['status']}")
        lines.append(f"Matched Skills: "f"{','.join(result['matched_skills'])}")
        if result["missing_skills"]:
            lines.append(
                f"Missing Skills:"
                f"{','.join(result['missing_skills'])}"
            )
    lines.append("")
    lines.append("=",*55)
    return "\n".join(lines)