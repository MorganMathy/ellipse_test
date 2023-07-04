# Ellipse Test

This test project has been developed as part of an application for an internship or apprenticeship with Ellipse. The project aims to showcase my development skills and familiarity with the technologies (python) used at Ellipse.

## Project Description

The project is a Python-based application that displays a real-time map of bike stations along with statistics related to these bike stations. It leverages various Python scripts and libraries to gather data about bike stations and present it in an interactive and informative manner.

Key Features:

Real-time bike station data: The application fetches live data about bike stations, including their locations and availability.
Interactive map visualization: The data is displayed on an interactive map, allowing users to explore bike stations and their details.
Statistical analysis: The application calculates and presents statistics based on the bike station data, such as station usage, bike availability, and more.

## Technologies used
The project utilizes the following technologies:

- Python: A versatile programming language used for scripting and data analysis.
- Django: A high-level Python web framework for developing web applications.
- Folium: A Python library for visualizing geospatial data on interactive maps.
- dotenv: A Python library for managing environment variables.
- Other relevant libraries and frameworks as required.


## Setup Instructions
To set up the project locally, follow these steps:

### 1. Clone the repository

```bash
git clone git@github.com:MorganMathy/ellipse_test.git
cd ellipse_test/
```

### 2. Create a virtual environment (optional but recommended): 
```bash
python3 -m venv env and activate it.
```

### 3. Install dependencies: 
```bash
pip install -r requirements.txt
```

### 4. Configure the environment variables: 
Create a .env file and set necessary API key for JCDecaux.
```bash
touch .env
```
Open the .env file in a text editor, and add the following line to the file:
```plaintext
API_KEY=<your-api-key>
```

### 5. Run the application:
Start the server :
```bash
python manage.py runserver
```

And finally access the application: Open your web browser and visit http://localhost:8000 to view the real-time map and statistics.