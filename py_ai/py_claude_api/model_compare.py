import anthropic

MODELS = {
    "Haiku 4.5":  "claude-haiku-4-5-20251001",
    "Sonnet 4.6": "claude-sonnet-4-6",
    "Opus 4.7":   "claude-opus-4-7",
}


def compare(question: str, models: dict = MODELS, max_tokens: int = 1024) -> dict[str, str]:
    client = anthropic.Anthropic()
    results = {}
    for label, model_id in models.items():
        print(f"Querying {label}...")
        response = client.messages.create(
            model=model_id,
            max_tokens=max_tokens,
            messages=[{"role": "user", "content": question}],
        )
        results[label] = response.content[0].text
    return results


def print_comparison(question: str, results: dict[str, str]) -> None:
    print(f"\n{'='*70}")
    print(f"QUESTION: {question}")
    print(f"{'='*70}")
    for label, answer in results.items():
        print(f"\n--- {label} ---\n")
        print(answer)
        print()


if __name__ == "__main__":
    import sys
    question = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else input("Enter your question: ")
    results = compare(question)
    print_comparison(question, results)
