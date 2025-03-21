import os
from typing import Annotated, List, Sequence, TypedDict

from dotenv import load_dotenv
# Import necessary modules
from langchain_core.messages import BaseMessage, HumanMessage, SystemMessage
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent


# Define your tools
@tool
def fetch_weather(location: str) -> str:
    """Fetch the current weather for a location."""
    # In a real scenario, this would call a weather API
    # For this example, we'll simulate a response
    return f"The weather in {location} is sunny with a temperature of 25°C."


@tool
def recommend_activities(weather_info: str) -> List[str]:
    """Recommend activities based on weather information."""
    # Parse the weather info and make recommendations
    if "sunny" in weather_info.lower():
        return ["Go for a hike", "Have a picnic", "Visit the beach"]
    elif "rainy" in weather_info.lower():
        return ["Visit a museum", "Watch a movie", "Read a book"]
    else:
        return ["Go for a walk", "Visit a local café", "Shopping"]


@tool
def create_itinerary(activities: List[str], duration_hours: int) -> str:
    """Create an itinerary based on recommended activities and duration."""
    if not activities or duration_hours <= 0:
        return "Unable to create itinerary with the provided information."

    hours_per_activity = duration_hours // len(activities)
    remaining_hours = duration_hours % len(activities)

    itinerary = "Your Itinerary:\n"
    start_time = 9  # Starting at 9 AM

    for i, activity in enumerate(activities):
        hours = hours_per_activity
        if i < remaining_hours:
            hours += 1

        end_time = start_time + hours
        itinerary += f"{start_time:02d}:00 - {end_time:02d}:00: {activity}\n"
        start_time = end_time

    return itinerary


# Create a list of tools
tools = [fetch_weather, recommend_activities, create_itinerary]

# Initialize the LLM
llm = ChatOpenAI(temperature=0)

# Create the ReAct agent
react_agent = create_react_agent(llm, tools)


# Define a handler function for the agent
def invoke_agent(message: str) -> Sequence[BaseMessage]:
    """Invoke the agent with a message and return the response."""
    messages = [
        SystemMessage(
            content="You are a helpful travel planning assistant. Use the tools available to help users plan their day based on weather and their preferences."
        ),
        HumanMessage(content=message),
    ]
    response = react_agent.invoke({"messages": messages})
    return response["messages"]


# Example usage
if __name__ == "__main__":
    load_dotenv()
    query = "I'm going to San Francisco tomorrow for 6 hours. What should I do?"
    response = invoke_agent(query)

    # Print the agent's thought process and final response
    for message in response:
        print(f"{message.type}: {message.content}")
        print("-" * 50)
