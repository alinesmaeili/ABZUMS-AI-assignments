import os
import json
from typing import List, Dict, Optional

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from openai import OpenAI

from src.retrieve import hybrid_retrieve

PROMPT_PATH = os.environ.get("PROMPT_PATH", "/workspace/prompts/psych_guardrail.txt")
MODEL = os.environ.get("MODEL", "gpt-4o-mini")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

app = FastAPI()


class SafetyFlags(BaseModel):
    suicidal_ideation: Optional[bool] = False
    homicidal_ideation: Optional[bool] = False
    psychosis: Optional[bool] = False


class SymptomRequest(BaseModel):
    age: Optional[int] = None
    duration_weeks: Optional[int] = None
    symptoms: List[str] = Field(default_factory=list)
    impacts: List[str] = Field(default_factory=list)
    risk_factors: List[str] = Field(default_factory=list)
    substance_use: Optional[str] = None
    safety: Optional[SafetyFlags] = SafetyFlags()
    free_text: Optional[str] = ""


def load_system_prompt(path: str) -> str:
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


@app.get("/health")
async def health():
    return {"status": "ok"}


@app.post("/api/check")
async def check(payload: SymptomRequest):
    if not OPENAI_API_KEY:
        raise HTTPException(status_code=500, detail="OPENAI_API_KEY not set")
    client = OpenAI(api_key=OPENAI_API_KEY)
    system_prompt = load_system_prompt(PROMPT_PATH)

    user_report_parts: List[str] = []
    if payload.age is not None:
        user_report_parts.append(f"Age: {payload.age}")
    if payload.duration_weeks is not None:
        user_report_parts.append(f"Duration (weeks): {payload.duration_weeks}")
    if payload.symptoms:
        user_report_parts.append("Symptoms: " + ", ".join(payload.symptoms))
    if payload.impacts:
        user_report_parts.append("Impacts: " + ", ".join(payload.impacts))
    if payload.risk_factors:
        user_report_parts.append("Risk factors: " + ", ".join(payload.risk_factors))
    if payload.substance_use:
        user_report_parts.append(f"Substance use: {payload.substance_use}")
    if payload.safety:
        flags = []
        if payload.safety.suicidal_ideation:
            flags.append("suicidal ideation")
        if payload.safety.homicidal_ideation:
            flags.append("homicidal ideation")
        if payload.safety.psychosis:
            flags.append("psychosis")
        if flags:
            user_report_parts.append("Safety flags: " + ", ".join(flags))
    if payload.free_text:
        user_report_parts.append("Free text: " + payload.free_text)

    user_report = " | ".join(user_report_parts)

    retrieved = hybrid_retrieve(user_report, k=8)
    context_lines = []
    for r in retrieved:
        page = r.get("metadata", {}).get("page_number")
        context_lines.append(f"[Page {page}] {r['text']}")
    context = "\n\n".join(context_lines)

    schema = {
        "triage_level": "emergency | urgent | routine | self-care",
        "red_flags": [{"flag": "string", "evidence": "string"}],
        "likely_conditions": [
            {
                "name": "string",
                "confidence": 0.0,
                "rationale": "string",
                "differentials": ["string"],
                "citations": [{"source": "Textbook", "section": "", "pages": [0]}],
            }
        ],
        "recommended_actions": {
            "self_care": ["string"],
            "professional": ["string"],
            "crisis": "string",
        },
        "limitations": "string",
    }

    user_prompt = (
        f"User symptoms/report:\n{user_report}\n\nRetrieved textbook excerpts (cite pages):\n{context}\n\n"
        f"Output strict JSON exactly in this schema (keys and types):\n{json.dumps(schema)}"
    )

    resp = client.chat.completions.create(
        model=MODEL,
        temperature=0.2,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        response_format={"type": "json_object"},
    )

    content = resp.choices[0].message.content
    try:
        data = json.loads(content)
    except Exception:
        data = {"raw": content}

    return data