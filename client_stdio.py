from fastmcp import Client
from fastmcp.client.transports import (
    SSETransport, 
    PythonStdioTransport, 
    FastMCPTransport
)

async def main():
    async with Client("/Users/mahadevgaonkar/code/mcp-server/demo-1/main.py") as client:
        tools = await client.list_tools()
        print(tools)

        # Call the add tool
        result = await client.call_tool("add", {"a": 1, "b": 2})
        print(f"Result of add(1, 2): {result}")


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())