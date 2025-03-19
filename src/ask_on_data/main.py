from dotenv import load_dotenv

from ask_on_data.graph.graph import Graph
from ask_on_data.model.repository import Repository

if __name__ == "__main__":
    load_dotenv()
    repository = Repository()

    # # Casual Chat example
    # result = repository.get_llm().invoke(
    #     "what is the capital of India ? and what is its population"
    # )
    # print(result.content)
    #
    # # Agent Example
    # hello_world_agent = HelloWorld(repository)
    # print(
    #     hello_world_agent.invoke(
    #         "What is the sum of ten thousand Eight hundred and 7890"
    #     )
    # )

    graph = Graph()
    # graph.get_graph().invoke(input={'query':'My pan number is ABCD1234. Please find by holdings.','llm':repository.get_llm()})
    graph.get_graph().invoke(
        input={"query": "how to open a savings account?.", "llm": repository.get_llm()}
    )
