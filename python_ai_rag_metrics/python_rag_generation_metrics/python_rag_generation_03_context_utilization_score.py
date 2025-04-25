# Generation metrics
# Context Utilization
# good / satisfied /bad
# > 0.7/ 0.4-0.7	/ < 0.4

from sentence_transformers import SentenceTransformer, util

# Initialize embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Retrieved context (simulate retrieved docs)
retrieved_context = """
Databricks is a unified platform for big data and AI. It supports Apache Spark and Delta Lake.
Users can collaborate using notebooks and build ML models at scale.
It also allows for real-time data ingestion and processing.
"""

# Generated answer by the LLM
generated_answer = """
Databricks is a unified data and AI platform that uses Apache Spark.
It also helps users build machine learning models collaboratively using notebooks.
"""

# Split context into individual sentences
context_sentences = [s.strip() for s in retrieved_context.strip().split('.') if s.strip()]
used_sentences = 0
threshold = 0.65  # similarity threshold to consider a context sentence "used"

# Compute embedding for the generated answer once
answer_embedding = model.encode(generated_answer, convert_to_tensor=True)

# For each context sentence, see if it matches the answer
for sentence in context_sentences:
    context_embedding = model.encode(sentence, convert_to_tensor=True)
    similarity = util.cos_sim(context_embedding, answer_embedding).item()

    if similarity > threshold:
        used_sentences += 1

# Compute utilization score
context_utilization_score = used_sentences / len(context_sentences)

print(f"📈 Context Utilization Score: {context_utilization_score:.2f}")