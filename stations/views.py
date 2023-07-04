import asyncio
from django.shortcuts import render
from django.views.decorators.cache import cache_page


from stations.utils.map import create_map

def index(request):
    # Your code here
    # Return an HttpResponse object
    return render(request, "index.html", {})
    
@cache_page(3600)
def map(request):
    map = asyncio.run(create_map())
    context={
        'map':map
    }
    return render(request, "map.html", context)

def stats(request):
    # Your code here
    # Return an HttpResponse object
    return render(request, "stats.html", {})