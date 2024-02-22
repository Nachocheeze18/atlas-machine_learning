#!/usr/bin/env python3
"""Imports"""
import requests

API_ROOT = "https://swapi-api.alx-tools.com/api/"

def sentientPlanets():
    """
    Returns:
        list of planets that are home to sentient species
    """
    planet_list = []
    page =   1

    while True:
        response = requests.get(f"{API_ROOT}species/?page={page}")
        if response.status_code !=   200:
            print("Error fetching species data:", response.status_code)
            break

        species_data = response.json()
        if not species_data['next']:
            break

        for species in species_data['results']:
            # Check if 'species_classification' key exists and is 'sentient'
            if 'species_classification' in species and species['species_classification'] == 'sentient' and species['homeworld']:
                planet_response = requests.get(species['homeworld'])
                if planet_response.status_code ==   200:
                    planet_data = planet_response.json()
                    planet_list.append(planet_data['name'])
                else:
                    print("Error fetching planet data:", planet_response.status_code)

        page +=   1

    return (planet_list)