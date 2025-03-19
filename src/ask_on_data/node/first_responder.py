from typing import Dict, Any

from ask_on_data.chain.first_responder_chain import get_first_responder_chain
from ask_on_data.state.graph_state import GraphState


def first_responder(state: GraphState) -> Dict[str, Any]:
    llm = state["llm"]
    query = state["query"]
    result = get_first_responder_chain(llm, query)
    return {"context": result[-1]}
