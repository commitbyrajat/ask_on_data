from typing import TypedDict, List, Literal

from langchain_core.language_models import BaseChatModel
from pydantic import BaseModel, Field


class Context(BaseModel):
    """
    Context state for LangGraph that determines the field value based on the query's intent.

    - Returns "FIXED_DEPOSIT" if the query involves initiating an action to open an FD.
    - Returns "HOLDINGS" if the query asks for holding details based on given PAN card numbers.
    - Returns "FAQ" by default for any other queries.
    """

    value: Literal["FIXED_DEPOSIT", "HOLDINGS", "FAQ"] = Field(
        description=(
            "Returns 'FIXED_DEPOSIT' if the query relates to opening an FD, "
            "'HOLDINGS' if it requests holding details using PAN card numbers, "
            "otherwise returns 'FAQ' by default."
        )
    )


class GraphState(TypedDict):
    query: str
    llm: BaseChatModel
    context: Context
