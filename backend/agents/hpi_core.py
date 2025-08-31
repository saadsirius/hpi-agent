# HPI Core Agent (skeleton)
# Goal: coordinate sub-agents, track overload, maintain an inner 'cognitive map'.

from typing import Dict, Any

class HPIState(dict):
    """Minimal state container."""
    pass

def hpi_core_reply(state: HPIState, user_message: str) -> Dict[str, Any]:
    # TODO: plug real LangGraph logic from graph.py
    # For now, return a structured dummy message.
    return {
        "role": "assistant",
        "content": f"[HPI-Core] J'ai bien reçu: {user_message}. Dis-moi où tu veux porter ton feu aujourd'hui.",
    }
