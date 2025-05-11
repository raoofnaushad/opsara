# 🧠 Lokam AI – FastAPI Backend Architecture Guidelines

Establishing a well-organized backend structure from the outset is **crucial for maintainability and scalability**. The following modular design will ensure **clear separation of concerns** and allow the backend to support all three core chatbot types effectively.

---

## 📁 Recommended Project Directory Layout

```
backend/
└── app/
    ├── main.py                 # Primary entry point
    ├── api/
    │   ├── regular_chatbot.py  # API endpoints for Regular Chatbot
    │   ├── rag_chatbot.py      # API endpoints for RAG Chatbot
    │   └── mcp_agent.py        # API endpoints for MCP Agent
    ├── models/
    │   ├── schemas.py          # Pydantic request/response models
    │   └── db_models.py        # SQLAlchemy database models
    ├── database/
    │   ├── db.py               # DB session + engine setup
    │   ├── pgvector_utils.py   # Functions for PGVector integration
    │   └── crud.py             # Common database operations
    └── config.py               # App-wide configuration (env vars, settings, etc.)
```

---

## ⚙️ Core Design Principles

### ✅ Modular APIs per Chatbot Type

Define separate endpoints for each chatbot use case under `api/`:

- `POST /api/v1/regular_chatbot/` – For LLM-based responses without context.
- `POST /api/v1/rag_chatbot/` – For context-enriched RAG queries.
- `POST /api/v1/mcp_agent/` – For multi-agent workflows via MCP.

---

### ✅ API Versioning

Prefix all routes with `/api/v1/` to ensure **forward compatibility** with future changes.

---

## 🧩 Pydantic Models

Use `app/models/schemas.py` to define **request and response payloads**. This ensures data validation and clean API design.

```python
from pydantic import BaseModel

class ChatRequest(BaseModel):
    query: str

class ChatResponse(BaseModel):
    answer: str
```

---

## 🗃️ PostgreSQL + PGVector Integration

Use SQLAlchemy for ORM operations:

- Define all DB models in `models/db_models.py`
- Set up engine/session logic in `database/db.py`
- Store and query vector embeddings using utilities in `database/pgvector_utils.py`

---

## 🔧 Configuration Management

Centralize all configuration (e.g., environment variables, constants) in `config.py`:

```python
import os

DATABASE_URL = os.getenv("DATABASE_URL")
PGVECTOR_DIM = 1536
```

Use `.env` files with `python-dotenv` for loading configs.

---

## 🛠 ORM and CRUD Utilities

Implement reusable database operations inside `database/crud.py`:

- Chat history storage
- Agent config retrieval
- Vector search for RAG

---

## 🚀 Entry Point

Ensure `main.py` does the following:

- Loads FastAPI app
- Includes routers from `api/`
- Initializes DB
- Handles middleware and CORS

```python
from fastapi import FastAPI
from app.api import regular_chatbot, rag_chatbot, mcp_agent

app = FastAPI()

app.include_router(regular_chatbot.router, prefix="/api/v1/regular_chatbot")
app.include_router(rag_chatbot.router, prefix="/api/v1/rag_chatbot")
app.include_router(mcp_agent.router, prefix="/api/v1/mcp_agent")
```

---

## ✅ Summary

This structure provides:

- ✅ Clean code separation  
- ✅ Scalable design for multiple chatbot types  
- ✅ Easy extensibility and testing  
- ✅ Alignment with best practices for production-grade APIs
