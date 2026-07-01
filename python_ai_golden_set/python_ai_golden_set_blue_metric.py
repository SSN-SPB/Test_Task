# pip install nltk rouge-score sentence-transformers scikit-learn

import numpy as np
from nltk.translate.bleu_score import sentence_bleu, SmoothingFunction
from rouge_score import rouge_scorer
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# -------------------------
# 1. Golden Set (reference vs prediction)
# -------------------------
golden_set = [
    {
        "reference": "The cat sat on the mat.",
        "prediction": "The cat is sitting on the mat.",
    },
    {
        "reference": "AI is transforming the world.",
        "prediction": "Artificial intelligence is changing the world.",
    },
    {
        "reference": "He quickly ran to the store.",
        "prediction": "He ran fast to the shop.",
    },
]


# -------------------------
# 2. BLEU Evaluation
# -------------------------
def compute_bleu(reference, prediction, weights=(0.25, 0.25, 0.25, 0.25)):
    ref_tokens = [reference.split()]
    pred_tokens = prediction.split()

    smoothing = SmoothingFunction().method1
    return sentence_bleu(
        ref_tokens, pred_tokens, weights=weights, smoothing_function=smoothing
    )


# -------------------------
# 3. ROUGE Evaluation
# -------------------------
rouge = rouge_scorer.RougeScorer(["rouge1", "rouge2", "rougeL"], use_stemmer=True)


def compute_rouge(reference, prediction):
    scores = rouge.score(reference, prediction)
    return {
        "rouge1": scores["rouge1"].fmeasure,
        "rouge2": scores["rouge2"].fmeasure,
        "rougeL": scores["rougeL"].fmeasure,
    }


# -------------------------
# 4. Semantic Similarity
# -------------------------
model = SentenceTransformer("all-MiniLM-L6-v2")


def compute_semantic_similarity(reference, prediction):
    embeddings = model.encode([reference, prediction])
    return cosine_similarity([embeddings[0]], [embeddings[1]])[0][0]


# -------------------------
# 5. Run Evaluation
# -------------------------
results = []

for item in golden_set:
    ref = item["reference"]
    pred = item["prediction"]

    bleu_default = compute_bleu(ref, pred)

    # 🔁 CHANGING BLEU METRIC (bigram-focused)
    bleu_bigram = compute_bleu(ref, pred, weights=(0.5, 0.5, 0, 0))

    rouge_scores = compute_rouge(ref, pred)
    semantic_score = compute_semantic_similarity(ref, pred)

    results.append(
        {
            "reference": ref,
            "prediction": pred,
            "bleu_default": bleu_default,
            "bleu_bigram": bleu_bigram,
            "rouge1": rouge_scores["rouge1"],
            "rouge2": rouge_scores["rouge2"],
            "rougeL": rouge_scores["rougeL"],
            "semantic_similarity": semantic_score,
        }
    )

# -------------------------
# 6. Display Results
# -------------------------
for i, r in enumerate(results):
    print(f"\nExample {i + 1}")
    print("Reference:", r["reference"])
    print("Prediction:", r["prediction"])
    print(f"BLEU (default 4-gram): {r['bleu_default']:.4f}")
    print(f"BLEU (bigram-weighted): {r['bleu_bigram']:.4f}")
    print(f"ROUGE-1: {r['rouge1']:.4f}")
    print(f"ROUGE-2: {r['rouge2']:.4f}")
    print(f"ROUGE-L: {r['rougeL']:.4f}")
    print(f"Semantic Similarity: {r['semantic_similarity']:.4f}")

# Thresholds for good vs bad
# BLEU (default 4-gram): > 0.5 / < 0.2 ( >0.6 is excellent, <0.1 is poor)
# BLEU (bigram-weighted): > 0.5 / < 0.2 ( >0.6 is excellent, <0.1 is poor)
# ROUGE-1 (Recall): > 0.6 / < 0.3 ( >0.7 is excellent, <0.2 is poor)
# ROUGE-2 (Precision): > 0.4 / < 0.2 ( >0.7 is excellent, <0.2 is poor)
# ROUGE-L (Longest common subsequence): > 0.6 / < 0.3 ( >0.7 is excellent, <0.2 is poor)
# Semantic Similarity (cosine similarity): > 0.8 / < 0.5 ( >0.9 is excellent, <0.4 is poor)
