# pip install duckduckgo-search -q
from duckduckgo_search import DDGS


def web_search(query: str, max_results: int = 5) -> list[dict]:
    """Search the web using DuckDuckGo and return a list of results."""
    with DDGS() as ddgs:
        results = list(ddgs.text(query, max_results=max_results))
    return results


web_search_schema = {
    "name": "web_search",
    "description": "Search the web using DuckDuckGo and return a list of relevant results including title, URL, and snippet.",
    "input_schema": {
        "type": "object",
        "properties": {
            "query": {
                "type": "string",
                "description": "The search query string.",
            },
            "max_results": {
                "type": "integer",
                "description": "Maximum number of results to return.",
                "default": 5,
            },
        },
        "required": ["query"],
    },
}


def process_tool_call(tool_name: str, tool_input: dict) -> str:
    if tool_name == "web_search":
        results = web_search(
            query=tool_input["query"],
            max_results=tool_input.get("max_results", 5),
        )
        if not results:
            return "No results found."
        lines = []
        for i, r in enumerate(results, 1):
            lines.append(f"{i}. {r.get('title', 'No title')}")
            lines.append(f"   URL: {r.get('href', '')}")
            lines.append(f"   {r.get('body', '')}")
        return "\n".join(lines)
    raise ValueError(f"Unknown tool: {tool_name}")
