from langgraph.graph import StateGraph

from ask_on_data.node.faq_service import get_faq_node
from ask_on_data.node.first_responder import first_responder
from ask_on_data.node.fixed_deposit_service import get_fixed_deposit_node
from ask_on_data.node.holdings_service import get_holdings_node
from ask_on_data.router.context_router import get_context_router
from ask_on_data.state.graph_state import GraphState


class Graph:
    def __init__(self):
        self.graph = StateGraph(GraphState)
        self.graph.add_node("first_responder", first_responder)
        self.graph.set_entry_point("first_responder")

        self.graph.add_node("FAQ", get_faq_node)
        self.graph.add_node("HOLDINGS", get_holdings_node)
        self.graph.add_node("FIXED_DEPOSIT", get_fixed_deposit_node)

        self.graph.add_conditional_edges(
            "first_responder",
            get_context_router,
            {"FAQ": "FAQ", "HOLDINGS": "HOLDINGS", "FIXED_DEPOSIT": "FIXED_DEPOSIT"},
        )

        self.graph = self.graph.compile()

    def get_graph(self):
        return self.graph
