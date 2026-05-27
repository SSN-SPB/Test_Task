# Components and structure of the pipeline:
LLM → Answer → Evaluator
evaluate_response(question, response, ground_truth)

            run_pipeline.py
                  │
   ┌──────────────┼──────────────┐
   │              │              │
generator.py  evaluator.py  ground_truth.py
   │              │              │
   └────── llm_providers/ ───────┘

1. run_pipeline.py - main script to execute the entire pipeline (orchestrator)
* Sends a question through the system
* Coordinates all components
* Prints results
* In real ML systems: like a training loop runner
* In RAG systems: like the main inference loop
Responsibilities:

✔ calls generator
✔ calls ground truth
✔ calls evaluator
✔ displays results

2. generator.py - responsible for generating answers to questions using an LLM (Ollama in this case)
* Takes a question as input
* Uses the LLM to generate a response
  ```
  generator.generate_response()
  ```
* Returns the generated answer
Responsibilities:
* Interface with the LLM provider (Ollama)
* defines system prompt
* hides model implementation
* delegates to provider
* Return the raw response from the LLM

3. ground_truth.py - responsible for calculating the correct answer to the question (using SymPy in this case)
   (GOLD STANDARD ANSWER GENERATOR)
Responsibilities:
* Takes the same question as input
* Uses a reliable method (e.g. SymPy) to compute the correct answer
* Returns the ground truth answer for evaluation
4. evaluator.py — JUDGE SYSTEM (LLM-as-a-judge)
* Takes the generated answer and the ground truth as input
* Uses a set of evaluation criteria to assess the quality of the generated answer (e.g. correctness, reasoning quality, instruction following, clarity, hallucination)
* Returns an evaluation score or a set of scores based on the criteria
Responsibilities:
* Define evaluation criteria
* compare against ground truth
* Return evaluation results

4. llm_providers/ - a directory containing code to interface with different LLM providers (e.g. Ollama)
* Contains code to send prompts to the LLM and receive responses
* Abstracts away the details of how to interact with the LLM
Responsibilities:
* Provide a clean interface for sending prompts and receiving responses from the LLM
* Handle any necessary formatting or preprocessing of prompts
* Handle any necessary postprocessing of responses
* Allow for easy switching between different LLM providers if needed

5. base.py - a base class for LLM providers that defines a common interface for generating responses
* This allows for easy integration of different LLM providers by implementing the same interface
* Defines a method like `generate_response(prompt)` that all LLM providers must implement
Responsibilities:
* Define a common interface for LLM providers
```
generate(system_prompt, user_prompt)
```
* Ensure consistency in how responses are generated across different providers



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
QUESTION: How do I solve 5x + 3 = 2 for x?

MODEL RESPONSE:
 Let's break it down step by step.

We have an equation: 5x + 3 = 2

Our goal is to isolate the variable x. To do that, we'll need to get rid of the constant term (+3) and then solve for x.

Here's the first step:

Subtract 3 from both sides of the equation to get:

5x + 3 - 3 = 2 - 3

This simplifies to:

5x = -1

Now we have a simpler equation, but still with an unknown variable. Next step:

Divide both sides by 5 (the coefficient of x) to solve for x.

5x / 5 = -1 / 5

This gives us:

x = -1/5

And that's the answer! We solved for x.

So, what is x? Well, x is equal to negative one fifth. That's right: -1/5.

GROUND TRUTH: None

EVALUATION:
 {'correctness': 1, 'reasoning_quality': 1, 'instruction_following': 1, 'clarity': 0.9, 'hallucination': 0, 'overall_score': 0.95}
```