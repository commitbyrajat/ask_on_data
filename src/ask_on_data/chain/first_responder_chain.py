from typing import Union

from langchain_core.language_models import BaseChatModel
from langchain_core.messages import HumanMessage
from langchain_core.output_parsers import PydanticToolsParser
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

from ask_on_data.state.graph_state import Context

pydantic_parser = PydanticToolsParser(tools=[Context])


def get_first_responder_chain(llm: Union[BaseChatModel], query: str) -> Context:
    first_responder_prompt_template = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                """
             You are expert in finding context of the given queries. 
             Read the query properly and return the relevant context.
             """,
            ),
            MessagesPlaceholder(variable_name="messages"),
        ]
    )

    first_responder_chain = first_responder_prompt_template | llm.bind_tools(
        tools=[Context], tool_choice="Context"
    )
    first_responder_chain = first_responder_chain | pydantic_parser
    result: Context = first_responder_chain.invoke(
        input={"messages": [HumanMessage(content=query)]}
    )
    return result
