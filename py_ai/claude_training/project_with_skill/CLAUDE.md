# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Workspace Layout

This worktree contains two independent sub-projects under `../` (the `claude_training/` parent):

| Directory | Role |
|---|---|
| `../ai_starter/` | FastMCP server exposing Python functions as tools |
| `../cli_project/` | Interactive CLI chat app integrating Claude API + MCP |

Each sub-project has its own `.venv` and `pyproject.toml`. All commands below must be run from the relevant sub-project directory.

## Commands

### ai_starter

```bash
cd ../ai_starter

# Setup
uv venv && uv pip install -e .

# Run MCP server
uv run main.py

# Run all tests
uv run pytest

# Run a single test
uv run pytest tests/test_document.py::TestBinaryDocumentToMarkdown::test_binary_document_to_markdown_with_docx
```

### cli_project

```bash
cd ../cli_project

# Setup — create .env with ANTHROPIC_API_KEY and optionally CLAUDE_MODEL
uv venv && uv pip install -e .

# Run the chat CLI
uv run main.py

# Inspect the MCP server in isolation
uv run mcp dev mcp_server.py
```

## Architecture

### ai_starter — FastMCP server

`main.py` creates a `FastMCP("docs")` instance, registers tools via `mcp.tool()(fn)`, and starts the server.

Tool modules live in `tools/`:
- `tools/math.py` — `add` tool (registered)
- `tools/document.py` — `binary_document_to_markdown` converts DOCX/PDF bytes to markdown via `markitdown` (**implemented but not yet registered**)

Tests use real binary fixtures in `tests/fixtures/` — no mocks.

To add a new tool: define it in `tools/` with `pydantic.Field` parameter descriptions and a structured docstring (summary, detail, when to use, examples), then register in `main.py`.

### cli_project — MCP Chat CLI

```
main.py          # entry point: wires Claude + MCPClient(s) + CliApp
core/
  claude.py      # Claude wrapper: chat(), add_user_message(), extended thinking support
  chat.py        # Chat base class: agentic loop (query → tool use → final answer)
  cli_chat.py    # CliChat extends Chat: handles @doc_id resources and /command prompts
  cli.py         # CliApp: prompt_toolkit UI with autocomplete for commands and resources
  tools.py       # ToolManager: discovers and executes tools across multiple MCPClients
mcp_client.py    # MCPClient: async wrapper around stdio MCP server connections
mcp_server.py    # FastMCP document server: read_document, edit_document tools
```

**Agentic loop** (`chat.py:Chat.run`): sends query → if Claude returns `tool_use` stop reason, `ToolManager.execute_tool_requests()` dispatches to the correct `MCPClient` → appends tool results → loops until end_turn.

**Multi-server setup**: `main.py` instantiates one `MCPClient` per MCP server and passes them all to `Chat`/`CliChat`. `ToolManager.get_all_tools()` aggregates tools across all clients.

**CLI features**: `@doc_id` syntax fetches document content from the MCP server and injects it into the query; `/command_name` retrieves a prompt template from the MCP server.

## Dependencies

- `mcp[cli]==1.8.0` — MCP protocol (both projects)
- `anthropic>=0.51.0` — Claude API (cli_project)
- `markitdown[docx,pdf]>=0.1.1` — document conversion (ai_starter)
- `prompt-toolkit>=3.0.51` — interactive CLI (cli_project)
- `python-dotenv>=1.1.0` — env var loading (cli_project)
- Package manager: `uv`; Python ≥ 3.10 required
