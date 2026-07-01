# Components and structure of the pipeline for RAGAS:
from LLM → Answer → Evaluator
to 
Question → Retriever → Context → LLM → Answer → Evaluator
                           run_pipeline.py
                                   │
         ┌─────────────────────────┼─────────────────────────┐
         │                         │                         │
         │                         │                         │
    generator.py             evaluator.py            ground_truth.py
         │                         │
         │                         │
         │                    evaluates:
         │               - correctness
         │               - faithfulness
         │               - hallucination
         │               - context relevance
         │
         │
    retriever.py
         │
         │
    documents/
         │
         └── my_doc.txt


         generator.py also uses:
                    │
                    ▼
          llm_providers/
               │
        ┌──────┴──────┐
        │             │
     base.py   ollama_provider.py

## to run the pipeline:
1. Install the required libraries (SymPy for ground truth calculations):
```
pip install sympy
```
2. Install model e.g. 
```
ollama pull llama3
```
3. Run the pipeline:
```python
"python run_pipeline.py"

```

## Example output:
```
====================
QUESTION: What is the project code name?

RETRIEVED CONTEXT:
The secret project code name is ORION-7.
The launch date is March 2027.
The lead engineer is Alice Navarro.

GROUND TRUTH: None

MODEL ANSWER:
The project code name is ORION-7.

EVALUATOR RAW RESPONSE:
{'model': 'llama3', 'created_at': '2026-05-08T11:36:07.5648419Z', 'message': {'role': 'assistant', 'content': '{\n  "correctness": 1,\n  "faithfulness": 1,\n  "context_relevance":
 1,\n  "hallucination": 0,\n  "overall_score": 0.75\n}'}, 'done': True, 'done_reason': 'stop', 'total_duration': 23643000300, 'load_duration': 248280400, 'prompt_eval_count': 202, 'prompt_eval_duration': 13232064300, 'eval_count': 47, 'eval_duration': 8044394700}

EVALUATION:
{'correctness': 1, 'faithfulness': 1, 'context_relevance': 1, 'hallucination': 0, 'overall_score': 0.75}
```