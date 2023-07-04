import asyncio
from django.shortcuts import render
from django.core.cache import cache
from django.views.decorators.cache import cache_page

from stations.api import get_all_stations
from stations.utils.map import create_map
from stations.utils.stats import calculate_statistics_per_city, plot_bike_distribution, plot_station_status, plot_stations_with_banking

def index(request):
    return render(request, "index.html", {})


@cache_page(900) # Set the cache to 15 minutes (900 seconds) for improved performance
def map(request):
    if 'refresh' in request.GET:
        # Clear the cache for the map view
        cache.clear()

    map = asyncio.run(create_map())
    context={
        'map':map
    }
    return render(request, "map.html", context)

async def stats(request):
    # Get station data
    stations = await get_all_stations()

    # Calculate statistics per city
    stats_per_city = calculate_statistics_per_city(stations)

    # Generate HTML charts
    bike_distribution_html = plot_bike_distribution(stats_per_city)
    station_status_html = plot_station_status(stats_per_city)
    stations_banking_html = plot_stations_with_banking(stats_per_city)

    # Context to be sent to the template
    context = {
        'bike_distribution_html': bike_distribution_html,
        'station_status_html': station_status_html,
        'stations_banking_html': stations_banking_html,
    }

    return render(request, "stats.html", context)