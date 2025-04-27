import nltk
from nltk.translate.bleu_score import (SmoothingFunction,  # for blue
                                       sentence_bleu)
from nltk.translate.meteor_score import meteor_score  # for meteor
from rouge_score import rouge_scorer  # for rouge
from sentence_transformers import SentenceTransformer, util  # for faithful

# Load a pre-trained embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Simulated retrieved context from a RAG system
# retrieved_context = """
# Databricks is a cloud-based data platform designed for data engineering, analytics, and machine learning.
# It supports collaborative notebooks, Apache Spark, and Delta Lake for scalable, reliable data workflows.
# """
retrieved_context = """
Paris is a capital of France
"""

# Generated answer by the LLM
# generated_answer = """
# Databricks helps teams collaborate on big data workflows and also supports machine learning pipelines using Apache Spark.
# """
generated_answer = """
Paris is a city.
"""
# Generation metrics
# 1 Faithfulness / Factuality	Whether the answer is factually grounded in the retrieved documents.
# value 1:perfect 0:bad
# good / bad
# # 2 BLEU	> 0.5 /	< 0.2
# ROUGE-1 (Recall)	> 0.6 /	< 0.3
# ROUGE-L (Longest common subsequence)	> 0.6 / < 0.3
# METEOR	> 0.6 / < 0.3

# Break both into sentences
retrieved_sentences = retrieved_context.strip().split(".")
generated_sentences = generated_answer.strip().split(".")

# Compute faithfulness: for each sentence in the answer, check if it’s similar to something in the context
threshold = 0.7  # Cosine similarity threshold to count a sentence as "grounded"
faithful_count = 0

for gen_sentence in generated_sentences:
    if not gen_sentence.strip():
        continue
    gen_embedding = model.encode(gen_sentence, convert_to_tensor=True)

    max_similarity = max(
        util.cos_sim(gen_embedding, model.encode(sent, convert_to_tensor=True)).item()
        for sent in retrieved_sentences
        if sent.strip()
    )

    if max_similarity > threshold:
        faithful_count += 1

faithfulness_score = faithful_count / len(generated_sentences)

print(f"Faithfulness Score: {faithfulness_score:.2f}")

reference_answer = """
Databricks is a cloud-based platform that allows teams to build data workflows and machine learning models using Apache Spark.
"""

# Tokenized inputs for BLEU and METEOR
reference_tokens = [reference_answer.strip().split()]
generated_tokens = generated_answer.strip().split()

# BLEU Score
smoothie = SmoothingFunction().method4
bleu = sentence_bleu(reference_tokens, generated_tokens, smoothing_function=smoothie)
print(f"🔷 BLEU Score: {bleu:.2f}")

# ROUGE Score
scorer = rouge_scorer.RougeScorer(["rouge1", "rougeL"], use_stemmer=True)
rouge = scorer.score(reference_answer, generated_answer)
print(f"🔴 ROUGE-1 (Precision, Recall, F1): {rouge['rouge1']}")
print(f"🔴 ROUGE-L (Longest Match): {rouge['rougeL']}")

# METEOR Score
meteor = meteor_score([reference_answer], generated_answer)
print(f"🟢 METEOR Score: {meteor:.2f}")
