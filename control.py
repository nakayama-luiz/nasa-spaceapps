import requests as r
import csv
import json
import time


def red(parametro):
    vilipendiar = r.get(
        f'https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&alertlevel={parametro}')
    size = r.get(
        'https://earthquake.usgs.gov/fdsnws/event/1/count?format=geojson&alertlevel=orange').json()

    ear = json.loads(vilipendiar.text)

    tamanho = ear['metadata']['count']

    x = 0
    earthquake_data = vilipendiar.json()

# Inicializa uma lista para armazenar os dados dos terremotos
    earthquakes = []

    for feature in earthquake_data['features']:
        properties = feature['properties']
        coordinates = feature['geometry']['coordinates']
        earthquake = {
            'Magnitude': properties['mag'],
            'Place': properties['place'],
            'Latitude': coordinates[1],
            'Longitude': coordinates[0],
            'Depth': coordinates[2]
        }
        earthquakes.append(earthquake)

    csv_file_path = f'earthquake_{str(time.time())[0:10]}.csv'
    with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Magnitude', 'Place',
                      'Latitude', 'Longitude', 'Depth']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for earthquake in earthquakes:
            writer.writerow(earthquake)
