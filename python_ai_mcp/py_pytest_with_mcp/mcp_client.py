import json
from mcp.client.sse import sse_client
from mcp import ClientSession


class MCPClient:
    def __init__(self, base_url="http://localhost:8000/sse"):
        self.base_url = base_url

    async def call_tool(self, tool_name, args=None):
        async with sse_client(self.base_url) as (read, write):
            async with ClientSession(read, write) as session:
                await session.initialize()
                result = await session.call_tool(tool_name, arguments=args or {})
                # result.content is a list of TextContent objects
                text = result.content[0].text
                return json.loads(text)