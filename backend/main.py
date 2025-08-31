from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import requests
from typing import Optional, Dict, Any

from .config import USE_OLLAMA, OLLAMA_MODEL, OLLAMA_ENDPOINT
from .graph import build_hpi_graph
from .agents.hpi_core import HPIState, hpi_core_reply

app = FastAPI(title="HPI Agent API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatIn(BaseModel):
    message: str
    session_id: Optional[str] = "default"

class ChatOut(BaseModel):
    reply: str
    meta: Dict[str, Any] = {}

SESSIONS: Dict[str, HPIState] = {}

def call_ollama(prompt: str) -> str:
    payload = {
        "model": OLLAMA_MODEL,
        "prompt": prompt,
        "stream": False
    }
    try:
        resp = requests.post(OLLAMA_ENDPOINT, json=payload, timeout=120)
        resp.raise_for_status()
        data = resp.json()
        return data.get("response", "").strip()
    except Exception as e:
        return f"[Ollama error] {e}"

@app.post("/api/chat", response_model=ChatOut)
def chat(in_: ChatIn):
    sid = in_.session_id or "default"
    state = SESSIONS.setdefault(sid, HPIState())
    state["last_user"] = in_.message

    # 1) If Ollama enabled => get model answer, else use HPI core dummy reply
    if USE_OLLAMA:
        model_reply = call_ollama(in_.message)
        reply_text = model_reply or "Désolé, aucun retour du modèle local."
    else:
        reply = hpi_core_reply(state, in_.message)
        reply_text = reply["content"]

    # 2) Run minimal graph step (placeholder)
    graph = build_hpi_graph()
    _ = graph.invoke({"last_user": in_.message})

    return ChatOut(reply=reply_text, meta={"use_ollama": USE_OLLAMA})

@app.get("/api/health")
def health():
    return {"status": "ok"}
