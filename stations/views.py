from django.http import HttpResponse
from django.shortcuts import render
import folium

def index(request):
    # Your code here
    # Return an HttpResponse object
    return render(request, "index.html", {})
    

def map(request):
    map1 = folium.Map(location=[46.603354, 1.888334],  zoom_start=5)
    map1 = map1._repr_html_()
    context={
        'map1':map1
    }
    return render(request, "map.html", context)

def stats(request):
    # Your code here
    # Return an HttpResponse object
    return render(request, "stats.html", {})