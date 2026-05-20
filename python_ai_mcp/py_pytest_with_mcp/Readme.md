# Target: Python AI MCP with Pytest
'''<br>
This example is useful as a learning exercise for MCP mechanics<br>
(server setup, SSE transport, client connection). <br>
But in production, you'd only reach for MCP <br>
when an AI agent needs to dynamically discover and invoke tools <br>
— not when tests call predetermined functions with fixed inputs.<br>
'''<br>


# Installation libraries
pip install mcp fastapi uvicorn pytest httpx <br>
pip install pytest-asyncio <br>

# Run
## run mcp_server integrated terminal
python mcp_server.py <br>
or (better) — run with uvicorn: <br>
uvicorn mcp_server:app --host 0.0.0.0 --port 8000<br>
<br>
### if need - to kill existing first
Option 1 — Ctrl+C in the terminal where uvicorn is running.<br>
<br>
Option 2 — Find and kill by port: <br>
netstat -ano | findstr :8000<br>
taskkill /PID <PID> /F <br>
<br>
Option 3 — Kill by process name:<br>
taskkill /IM uvicorn.exe /F <br>
<br>
## run tests in another terminal from project root directory
pytest -v .\tests\test_mcp.py<br>

