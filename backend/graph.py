# Minimal LangGraph sketch for HPI orchestration
from langgraph.graph import StateGraph, END
from typing import Dict, Any
from .agents.hpi_core import HPIState, hpi_core_reply

def build_hpi_graph():
    graph = StateGraph(HPIState)

    def start_node(state: HPIState) -> Dict[str, Any]:
        # No-op or boot message
        return {"boot": True}

    def hpi_node(state: HPIState) -> Dict[str, Any]:
        last_user = state.get("last_user", "")
        reply = hpi_core_reply(state, last_user)
        return {"last_assistant": reply}

    graph.add_node("start_node", start_node)
    graph.add_node("hpi_node", hpi_node)

    graph.add_edge("start", "hpi_node")
    graph.add_edge("hpi_node", END)
    graph.set_entry_point("start")
    return graph.compile()
