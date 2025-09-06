from mcp.server.fastmcp import FastMCP

mcp = FastMCP("WeatherTools")

@mcp.tool()
def get_weather(city: str) -> str:
    """Gets the current weather for a city."""
    # Simulate weather data; integrate a real API like OpenWeatherMap in production
    weather_data = {"new york": "Sunny, 75°F", "london": "Rainy, 60°F"}
    return weather_data.get(city.lower(), "Weather data not available")

if __name__ == "__main__":
    mcp.run(transport="streamable-http")  # Run on HTTP for this server