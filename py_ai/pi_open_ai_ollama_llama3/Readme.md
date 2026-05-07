# Pre Installation Requirements

1. Download and install Ollama from https://ollama.com/download
2. Pull the LLaMA 3 model using the command:
```
ollama pull llama3
or
ollama pull llama3:latest
or
ollama pull llama3:3.1.0  
or
ollama pull mistral
ollama pull phi3
ollama pull gemma
``` 
3. Install the required Python libraries:
```
pip install sympy
pip install ollama
``` 
Run the pipeline:
```python run_pipeline.py (or single file like py_ai_ollama_llama3_00.py)
```