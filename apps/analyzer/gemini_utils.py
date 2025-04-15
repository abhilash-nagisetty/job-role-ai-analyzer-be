import google.generativeai as genai
from dotenv import load_dotenv
import os
import json
import re

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash")

def analyze_job_role(job_role: str) -> dict:
    with open("job_prompt.txt", "r") as f:
        static_prompt = f.read()

    full_prompt = f"{static_prompt}\n\nJob Role: {job_role}"
    response = model.generate_content(full_prompt)
    raw_text = response.text.strip()

    # Clean ```json blocks if present
    cleaned = re.sub(r"```json|```", "", raw_text).strip()

    try:
        return json.loads(cleaned)
    except json.JSONDecodeError as e:
        return {
            "error": "Failed to parse Gemini response",
            "details": str(e),
            "raw_response": raw_text
        }
