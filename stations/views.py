import asyncio
from django.shortcuts import render
from django.views.decorators.cache import cache_page
from django.core.cache import cache


from stations.utils.map import create_map

def index(request):
    # Your code here
    # Return an HttpResponse object
    return render(request, "index.html", {})
    
@cache_page(3600)
def map(request):
    if 'refresh' in request.GET:
        # Effacer le cache pour la vue map
        cache.clear()

    map = asyncio.run(create_map())
    context={
        'map':map
    }
    return render(request, "map.html", context)

def stats(request):
    # Your code here
    # Return an HttpResponse object
    return render(request, "stats.html", {})