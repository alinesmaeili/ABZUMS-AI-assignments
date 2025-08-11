# Psychology RAG Symptom Checker (MVP)

Stages:

1) Extract PDF pages

```
python3 stages/01_extract_text.py
```

- Expects PDF at `/workspace/data/raw/textbook.pdf`.

2) Clean and chunk

```
python3 stages/02_clean_and_chunk.py
```

- Outputs `/workspace/data/chunks/chunks.jsonl`.

3) Embed and index (OpenAI embeddings + Chroma)

Set your key first:

```
export OPENAI_API_KEY=sk-...
```

Then run:

```
python3 stages/03_embed_and_index.py
```

4) Retrieve test

```
python3 stages/04_retrieve.py
```

5) Answer (structured JSON)

```
python3 stages/05_answer.py
```

API (FastAPI):

```
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

POST /api/check example body:

```
{
  "age": 28,
  "duration_weeks": 6,
  "symptoms": ["low mood", "anhedonia", "fatigue", "sleep disturbance"],
  "impacts": ["work impairment"],
  "risk_factors": ["family history depression"],
  "substance_use": "none",
  "safety": {"suicidal_ideation": false, "homicidal_ideation": false, "psychosis": false},
  "free_text": "Feeling down most days, nothing is enjoyable."
}
```

Notes:
- This is educational only; not a medical diagnosis.
- The system prompt lives in `prompts/psych_guardrail.txt`.
- Vector store is persisted in `/workspace/data/chroma`. 
