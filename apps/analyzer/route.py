from fastapi import APIRouter
from pydantic import BaseModel
from apps.analyzer.gemini_utils import analyze_job_role

router = APIRouter()

class JobRequest(BaseModel):
    job_role: str

@router.post("/")
async def analyze(job: JobRequest):
    result = analyze_job_role(job.job_role)
    return result
