import asyncio

from App.parser import (
    load_candidates,
    load_jobs,
)

from App.validators import (
    validate_candidate,
    validate_job,
)

from App.aysnc_processor import (
    process_all_matches,
)

from App.reports import create_report

from App.utils.file_utils import (
    save_file,
)


async def main():

    print("=" * 55)
    print("          SMART JOB MATCHING ENGINE")
    print("=" * 55)

    print("\nLoading candidates...")

    candidates = load_candidates(
        "data/candidates.json"
    )

    print(
        f"✓ {len(candidates)} candidates loaded"
    )

    print("\nLoading jobs...")

    jobs = load_jobs(
        "data/jobs.json"
    )

    print(
        f"✓ {len(jobs)} jobs loaded"
    )

    print("\nValidating data...")

    for candidate in candidates:
        validate_candidate(candidate)

    for job in jobs:
        validate_job(job)

    print("✓ All data is valid")

    print("\nProcessing matches...")

    results = await process_all_matches(
        candidates,
        jobs,
    )

    print(
        f"✓ {len(results)} matches processed"
    )

    report = create_report(results)

    print("\n")
    print(report)

    save_file(
        "matching_report.txt",
        report,
    )

    print("\n✓ Report saved to matching_report.txt")


if __name__ == "__main__":
    asyncio.run(main())