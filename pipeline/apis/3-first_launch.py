#!/usr/bin/env python3
"""Imports"""
if __name__ == "__main__":
    import requests

    BASE_URL = 'https://api.spacexdata.com/v4/'
    LAUNCHES_URL = BASE_URL + 'launches/upcoming'
    ROCKETS_URL = BASE_URL + 'rockets/'
    PADS_URL = BASE_URL + 'launchpads/'

    upcoming_response = requests.get(LAUNCHES_URL)
    upcoming_launches = upcoming_response.json()

    earliest_date = None
    earliest_launches = []

    for launch in upcoming_launches:
        launch_date = launch['date_local']
        if earliest_date is None or launch_date < earliest_date:
            earliest_date = launch_date
            earliest_launches = [launch]
        elif launch_date == earliest_date:
            earliest_launches.append(launch)

    for launch in earliest_launches:
        rocket_response = requests.get(ROCKETS_URL + launch['rocket'])
        rocket_data = rocket_response.json()
        rocket = rocket_data['name']

        pad_response = requests.get(PADS_URL + launch['launchpad'])
        pad_data = pad_response.json()
        pad = pad_data['name']
        locality = pad_data['locality']

        print("{} ({}) {} - {} ({})".format(
            launch['name'], launch['date_local'],
            rocket, pad, locality))
