import os
import json
from typing import Dict, Iterable, List

from dotenv import load_dotenv
load_dotenv()

import chromadb
from chromadb.config import Settings
from tqdm import tqdm

from openai import OpenAI

CHUNKS_JSONL = os.environ.get("CHUNKS_JSONL", "/workspace/data/chunks/chunks.jsonl")
CHROMA_DIR = os.environ.get("CHROMA_DIR", "/workspace/data/chroma")
COLLECTION_NAME = os.environ.get("COLLECTION_NAME", "psych_textbook")
EMBED_MODEL = os.environ.get("EMBED_MODEL", "text-embedding-3-large")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    print("Warning: OPENAI_API_KEY not set. Set it in your environment or .env before running.")


def read_jsonl(path: str) -> Iterable[Dict]:
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                yield json.loads(line)


def get_or_create_collection(client: chromadb.Client, name: str):
    try:
        return client.get_collection(name)
    except Exception:
        return client.create_collection(name)


if __name__ == "__main__":
    os.makedirs(CHROMA_DIR, exist_ok=True)
    chroma_client = chromadb.PersistentClient(path=CHROMA_DIR, settings=Settings(anonymized_telemetry=False))
    collection = get_or_create_collection(chroma_client, COLLECTION_NAME)

    client = OpenAI(api_key=OPENAI_API_KEY)

    ids: List[str] = []
    metadatas: List[Dict] = []
    documents: List[str] = []

    for rec in tqdm(read_jsonl(CHUNKS_JSONL), desc="Loading chunks"):
        ids.append(rec["id"])
        metadatas.append({
            "page_number": rec.get("page_number"),
            "chunk_index": rec.get("chunk_index"),
        })
        documents.append(rec["text"])

    print(f"Embedding {len(documents)} chunks with {EMBED_MODEL}...")
    # Batch to avoid large payloads
    batch_size = 128
    for start in tqdm(range(0, len(documents), batch_size), desc="Embedding"):
        batch_docs = documents[start:start + batch_size]
        batch_ids = ids[start:start + batch_size]
        batch_metas = metadatas[start:start + batch_size]
        resp = client.embeddings.create(model=EMBED_MODEL, input=batch_docs)
        vectors = [d.embedding for d in resp.data]
        collection.add(ids=batch_ids, embeddings=vectors, metadatas=batch_metas, documents=batch_docs)

    print(f"Chroma collection '{COLLECTION_NAME}' populated at {CHROMA_DIR}")