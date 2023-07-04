import os
import aiohttp

from dotenv import load_dotenv



# Load environment variables from .env file
load_dotenv()

# Get the API key from environment variables
api_key = os.getenv("API_KEY")

# Base URL for the API
API_URL = "https://api.jcdecaux.com/vls/v3"


async def get_contracts():
    """
    Fetches the list of available contracts.

    Returns:
        List: A list of contracts.
    """
    url = f"{API_URL}/contracts"
    params = {"apiKey": api_key}

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, params=params) as response:
                contracts = await response.json()

        return contracts
    except Exception as e:
        # Handle exceptions and log the error
        print("Error fetching contracts:", str(e))
        return []

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

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, params=params) as response:
                stations = await response.json()

        return stations
    except Exception as e:
        # Handle exceptions and log the error
        print(f"Error fetching stations for contract {contract_name}:", str(e))
        return []


async def get_all_stations():
    """
    Fetches the list of all stations.

    Returns:
        List: A list of all stations.
    """
    url = f"{API_URL}/stations"
    params = {"apiKey": api_key}

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, params=params) as response:
                stations = await response.json()

        return stations
    except Exception as e:
        # Handle exceptions and log the error
        print("Error fetching all stations:", str(e))
        return []


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

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, params=params) as response:
                station_details = await response.json()

        return station_details
    except Exception as e:
        # Handle exceptions and log the error
        print(f"Error fetching details for station {station_id} in contract {contract_name}:", str(e))
        return {}
