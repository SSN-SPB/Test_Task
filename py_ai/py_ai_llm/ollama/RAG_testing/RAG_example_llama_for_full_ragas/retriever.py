from sentence_transformers import SentenceTransformer
import numpy as np


class SimpleRetriever:
    def __init__(self, documents):
        self.documents = documents

        self.model = SentenceTransformer(
            "all-MiniLM-L6-v2"
        )

        self.embeddings = self.model.encode(documents)

    def retrieve(self, query, k=2):

        query_embedding = self.model.encode([query])[0]

        scores = np.dot(
            self.embeddings,
            query_embedding
        )

        top_indices = np.argsort(scores)[-k:][::-1]

        return [
            self.documents[i]
            for i in top_indices
        ]