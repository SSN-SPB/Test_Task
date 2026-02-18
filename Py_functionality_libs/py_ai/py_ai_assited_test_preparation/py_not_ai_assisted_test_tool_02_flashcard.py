notes = """
Neural networks are computational models inspired by the human brain.
They consist of layers of neurons that learn representations of data.
Backpropagation is used to train neural networks.
"""


def generate_flashcards(notes):
    sentences = notes.split(".")
    cards = []
    for s in sentences:
        if len(s.split()) > 6:
            cards.append(
                {
                    "question": f"What does this describe: '{s.strip()[:40]}...'?",
                    "answer": s.strip(),
                }
            )
    return cards


cards = generate_flashcards(notes)
for c in cards:
    print("Q:", c["question"])
    print("A:", c["answer"])
    print()
