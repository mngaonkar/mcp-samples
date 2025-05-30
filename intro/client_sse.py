from fastmcp  import Client
from fastmcp.client.transports import (
    SSETransport, 
    PythonStdioTransport, 
    FastMCPTransport
)

async def main():
    try:
        async with Client("http://localhost:8000/sse") as client:
            print("Client connected to server.")
            tools = await client.list_tools()
            print(tools)

            # Call the add tool
            result = await client.call_tool("add", {"a": 1, "b": 2})
            print(f"Result of add(1, 2): {result}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())