import asyncio 
from App.models import Canadidate,Job
from App.matching import match_candidate
async def process_match(candidate:Canadidate,job:Job)->dict:
    await asyncio.sleep(0.1)
    result=match_candidate(candidate,job)
    return result
async def process_all_matches(candidates:list[Canadidate],jobs:list[Job],)->list[dict]:
    tasks=[]
    for candidate in candidates:
        for job in jobs:
            task=process_match(candidate,job)
            task.append(task)
    results=await asyncio.gather(*task)
    return results
