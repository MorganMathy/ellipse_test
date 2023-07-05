import asyncio
from datetime import datetime
from django.shortcuts import redirect, render
from django.core.cache import cache
from django.views.decorators.cache import cache_page


from stations.utils.map import create_map
from stations.utils.stats import plot_bike_distribution, plot_station_status, plot_stations_with_banking
from stations.utils.tasks import update_statistics

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
    # Calculate statistics per city
    stats_per_city = cache.get('stats_per_city')
    last_update = cache.get('last_update')

    if stats_per_city is None or last_update is None:
        await update_statistics()
        last_update = cache.get('last_update')
        stats_per_city = cache.get('stats_per_city')

    # Generate HTML charts
    bike_distribution_html = plot_bike_distribution(stats_per_city)
    station_status_html = plot_station_status(stats_per_city)
    stations_banking_html = plot_stations_with_banking(stats_per_city)
    # Context to be sent to the template
    context = {
        'bike_distribution_html': bike_distribution_html,
        'station_status_html': station_status_html,
        'stations_banking_html': stations_banking_html,
        'last_update': last_update,
    }

    return render(request, "stats.html", context)

from django.shortcuts import redirect, render

async def update_stats_endpoint(request):
    """
    Handles the update statistics endpoint.
    If accessed via POST request, it calls the `update_statistics()` function asynchronously,
    and optionally redirects to the stats page.
    If accessed via GET request, it renders the stats page.
    """
    if request.method == 'POST':
        # Call the update_statistics() function here
        await update_statistics()

        # Optionally, redirect to the stats page 
        return redirect('stats')

    # Render the stats page if accessed via GET request
    return render(request, 'stats.html')
