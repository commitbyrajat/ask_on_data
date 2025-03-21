from dotenv import load_dotenv

from ask_on_data.graph.graph import Graph
from ask_on_data.model.repository import Repository

if __name__ == "__main__":
    load_dotenv()
    repository = Repository()
    graph = Graph()
    # graph.get_graph().invoke(input={'query':'My pan number is ABCD1234. Please find by holdings.','llm':repository.get_llm()})
    executor = graph.get_graph().invoke(
        input={
            "query": "SmartWealth mein invest karne ke liye kya mujhe kuch karna padega?",
            "llm": repository.get_llm(),
        }
    )
    result = executor["result"]
    print(result)
