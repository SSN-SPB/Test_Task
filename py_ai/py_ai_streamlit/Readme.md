# Pre Installation Requirements

1. Download and install Ollama from https://ollama.com/download
2. Pull the LLaMA model using the command:
```
ollama pull llava
ollama pull moondream
``` 
3. Check by command
```commandline
ollama list
```
or by command:
```commandline
ollama show llava
ollama show moondream
```

# Run application
```commandline
streamlit run .\py_ai_streamlit_01basic.py 
```

# Check application
You can now view your Streamlit app in your browser.
```
  Local URL: http://localhost:8501
  Network URL: http://192.168.0.11:8501
```