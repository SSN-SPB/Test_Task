# Target: Python AI MCP with Pytest

| Section     | Details |
|-------------|---------|
| **Purpose** | Learning exercise for MCP mechanics (server setup, SSE transport, client connection) |
| **Note**    | In production, MCP is used when an AI agent needs to dynamically discover and invoke tools — not for predetermined function calls with fixed inputs |
| **Idea**    | Pytest → MCP Client → MCP Server → Tools (APIs, DB, logic) |

## Where MCP Actually Adds Value

| Scenario | Why MCP Helps |
|----------|---------------|
| AI agent selects tools dynamically | LLM discovers available tools at runtime via protocol |
| Multiple consumers share tools | One MCP server serves IDE extensions, chatbots, test harnesses |
| Tool composition across systems | Standardized protocol replaces custom integrations |
| Remote/distributed tool execution | Tools run on a different machine/service |


# Installation libraries
pip install mcp fastapi uvicorn pytest httpx <br>
pip install pytest-asyncio <br>

# Run
## run mcp_server integrated terminal
python mcp_server.py <br>
or (better)
## Run MCP Server and Tests

| Terminal | Task                                  | Command                                             |
|----------|---------------------------------------|-----------------------------------------------------|
| 1        | Start MCP server in separate terminal | `uvicorn mcp_server:app --host 0.0.0.0 --port 8000` |
| 1a       | Start MCP server via docker           | docker build -t mcp-server . <br> docker run -p 8000:8000 mcp-server                  |
| 2        | Check server status                   | `http://localhost:8000/sse`                         |
| 3        | Run tests                             | `pytest -v tests/test_api.py`                       |

## Stop the Server

| Option | Command |
|--------|---------|
| Option 1 | Press `Ctrl+C` in the terminal |
| Option 2 (by port) | `netstat -ano \| findstr :8009` then `taskkill /PID <PID> /F` |
| Option 3 (by process) | `taskkill /IM python.exe /F` |

## Project Structure

| File | Purpose |
|------|---------|
| `mcp_server.py` | MCP server with registered tools and custom HTTP endpoint |
| `tests/test_api.py` | Pytest tests for MCP tools |
| `requirements.txt` | Project dependencies |
| `pyproject.toml` | Project configuration and build settings |

