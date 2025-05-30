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


@mcp.resource("movie://data")
async def weather_data() -> dict:
    return {"name": "Pulp Fiction", "year": 1994, "director": "Quentin Tarantino"}

@mcp.prompt()
async def user_query_template() -> str:
    return "Generate a SQL query to retrieve user data from a table named 'users' with columns 'id', 'name', and 'email' where {condition}."

if __name__ == '__main__':
    # Run the FastMCP server
    mcp.run()