import os
import aiohttp
import datetime
from dotenv import load_dotenv
from django.core.cache import cache
from django.views.decorators.cache import cache_page

# Load environment variables from .env file
load_dotenv()

# Get the API key from environment variables
api_key = os.getenv("API_KEY")

# Base URL for the API
API_URL = "https://api.jcdecaux.com/vls/v3"
CACHE_KEY = "stations_data"


async def get_contracts():
    """
    Fetches the list of available contracts.

    Returns:
        List: A list of contracts.
    """
    url = f"{API_URL}/contracts"
    params = {"apiKey": api_key}

    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params) as response:
            contracts = await response.json()

    return contracts


async def get_stations_from_contract(contract_name):
    """
    Fetches the list of stations for a specific contract.

    Args:
        contract_name (str): The name of the contract.

    Returns:
        List: A list of stations for the specified contract.
    """
    url = f"{API_URL}/stations"
    params = {"apiKey": api_key, "contract": contract_name}

    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params) as response:
            stations = await response.json()

    return stations


async def get_all_stations():
    """
    Fetches the list of all stations.

    Returns:
        List: A list of all stations.
    """    
    url = f"{API_URL}/stations"
    params = {
        "apiKey": api_key,
    }

    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params) as response:
            stations = await response.json()

    return stations


async def get_station_details(contract_name, station_id):
    """
    Fetches the details of a specific station.

    Args:
        contract_name (str): The name of the contract.
        station_id (str): The ID of the station.

    Returns:
        Dict: The details of the specified station.
    """
    url = f"{API_URL}/stations/{station_id}"
    params = {"apiKey": api_key, "contract": contract_name}

    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params) as response:
            station_details = await response.json()

    return station_details
