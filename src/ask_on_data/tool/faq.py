import os
from os import path
from typing import Optional

from langchain_core.tools import tool


@tool
def query_content_file(query: str, file_path: Optional[str] = None) -> str:
    """
    Use exact query input by user before generating answer for given data.
    Search through a content file to find information related to a specific query.
    The tool returns a prompt that instructs the LLM to answer only using the content
    found in the file, or to indicate if the data is not present.

    Args:
        query: The exact question or query from the user
        file_path: Optional path to the text file. If not provided, uses default path.

    Returns:
        A prompt containing both the relevant content and instructions for the LLM
    """

    if file_path is None:
        file_path = path.join(
            path.dirname(__file__), "..", "..", "resources", "faq.csv"
        )

    if not os.path.exists(file_path):
        return f"ERROR: The file '{file_path}' does not exist. Please provide a valid file path."

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()

        prompt = f"""
                QUERY: {query}
            
                SOURCE CONTENT:
                {content}
            
                INSTRUCTIONS:
                1. Answer the query ONLY using information found in the SOURCE CONTENT above.
                2. If the information needed to answer the query is not present in the SOURCE CONTENT, respond with: "I cannot answer this query based on the provided data."
                3. Do not use prior knowledge or external information to supplement your answer.
                4. When providing information, include a brief mention of which section or paragraph from the SOURCE CONTENT contains the relevant information.
                5. Keep your answer concise and directly related to the query.
            
                Based strictly on the SOURCE CONTENT, please answer the query.
                """
        return prompt

    except Exception as e:
        return f"ERROR: Failed to process the file. Exception: {str(e)}"
