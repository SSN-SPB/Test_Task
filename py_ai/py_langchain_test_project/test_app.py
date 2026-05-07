import re
from app import ask_llama

def test_ask_llama_returns_string():
    result = ask_llama("Why is the sky blue?")

    assert isinstance(result, str)
    assert len(result) > 0


def test_ask_llama_has_5_sentences():
    result = ask_llama("Why is the sky blue?")

    lines = [line.strip() for line in result.split("\n") if line.strip()]

    assert len(lines) == 5


def test_each_sentence_is_numbered():
    result = ask_llama("Why is the sky blue?")

    lines = [line.strip() for line in result.split("\n") if line.strip()]

    for i, line in enumerate(lines, start=1):
        assert re.match(rf"^{i}\.", line)