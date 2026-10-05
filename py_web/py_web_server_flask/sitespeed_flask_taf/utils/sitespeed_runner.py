import subprocess
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent.parent

SITESPEED_SCRIPT = (
    PROJECT_ROOT
    / "node_modules"
    / "sitespeed.io"
    / "bin"
    / "sitespeed.js"
)


def run_sitespeed(url: str) -> subprocess.CompletedProcess:
    command = [
        "node",
        str(SITESPEED_SCRIPT),
        url,
        "-b",
        "chrome",
        "-n",
        "1",
    ]

    return subprocess.run(
        command,
        capture_output=True,
        text=True,
        check=False,
    )