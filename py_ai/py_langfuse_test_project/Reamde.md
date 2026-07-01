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
   need to install models by command
# Install Ollama: https://ollama.com
# Then pull the models:
ollama pull llama3
ollama pull mistral
ollama pull llama3.2:3b 
```
## Checking
```
ollama list
check the models are installed
```
## check the memory usage
```
systeminfo | findstr /C:"Total Physical Memory" 
See results in the Langfuse dashboard: https://app.langfuse.com:
https://cloud.langfuse.com/project/cmp46rs8h02b1ad07e3sc2pb3
```

## The typical response for python .\langfuse_copilot_example3_opus4_6real_model.py should be:
```
Answer: Langfuse is a malware and ransomware variant that was discovered in 2017. It's primarily spread through phishing emails, exploits vulnerabilities on systems, and uses various social engineering tactics to gain access to victims' computers.

When infected, Langfuse encodes files using the AES encryption algorithm, making them inaccessible to users without providing a decryption key or password. The attackers might demand payment for the decryption key in cryptocurrency forms like Bitcoin.

Langfuse operates as an Ransomware-as-a-Service (RaaS), where hackers can buy and sell the software. It has evolved over time to improve its spread rate, evasion techniques, and anti-forensic tools.

If you suspect your system is infected with Lang fuse, it's recommended that you seek professional help from a cybersecurity expert or the operating system manufacturer for assistance in detecting and removing the threat.
```



```
[llama3] Q: What is Langfuse used for?
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
