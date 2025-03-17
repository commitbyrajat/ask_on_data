# ask-on-data  

A Python project that utilizes **LangChain**, **LangGraph**, and **OpenAI's LLMs** to perform AI-driven data queries and calculations.  

## Features  
- **Casual Chat**: Uses LLMs to answer general knowledge queries.  
- **Agent-based Processing**: Implements a **HelloWorld agent** that performs numerical calculations.  
- **Tool Integration**: Includes an `add_number` tool for sum calculations.  

## Project Structure  
```
ask-on-data/  
│── src/  
│   ├── ask_on_data/  
│   │   ├── main.py                # Entry point of the application  
│   │   ├── agent/  
│   │   │   ├── hello_world.py      # Defines the HelloWorld agent  
│   │   ├── model/  
│   │   │   ├── repository.py       # Manages LLM model  
│   │   ├── tool/  
│   │   │   ├── add_number.py       # Defines a tool to add numbers  
│── pyproject.toml  
│── README.md  
```  

## Setup & Installation  

### 1️⃣ Install **Rye**  
Ensure you have Rye installed. If not, install it using:  
```sh  
curl -sSf https://rye.astral.sh/get | bash  
```  
Then restart your shell and enable Rye:  
```sh  
rye self install  
```  

### 2️⃣ Clone the Repository  
```sh  
git clone <your-repo-url>  
cd ask-on-data  
```  

### 3️⃣ Set Up the Project Environment  
```sh  
rye sync  
```  

### 4️⃣ Set Up Environment Variables  
This project uses **OpenAI API keys**. Create a `.env` file in the project root and add:  
```
OPENAI_API_KEY=your_api_key_here  
```  

### 5️⃣ Run the Application  
```sh  
rye run start  
```  

### Example Output  
Running the project produces the following output:  
```sh  
$ rye run start  

The capital of India is New Delhi. As for the population, as of the latest estimates in 2023, the population of New Delhi is approximately 21 million people when considering the broader National Capital Territory of Delhi. The population figures can vary based on the specific area being referenced, so it's always a good idea to check the most recent census or demographic data for the latest numbers.  

================================ Human Message =================================  
What is the sum of ten thousand Eight hundred and 7890  

================================== Ai Message ==================================  
Name: Hello_World_Addition_Agent  
Tool Calls:  
  add (call_7FxEGPU3kUuoxnrCyg0wr3p6)  
 Call ID: call_7FxEGPU3kUuoxnrCyg0wr3p6  
  Args:  
    a: 10800  
    b: 7890  

================================= Tool Message =================================  
Name: add  
18690  

================================== Ai Message ==================================  
Name: Hello_World_Addition_Agent  
The sum is 18690.  

{'agent_result': 'The sum is 18690.'}  
```  

## Dependencies  
The project uses:  
- `langgraph>=0.3.11`  
- `langchain-openai>=0.3.8`  
- `black>=25.1.0`  
- `isort>=6.0.1`  
- `langchain-community>=0.3.19`  


---

Raise a PR if you want any modifications! 🚀