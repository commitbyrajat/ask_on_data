from typing import Any

from ask_on_data.agent.faq_agent import get_faq_agent
from ask_on_data.state.graph_state import GraphState


def get_faq_node(state: GraphState) -> dict[str, Any]:
    llm = state["llm"]
    query = state["query"]
    result = get_faq_agent(llm, query)
    return {"result": result}
