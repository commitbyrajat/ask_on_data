from ask_on_data.state.graph_state import GraphState


def get_context_router(state: GraphState) -> str:
    return state["context"].value
