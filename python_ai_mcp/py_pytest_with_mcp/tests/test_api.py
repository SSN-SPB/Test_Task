import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest
from mcp_client import MCPClient

client = MCPClient()


@pytest.mark.asyncio
async def test_api_success():
    # Step 1: Call MCP to simulate API
    api_response = await client.call_tool("mock_api_call")

    # Step 2: Validate response via MCP tool
    validation = await client.call_tool(
        "validate_status_code",
        {"actual": api_response["status"], "expected": 200}
    )

    assert validation["valid"] is True


@pytest.mark.asyncio
async def test_user_data_generation():
    # Use MCP to generate test data
    user = await client.call_tool("generate_user_data")

    assert "username" in user
    assert "email" in user