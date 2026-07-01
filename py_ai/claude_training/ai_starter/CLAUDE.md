# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

```bash
# Create and activate virtual environment
uv venv
.venv\Scripts\activate        # Windows
source .venv/bin/activate     # Linux/macOS

# Install package in development mode
uv pip install -e .

# Start the MCP server
uv run main.py

# Run all tests
uv run pytest

# Run a single test file
uv run pytest tests/test_document.py

# Run a single test by name
uv run pytest tests/test_document.py::TestBinaryDocumentToMarkdown::test_binary_document_to_markdown_with_docx
```

## Architecture

This is a **FastMCP server** that exposes Python functions as tools to LLM interfaces (e.g., Claude Desktop).

**Entry point**: `main.py` creates a `FastMCP` instance named `"docs"`, registers tools via `mcp.tool()(function)`, and runs the server.

**Tool modules** live in `tools/`:
- `tools/math.py` — example `add` tool, registered in `main.py`
- `tools/document.py` — `binary_document_to_markdown` converts binary DOCX/PDF data to markdown via `markitdown`; currently implemented but **not yet registered** with the MCP server

**Tests** are in `tests/` with real binary fixture files (`tests/fixtures/mcp_docs.docx`, `mcp_docs.pdf`) — no mocks.

## Adding a New Tool

1. Define the function in `tools/` using `pydantic.Field` for parameter descriptions
2. Write a docstring with: one-line summary, detailed explanation, when to use/not use, and input/output examples
3. Register it in `main.py` with `mcp.tool()(my_function)`

Tool docstring structure:
```python
from pydantic import Field

def my_tool(
    param: str = Field(description="What this param does")
) -> str:
    """One-line summary.

    Detailed explanation of what this does, when to use it,
    when NOT to use it, and example input/output.
    """
```
