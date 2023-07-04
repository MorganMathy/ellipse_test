import plotly.graph_objects as go


def calculate_statistics_per_city(stations):
    """
    Calculates statistics per city based on the station data.

    Args:
        stations (List[Dict]): List of station data.

    Returns:
        Dict: Statistics per city.
    """
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


def create_bar_chart(x_values, y_values, bar_names, title, xaxis_title, yaxis_title):
    """
    Creates a bar chart using Plotly.

    Args:
        x_values (List): List of x-axis values.
        y_values (List): List of y-axis values.
        bar_names (List): List of names for each bar.
        title (str): Chart title.
        xaxis_title (str): x-axis label.
        yaxis_title (str): y-axis label.

    Returns:
        str: HTML representation of the chart.
    """
    fig = go.Figure()
    for x, y, name in zip(x_values, y_values, bar_names):
        fig.add_trace(go.Bar(x=x, y=y, name=name))

    fig.update_layout(barmode='stack')
    fig.update_layout(title=title)
    fig.update_layout(xaxis_title=xaxis_title, yaxis_title=yaxis_title)

    chart_html = fig.to_html(full_html=False)

    return chart_html


def plot_bike_distribution(stats_per_city):
    """
    Plots the bike distribution per city.

    Args:
        stats_per_city (Dict): Statistics per city.

    Returns:
        str: HTML representation of the chart.
    """
    cities = []
    electrical_bikes = []
    mechanical_bikes = []
    
    for city, stats in stats_per_city.items():
        cities.append(city)
        electrical_bikes.append(stats['electrical_bikes'])
        mechanical_bikes.append(stats['mechanical_bikes'])

    chart_html = create_bar_chart(
        x_values=[cities, cities],
        y_values=[electrical_bikes, mechanical_bikes],
        bar_names=['Vélos électriques', 'Vélos mécaniques'],
        title='Répartition des vélos disponibles selon le type et la ville',
        xaxis_title='Villes',
        yaxis_title='Nombre de vélos'
    )

    return chart_html


def plot_station_status(stats_per_city):
    """
    Plots the station status (open/closed) per city.

    Args:
        stats_per_city (Dict): Statistics per city.

    Returns:
        str: HTML representation of the chart.
    """
    cities = []
    open_stations = []
    closed_stations = []

    for city, stats in stats_per_city.items():
        cities.append(city)
        open_stations.append(stats['open_stations'])
        closed_stations.append(stats['closed_stations'])

    chart_html = create_bar_chart(
        x_values=[cities, cities],
        y_values=[open_stations, closed_stations],
        bar_names=['Stations ouvertes', 'Stations fermées'],
        title='Répartition des stations ouvertes et fermées par ville',
        xaxis_title='Villes',
        yaxis_title='Nombre de stations'
    )

    return chart_html


def plot_stations_with_banking(stats_per_city):
    """
    Plots the distribution of stations with and without banking per city.

    Args:
        stats_per_city (Dict): Statistics per city.

    Returns:
        str: HTML representation of the chart.
    """
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

    chart_html = fig.to_html(full_html=False)
    return chart_html
