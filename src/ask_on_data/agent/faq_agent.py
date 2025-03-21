from dotenv import load_dotenv
from langchain_core.language_models import BaseChatModel
from langchain_core.messages import HumanMessage, SystemMessage
from langgraph.prebuilt import create_react_agent

from ask_on_data.model.repository import Repository
from ask_on_data.tool.faq import query_content_file


def get_faq_agent(llm: BaseChatModel, query: str) -> str:
    """Invoke the agent with a message and return the response."""
    SYSTEM_PROMPT = """You are a helpful assistant that answers questions based only on provided data sources.

    IMPORTANT: When a user asks any question about data or information:
    1. You MUST use the query_content_file tool
    2. You MUST pass the user's query EXACTLY as written to the tool
    3. Do NOT modify, rephrase, or summarize the user's query when passing it to the tool
    4. After receiving the tool's response, answer according to the instructions provided by the tool

    Do not try to answer data questions from your own knowledge. Always use the tool first.
    """
    tools = [query_content_file]
    agent = create_react_agent(model=llm, tools=tools, prompt=SYSTEM_PROMPT)

    messages = [
        SystemMessage(
            content="You are a helpful assistant that answers questions based only on provided data sources."
        ),
        HumanMessage(content=query),
    ]
    events = agent.stream({"messages": messages}, stream_mode="values")
    responses = []
    for event in events:
        # event["messages"][-1].pretty_print()
        response = event["messages"][-1].content
        responses.append(response)

    return responses[-1]


if __name__ == "__main__":
    load_dotenv()
    repo = Repository()
    prompt = get_faq_agent(
        repo.get_llm(),
        "SmartWealth mein invest karne ke liye kya mujhe kuch karna padega?",
    )
    print(prompt)
