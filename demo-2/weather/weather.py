from typing import Any
import httpx
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("weather")

# Constants
NWS_API_BASE = "https://api.weather.gov"
USER_AGENT = "weather-app/1.0"

async def make_request(url: str) -> Any:
    """
    Make a request to the National Weather Service API for weather data.
    Args:
        location (str): The location to get the weather for, in the format "latitude,longitude".
    Returns:
        Any: The JSON response from the National Weather Service API.
    """
    headers = {"User-Agent": USER_AGENT}

    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
        
@mcp.tool()
async def get_weather(location: str) -> Any:
    """
    Get the current weather for a given location.
    
    Args:
        location (str): The location to get the weather for, in the format "latitude,longitude".
    
    Returns:
        Any: The weather data from the National Weather Service API.
    """
    url = f"{NWS_API_BASE}/points/{location}"
    points_data = await make_request(url)
    forecast_url = points_data["properties"]["forecast"]
    forecast_data = await make_request(forecast_url)

    if not forecast_data:
        return {"error": "No forecast data available for this location."}

    periods = forecast_data["properties"]["periods"]
    forecasts = []
    for period in periods[:5]:
        forecast = f"""
            {period['name']}:
            Temperature: {period['temperature']}°{period['temperatureUnit']}
            Wind: {period['windSpeed']} {period['windDirection']}
            Forecast: {period['detailedForecast']}
            """
        forecasts.append(forecast.strip())

    return "\n---\n".join(forecasts)

if __name__ == "__main__":
    mcp.run(transport="stdio")