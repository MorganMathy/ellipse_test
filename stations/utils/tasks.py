import asyncio
from datetime import datetime
from django.core.cache import cache

from stations.api import get_all_stations
from stations.utils.stats import calculate_statistics_per_city

async def update_statistics():
    """
    Asynchronously updates the statistics for stations.
    """
    stations = await get_all_stations()  # Fetch all stations asynchronously
    stats_per_city = calculate_statistics_per_city(stations)  # Calculate statistics per city
    cache.set('stats_per_city', stats_per_city, timeout=150) 
    cache.set('last_update', datetime.now(), timeout=150)

    return stats_per_city

asyncio.run(update_statistics())
