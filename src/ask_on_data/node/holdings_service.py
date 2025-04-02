from ask_on_data.agent.holding_agent import get_holding_agent
from ask_on_data.state.graph_state import GraphState


def get_holdings_node(state: GraphState):
    llm = state["llm"]
    query = state["query"]
    result = get_holding_agent(llm, query)
    return {"result": result}
