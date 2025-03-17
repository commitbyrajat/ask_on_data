from langchain_core.tools import tool


@tool
def add(a: int, b: int) -> int:
    """add two numbers and return the sum"""
    return a + b
