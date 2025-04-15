# from fastapi import FastAPI
# from pydantic import BaseModel
# from gemini_utils import analyze_job_role

# app = FastAPI()

# class JobRequest(BaseModel):
#     job_role: str

# @app.get("/")
# def root():
#     return {"message": "Job Role AI Analyzer is running!"}

# @app.post("/analyze-job")
# def analyze(job: JobRequest):
#     result = analyze_job_role(job.job_role)
#     return result
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from constants import SERVER_URL, PORT, ENV
from apps.analyzer.route import router as analyzer_router  # 🔁 change this if your folder/module is named differently

@asynccontextmanager
async def lifespan(app: FastAPI):
    yield  # No setup/teardown for now

# Create FastAPI app with optional lifespan
app = FastAPI(lifespan=lifespan)

# Enable CORS for all origins (you can restrict this in production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Health check endpoint
@app.get("/")
async def root():
    return {"message": "Job Role AI Analyzer API is running 🎯"}

# Register routers
app.include_router(analyzer_router, prefix="/analyze-job", tags=["job-analysis"])

# Start server
if __name__ == "__main__":
    uvicorn.run("main:app", host=SERVER_URL, port=int(PORT), reload=(ENV == "dev"))
