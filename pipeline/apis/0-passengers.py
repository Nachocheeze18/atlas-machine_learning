#!/usr/bin/env python3
"""Imports"""
import requests
API_ROOT = "https://swapi-api.alx-tools.com/api/"


def availableShips(passengerCount):
    """Returns a list of starships that can hold the given number of passengers."""
    page =  1
    ships_list = []

    response = requests.get(API_ROOT + 'starships/?page={}'.format(page))
    starships_data = response.json()

    while starships_data['next']:
        for starship in starships_data['results']:
            if starship['passengers'] == 'n/a' or starship['passengers'] == 'unknown':
                continue
            if int(starship['passengers'].replace(',', '')) >= passengerCount:
                ships_list.append(starship['name'])
        page +=  1
        response = requests.get(API_ROOT + 'starships/?page={}'.format(page))
        starships_data = response.json()

    return ships_list
