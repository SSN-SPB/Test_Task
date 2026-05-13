# required libraries
```
pip install langfuse
pip install langfuse openai python-dotenv
```
```
# Setting up Langfuse
# 1. Create an account on Langfuse and get your API key.
# 2. Set the API key as an environment variable:
#    - On Windows:
#      ```cmd       
#      setx LANGFUSE_API_KEY "your_api_key_here"
#      ```
#    - On macOS/Linux:
#      ```bash          
#      export LANGFUSE_API_KEY="your_api_key_here"
#      ```  
```    
## Place it to .env file
LANGFUSE_PUBLIC_KEY=pk-lf-...
LANGFUSE_SECRET_KEY=sk-lf-...

## Run the test
```python
python .\langfuse_copilot_example.py
for running
python .\langfuse_copilot_example3_opus4_6real_model.py
   need to install llama3 by command
# Install Ollama: https://ollama.com
# Then pull the model:
ollama pull llama3
ollama pull mistral
```

The typical response for langfuse_copilot_example5_opus4_6compare_misttral_llama3.py should be:
```[llama3] Q: What is Langfuse used for?
  Answer: Langridge is a type of glassblowing technique that involves gathering molten gla...
  Scores: {'quality': 0.0, 'hallucination': True, 'relevance': 0.0}

[llama3] Q: What is Python?
  Answer: Python is a high-level, interpreted programming language that is widely used for...
  Scores: {'quality': 1.0, 'hallucination': False, 'relevance': 1.0}

[llama3] Q: What is 2 + 2?
  Answer: The answer to 2 + 2 is... 4!...
  Scores: {'quality': 1.0, 'hallucination': False, 'relevance': 1.0}

[mistral] Q: What is Langfuse used for?
  Answer:  LangFUSE is a filesystem that allows you to mount and interact with large text ...
  Scores: {'quality': 0.0, 'hallucination': True, 'relevance': 0.0}

[mistral] Q: What is Python?
  Answer:  Python is a high-level, general-purpose programming language that is widely use...
  Scores: {'quality': 1.0, 'hallucination': False, 'relevance': 1.0}

[mistral] Q: What is 2 + 2?
  Answer:  The sum of 2 + 2 is 4....
  Scores: {'quality': 1.0, 'hallucination': False, 'relevance': 1.0}
```
