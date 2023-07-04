import folium
from folium.plugins import MarkerCluster
from dateutil import parser
from django.views.decorators.cache import cache_page
from stations.api import get_all_stations


async def create_map():
    map = folium.Map(location=[46.603354, 1.888334], zoom_start=5)
    marker_cluster = MarkerCluster()
    stations = await get_all_stations()
    for station in stations:
        marker = create_marker(station)
        marker_cluster.add_child(marker)
    map.add_child(marker_cluster)
    map = map._repr_html_()
    return map

def create_marker(station):
    name = station['name']
    if station['status'] == 'OPEN':
        available = 'Station Ouverte'
        marker_color = 'green'
    else:
        available = 'Station fermée'
        marker_color = 'red'
    position = station['position']
    latitude = position['latitude']
    longitude = position['longitude']
    electrical_bikes_availables = station['totalStands']['availabilities']['electricalBikes']
    mechanical_bikes_availables = station['totalStands']['availabilities']['mechanicalBikes']
    free_stands = station['totalStands']['availabilities']['stands']
    last_update = station['lastUpdate']

    popup_content = f"<h4>Station: {name}</h4>" \
                    f"<p>{available}</p>" \
                    f"<p>Vélo(s) électrique(s) disponible(s): {electrical_bikes_availables}</p>" \
                    f"<p>Vélo(s) mécanique(s) disponible(s): {mechanical_bikes_availables}</p>" \
                    f"<p>Emplacement(s) disponible(s): {free_stands}" \
                    

    if station['banking']: 
        popup_content += f"<p>Terminal de paiement électronique</p>"     
    if station['bonus']:
        popup_content += f"<p>Station bonus !</p>"
    
    formatted_time = ""

    if last_update is not None:
        parsed_time = parser.parse(last_update)
        formatted_time = parsed_time.strftime("%d/%m/%Y %H:%M:%S")
        popup_content += f"<p>Dernière mise à jour : {formatted_time}" \

    popup = folium.Popup(popup_content, max_width="300")

    marker = folium.Marker([latitude, longitude], popup=popup, icon=folium.Icon(color=marker_color))
    return marker

