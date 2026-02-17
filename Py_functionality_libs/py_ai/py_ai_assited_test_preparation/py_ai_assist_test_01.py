import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from collections import Counter

# Uncomment the following lines to download necessary NLTK resources (only needed the first time)
# nltk.download('punkt')
# nltk.download('stopwords')
# nltk.download("all")

def extract_keywords(text, top_n=5):
    words = word_tokenize(text.lower())
    stop_words = set(stopwords.words('english'))
    keywords = [w for w in words if w.isalpha() and w not in stop_words]
    return [w for w, _ in Counter(keywords).most_common(top_n)]

def generate_questions(text):
    sentences = sent_tokenize(text)
    keywords = extract_keywords(text)
    questions = []
    for kw in keywords:
        for s in sentences:
            if kw in s.lower():
                questions.append(f"What is {kw}?")
                questions.append(f"How {kw} is working?")
                break
    return questions

notes = """
Neural networks are computational models inspired by the human brain.
They consist of layers of neurons that learn representations of data.
Backpropagation is used to train neural networks.
"""

comments = """ Python is a versatile programming language that is widely used in various fields, including web development, data science, artificial intelligence, and more. It has a simple syntax that emphasizes readability and ease of use, making it a popular choice for both beginners and experienced developers. Python's extensive standard library and large ecosystem of third-party packages allow developers to accomplish a wide range of tasks efficiently. Additionally, Python supports multiple programming paradigms, including procedural, object-oriented, and functional programming, making it a flexible tool for solving complex problems.
"""

# for q in generate_questions(notes):
#     print(q)

for q in generate_questions(comments):
    print(q)

