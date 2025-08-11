# ABZUMS-AI-assignments
ABZUMS AI assignments of alinesmaeili

## Quickstart

1. Create and activate a virtual environment.
2. Install dependencies as needed for each assignment or script.
3. Provide your API keys via environment variables.

### Environment variables

Create a `.env` file (or export in your shell) with:

```
OPENAI_API_KEY=your_key_here
OPENAI_BASE_URL=https://api.avalai.ir/v1
```

### Running `API.py`

```
python API.py
```

You will be prompted to enter a conversation tone and then interact with the assistant.

## RAG pipeline (from images)

- **Pre-processing**: Extract PDF content (e.g., `pdfplumber`).
- **Structuring**: Use a library like `unstructured` to normalize elements into dictionaries.
- **Vector DB + Embeddings**: Generate embeddings (OpenAI, Hugging Face `sentence-transformers`) and index in a vector store (Pinecone, Weaviate, ChromaDB).
- **Searchable DB**:
  - Indexing phase: store embeddings and metadata.
  - Retrieval phase: embed query, search vector DB, return results.
- **AI brain**:
  - UI accepts a query.
  - Retrieval pipeline fetches relevant chunks.
  - LLM generation via API (OpenAI, Google Gemini, Anthropic Claude, or OSS models from Hugging Face).

Images can be added under `docs/` and referenced here once available, for example:

`docs/rag_overview.jpg`
`docs/ai_brain_options.jpg` 
