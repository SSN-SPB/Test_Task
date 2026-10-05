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

CONFIG_FILE = PROJECT_ROOT / "config" / "sitespeed.json"
REPORT_DIR = PROJECT_ROOT / "reports" / "sitespeed"


def run_sitespeed(url: str) -> subprocess.CompletedProcess:
    REPORT_DIR.mkdir(parents=True, exist_ok=True)

    command = [
        "node",
        str(SITESPEED_SCRIPT),
        "--config",
        str(CONFIG_FILE),
        "--outputFolder",
        str(REPORT_DIR),
        url,
    ]

    return subprocess.run(
        command,
        capture_output=True,
        text=True,
        check=False,
    )