#!/usr/bin/env python3
"""Imports"""
if __name__ == "__main__":
    import requests

    BASE_URL = 'https://api.spacexdata.com/v4/'
    LAUNCHES_URL = BASE_URL + 'launches/upcoming'
    ROCKETS_URL = BASE_URL + 'rockets/'
    PADS_URL = BASE_URL + 'launchpads/'

    # Fetch upcoming launches
    upcoming_response = requests.get(LAUNCHES_URL)
    upcoming_launches = upcoming_response.json()

    # Find the upcoming launch with the earliest date
    min_launch = min(upcoming_launches, key=lambda l: l['date_local'])

    # Fetch rocket and launchpad details
    rocket_response = requests.get(ROCKETS_URL + min_launch['rocket'])
    rocket_data = rocket_response.json()
    rocket = rocket_data['name']

    pad_response = requests.get(PADS_URL + min_launch['launchpad'])
    pad_data = pad_response.json()
    pad = pad_data['name']
    locality = pad_data['locality']

    # Print the details of the upcoming launch
    print("{} ({}) {} - {} ({})".format(min_launch['name'], min_launch['date_local'], rocket, pad, locality))
