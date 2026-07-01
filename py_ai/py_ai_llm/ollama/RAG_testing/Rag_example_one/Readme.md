# Structure of mini RAG evaluation system:

1. Generator (Claude tutor) - generates questions and answers based on a given topic
2. Ground truth engine (SymPy) - provides correct answers for the generated questions - ground_truth.py
3. LLM judge (evaluation metrics) - evaluates the generated answers against the ground truth answers using various metrics (e.g., accuracy, precision, recall) - evaluator.py
4. Pipeline runner - orchestrates the entire process, from question generation to evaluation - run_pipeline.py

## to run the pipeline:
1. Make sure you have Python installed on your system.
2. Install the required libraries (SymPy for ground truth calculations):
```pip install sympy
```
3. Run the pipeline:
```python
"python run_pipeline.py"

```

<br>
## Example output:
```

====================
QUESTION: How do I solve 5x + 3 = 2 for x?

MODEL RESPONSE:
 Great question! Let's work through this step by step.

**Your goal is to get x by itself on one side of the equation.**

---

**Step 1: Get rid of the +3**

To remove the 3 from the left side, you need to do the **opposite operation** — which is subtraction.

Subtract 3 from **both sides**:

> 5x + 3 - 3 = 2 - 3

What does that simplify to on each side?

GROUND TRUTH: [-1/5]

EVALUATION:
json
{
  "correctness": 0.7,
  "reasoning_quality": 0.8,
  "instruction_following": 0.6,
  "clarity": 0.9,
  "hallucination": 1.0,
  "overall_score": 0.75
}

```