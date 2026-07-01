# Pre Installation Requirements

1. Download and install Ollama from https://ollama.com/download
2. Pull the LLaMA 3 model using the command:
```
ollama pull llama3
``` 
3. Install the required Python libraries:
```
pip install openai langsmith pytest python-dotenv
or
pip install -r requirements.txt
``` 
# Setup Instructions
add valid .env file with the following content:
```
LANGCHAIN_TRACING_V2=true
LANGCHAIN_API_KEY=lsv2_pt_xxxxxxx
LANGCHAIN_PROJECT=ollama-llama3-tests
```
# Run the tests
``` 
pytest -v
```

# Expected Output
```
============================= test session starts ==============================
collected 3 items           
test_langchain_ollama_llama3.py::test_ollama_llama3_response PASSED [ 33%]
test_langchain_ollama_llama3.py::test_ollama_llama3_response_with_langchain PASSED [ 66%]
test_langchain_ollama_llama3.py::test_ollama_llama3_response_with_langchain_and_tracing PASSED [100%]
============================== 3 passed in 0.XXs ==============================