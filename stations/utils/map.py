import folium
from folium.plugins import MarkerCluster
from dateutil import parser

from stations.api import get_all_stations


async def create_map():
    """
    Creates a map with station markers.

    Returns:
        str: HTML representation of the map.
    """
    # Create a folium map object with initial location and zoom level
    map = folium.Map(location=[46.603354, 1.888334], zoom_start=5)
    
    # Create a marker cluster for better marker management
    marker_cluster = MarkerCluster()

    # Get station data
    stations = await get_all_stations()

    # Add markers for each station
    for station in stations:
        marker = create_marker(station)
        marker_cluster.add_child(marker)

    # Add marker cluster to the map
    map.add_child(marker_cluster)

    # Get the HTML representation of the map
    map_html = map._repr_html_()
    return map_html


def create_marker(station):
    """
    Creates a marker for a station.

    Args:
        station (dict): Station data.

    Returns:
        folium.Marker: Marker object.
    """
    name = station['name']
    
    # Determine the availability status and marker color
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

    # Create the content for the popup
    popup_content = f"<h4>Station: {name}</h4>" \
                    f"<p>{available}</p>" \
                    f"<p>Vélo(s) électrique(s) disponible(s): {electrical_bikes_availables}</p>" \
                    f"<p>Vélo(s) mécanique(s) disponible(s): {mechanical_bikes_availables}</p>" \
                    f"<p>Emplacement(s) disponible(s): {free_stands}"
    
    # Add additional information if available
    if station['banking']:
        popup_content += f"<p>Terminal de paiement électronique</p>"
    if station['bonus']:
        popup_content += f"<p>Station bonus !</p>"

    # Format and add last update time if available
    formatted_time = ""
    if last_update is not None:
        parsed_time = parser.parse(last_update)
        formatted_time = parsed_time.strftime("%d/%m/%Y %H:%M:%S")
        popup_content += f"<p>Dernière mise à jour : {formatted_time}"

    # Create a folium Popup object with the popup content
    popup = folium.Popup(popup_content, max_width="300")

    # Create a folium Marker object with position, popup, and custom icon
    marker = folium.Marker([latitude, longitude], popup=popup, icon=folium.Icon(color=marker_color))
    return marker
