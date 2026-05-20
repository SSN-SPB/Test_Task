from mcp.server.fastmcp import FastMCP

mcp = FastMCP("TestAutomationServer")

# Tool 1: Generate test data
@mcp.tool()
def generate_user_data():
    return {
        "username": "test_user",
        "email": "test@example.com"
    }

# Tool 2: Validate API response
@mcp.tool()
def validate_status_code(actual: int, expected: int):
    return {
        "valid": actual == expected,
        "actual": actual,
        "expected": expected
    }

# Tool 3: fake API simulation
@mcp.tool()
def mock_api_call():
    return {
        "status": 200,
        "data": {"message": "success"}
    }

app = mcp.sse_app()

if __name__ == "__main__":
    mcp.run()