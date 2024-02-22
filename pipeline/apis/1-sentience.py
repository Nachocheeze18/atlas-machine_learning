#!/usr/bin/env python3
"""Imports"""
import requests
API_ROOT = "https://swapi-api.alx-tools.com/api/"


def sentientPlanets():
    """Returns a list of planets that are home to sentient species"""
    page = 1
    species_planet_urls = []

    while True:
        response = requests.get(API_ROOT + 'species/?page={}'.format(page))
        species_data = response.json()

        for species in species_data['results']:
            if (species['designation'] == 'sentient' or
                    species['classification'] == 'sentient'):
                species_planet_urls.extend([species['homeworld']])

        if species_data['next']:
            page += 1
        else:
            break

    planet_list = []

    for url in species_planet_urls:
        if url is not None:
            response = requests.get(url)
            planet_data = response.json()
            planet_list.append(planet_data['name'])

    return planet_list
