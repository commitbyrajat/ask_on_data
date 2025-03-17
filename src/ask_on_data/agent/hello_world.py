from typing import Any

from langgraph.prebuilt import create_react_agent

from ask_on_data.model.repository import Repository
from ask_on_data.tool.add_number import add


class HelloWorld:
    def __init__(self, repository: Repository):
        tools = [add]
        system_prompt = "You are Fred, a friendly calculator. When given two numbers, return their sum without any extra explanation."
        self.agent = create_react_agent(
            repository.get_llm(),
            tools=tools,
            name="Hello_World_Addition_Agent",
            prompt=system_prompt,
        )
        # self.executor = AgentExecutor(agent=agent, tools=tools)

    def invoke(self, query: str) -> dict[str, Any]:
        events = self.agent.stream(
            {"messages": [("user", query)]}, stream_mode="values"
        )

        for event in events:
            event["messages"][-1].pretty_print()

        return {"agent_result": event["messages"][-1].content}
