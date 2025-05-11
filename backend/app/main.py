from fastapi import FastAPI
from app.api import  rag_chatbot, mcp_agent

app = FastAPI()

app.include_router(rag_chatbot.router, prefix="/api/v1/rag_chatbot")
app.include_router(mcp_agent.router, prefix="/api/v1/mcp_agent")


