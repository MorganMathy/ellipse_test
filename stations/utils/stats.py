import plotly.graph_objects as go


def calculate_statistics_per_city(stations):
    stats_per_city = {}

    for station in stations:
        contract_name = station['contractName']
        status = station['status']
        electrical_bikes = station['totalStands']['availabilities']['electricalBikes']
        mechanical_bikes = station['totalStands']['availabilities']['mechanicalBikes']
        has_banking = station['banking']

        if contract_name not in stats_per_city:
            stats_per_city[contract_name] = {
                'electrical_bikes': electrical_bikes,
                'mechanical_bikes': mechanical_bikes,
                'stations_with_banking': 0,
                'stations_without_banking': 0,
                'open_stations': 0,
                'closed_stations': 0
            }

        stats_per_city[contract_name]['electrical_bikes'] += electrical_bikes
        stats_per_city[contract_name]['mechanical_bikes'] += mechanical_bikes

        if has_banking:
            stats_per_city[contract_name]['stations_with_banking'] += 1
        else:
            stats_per_city[contract_name]['stations_without_banking'] += 1

        if status == 'OPEN':
            stats_per_city[contract_name]['open_stations'] += 1
        else:
            stats_per_city[contract_name]['closed_stations'] += 1

    return stats_per_city


def plot_bike_distribution(stats_per_city):
    cities = []
    electrical_bikes = []
    mechanical_bikes = []

    for city, stats in stats_per_city.items():
        cities.append(city)
        electrical_bikes.append(stats['electrical_bikes'])
        mechanical_bikes.append(stats['mechanical_bikes'])

    # Créer le diagramme en barres superposées
    fig = go.Figure()
    fig.add_trace(go.Bar(x=cities, y=electrical_bikes, name='Vélos électriques'))
    fig.add_trace(go.Bar(x=cities, y=mechanical_bikes, name='Vélos mécaniques'))

    # Configurer le paramètre barmode pour superposer les barres
    fig.update_layout(barmode='stack')

    fig.update_layout(title='Répartition des vélos disponibles selon le type et la ville')

    # Ajouter des labels aux axes
    fig.update_layout(xaxis_title='Villes', yaxis_title='Nombre de vélos')

    # Convertir le diagramme en HTML
    diagram_html = fig.to_html(full_html=False)

    return diagram_html


def plot_station_status(stats_per_city):
    cities = []
    open_stations = []
    closed_stations = []

    for city, stats in stats_per_city.items():
        cities.append(city)
        open_stations.append(stats['open_stations'])
        closed_stations.append(stats['closed_stations'])

    # Créer le diagramme en barres superposées
    fig = go.Figure()
    fig.add_trace(go.Bar(x=cities, y=open_stations, name='Stations ouvertes'))
    fig.add_trace(go.Bar(x=cities, y=closed_stations, name='Stations fermées'))

    # Configurer le paramètre barmode pour superposer les barres
    fig.update_layout(barmode='stack')

    # Ajouter des labels aux axes
    fig.update_layout(xaxis_title='Villes', yaxis_title='Nombre de stations')

    # Ajouter un titre au diagramme
    fig.update_layout(title='Répartition des stations ouvertes et fermées par ville')

    # Convertir le diagramme en HTML
    diagram_html = fig.to_html(full_html=False)

    return diagram_html


def stations_with_banking_chart(stats_per_city):
    labels = ['Stations avec terminal de paiement', 'Stations sans terminal de paiement']
    values = [0, 0]

    for city_stats in stats_per_city.values():
        values[0] += city_stats['stations_with_banking']
        values[1] += city_stats['stations_without_banking']

    fig = go.Figure(data=[go.Pie(labels=labels, values=values)])

    fig.update_layout(
        title='Répartition des stations avec et sans terminal de paiement',
        showlegend=True
    )

    pie_html = fig.to_html(full_html=False)
    return pie_html