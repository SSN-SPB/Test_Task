import subprocess
import sys
import time
from pathlib import Path

import pytest
import requests

SERVER_URL = "http://127.0.0.1:5000"

SERVER_DIR = (
    Path(__file__).resolve().parent.parent / "py_web_flask_01basic"
)


@pytest.fixture(scope="session", autouse=True)
def flask_server():

    print(f"\nStarting Flask from: {SERVER_DIR}")

    process = subprocess.Popen(
        [sys.executable, "run.py"],
        cwd=SERVER_DIR,
    )

    try:
        # Wait until Flask is available
        deadline = time.time() + 10

        while time.time() < deadline:

            try:
                response = requests.get(
                    SERVER_URL,
                    timeout=1,
                )

                if response.status_code < 500:
                    print("\nFlask server is ready")
                    break

            except requests.ConnectionError:
                time.sleep(0.2)

        else:
            process.terminate()

            raise RuntimeError(
                "Flask server did not start within 10 seconds"
            )

        yield

    finally:
        print("\nStopping Flask server...")

        process.terminate()

        try:
            process.wait(timeout=5)
        except subprocess.TimeoutExpired:
            process.kill()
            process.wait()
