from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Demo")

@mcp.tool()
def add(a: int, b: int) -> int:
    """
    Add two integers.
    Args:
    a (int): The first integer.
    b (int): The second integer.
    Returns:
    int: The sum of the two integers.
    """
    return a + b

@mcp.resource("greetings://{name}")
def get_greetings(name: str) -> str:
    """
    Get a greeting message for the given name.
    Args:
    name (str): The name to greet.
    Returns:
    str: A greeting message.
    """
    return f"Hello, {name}!"

if __name__ == '__main__':
    # Run the FastMCP server
    # mcp.run()
    # Uncomment the following line to run the FastMCP server with a specific port
    mcp.run(port=8000)