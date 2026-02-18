import requests

from Py_functionality_libs.py_ai.py_ai_assited_test_preparation.py_ai_assisted_test_tool_01_openai_02generate_testcases import \
    requirement

OLLAMA_URL = "http://localhost:11434/api/generate"

requirement = "Login should fail if password is incorrect"

def generate_tests(requirement: str) -> str:
    payload = {
        "model": "mistral",
        "prompt": f"""
You are a QA automation engineer.
Generate Pytest tests for this requirement:

{requirement}

Return ONLY Python code.
""",
        "stream": False
    }

    r = requests.post(OLLAMA_URL, json=payload, timeout=120)
    r.raise_for_status()
    return r.json()["response"]

if __name__ == "__main__":
    tests_code = generate_tests(requirement)
    print(tests_code)