#!/usr/bin/env/python3
"""imports"""
import requests
API_ROOT = "https://swapi-api.alx-tools.com/api/"


def sentientPlanets():
    """list of planets that are home to sentient species"""
    page =  1
    species_planet_urls = []

    while True:
        response = requests.get(f'{API_ROOT}species/?page={page}')
        if response.status_code !=  200:
            break
        species_data = response.json()
        species_planet_urls.extend(
            [species['homeworld'] for species in species_data['results']
             if species.get('designation') == 'sentient' or species.get('classification') == 'sentient']
        )
        if not species_data['next']:
            break
        page +=  1

    planet_list = [
        requests.get(url).json()['name'] for url in species_planet_urls if url is not None
    ]

    return planet_list
