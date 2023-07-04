import asyncio
from django.shortcuts import render
from django.views.decorators.cache import cache_page
from django.core.cache import cache
from stations.api import get_all_stations


from stations.utils.map import create_map
from stations.utils.stats import calculate_statistics_per_city, plot_bike_distribution, plot_station_status, stations_with_banking_chart

def index(request):
    # Your code here
    # Return an HttpResponse object
    return render(request, "index.html", {})

@cache_page(900)    
def map(request):
    if 'refresh' in request.GET:
        # Effacer le cache pour la vue map
        cache.clear()

    map = asyncio.run(create_map())
    context={
        'map':map
    }
    return render(request, "map.html", context)

async def stats(request):
     # Obtention des données des stations (à adapter selon votre modèle de données)
    stations = await get_all_stations()

    # Calcul des statistiques par ville
    stats_per_city = calculate_statistics_per_city(stations)

    # Génération des graphiques en HTML
    bike_distribution_html = plot_bike_distribution(stats_per_city)
    station_status_html = plot_station_status(stats_per_city)
    stations_banking_html = stations_with_banking_chart(stats_per_city)

    # Contexte à envoyer au template
    context = {
        'bike_distribution_html': bike_distribution_html,
        'station_status_html': station_status_html,
        'stations_banking_html': stations_banking_html,
    }

    return render(request, "stats.html", context)