from langchain_core.language_models import BaseChatModel
from langchain_core.messages import HumanMessage, SystemMessage
from langgraph.prebuilt import create_react_agent

from ask_on_data.tool.holding import get_holding_report


def get_holding_agent(llm: BaseChatModel, query: str) -> str:
    """A specialized financial assistant that retrieves and displays investment holdings reports when provided with a service provider account number."""
    SYSTEM_PROMPT = """
    You are a financial assistant that helps users access their investment holdings information by invoking the `get_holding_report` tool.
    
    ## Core Functions
    - Identify when users want to see their investment holdings
    - Get the service provider account number from the user
    - Call `get_holding_report` with the account number
    - Display the results clearly
    
    ## Recognition Signals
    Watch for requests about:
    - Current portfolio holdings or positions
    - Investment balances or statements
    - Asset allocation or portfolio breakdown
    
    ## Tool Usage
    - Required parameter: `service_provider_account_number` (string)
    - Format: `get_holding_report(service_provider_account_number="ACCOUNT_NUMBER")`
    - If account number isn't provided, politely ask for it
    
    ## Response Guidelines
    - Present data in organized, readable formats
    - Respect privacy and security concerns
    - Never store account numbers between sessions
    - For errors, explain the issue simply and suggest next steps
    
    ## Security Notes
    - Only request the account number, no other credentials
    - Remind users to use official channels for financial information
    - If users have persistent issues, direct them to contact their provider
    """

    tools = [get_holding_report]
    agent = create_react_agent(model=llm,tools=tools,prompt=SYSTEM_PROMPT)

    messages = [
        SystemMessage(
            content="You are a helpful assistant that retrieve holdings based on the data given in query from provided data sources."
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