#!/usr/bin/env python3
"""Imports"""
if __name__ == "__main__":
    import requests
    from collections import Counter
    
    LAUNCH_URL = 'https://api.spacexdata.com/v5/launches'
    ROCKET_URL = 'https://api.spacexdata.com/v4/rockets'

    # Function to retrieve rocket names from IDs
    def get_rocket_name(rocket_id):
        rocket_response = requests.get(f"{ROCKET_URL}/{rocket_id}")
        rocket_data = rocket_response.json()
        return rocket_data['name'] if 'name' in rocket_data else "Unknown Rocket"

    launch_response = requests.get(LAUNCH_URL)
    launch_data = launch_response.json()

    # Extract rocket names and count launches per rocket
    rocket_launch_counts = Counter(get_rocket_name(launch['rocket']) for launch in launch_data)

    sorted_result = sorted(rocket_launch_counts.items(),
                           key=lambda x: (-x[1], x[0]))

    # Print the results without using f-strings
    for rocket_name, launch_count in sorted_result:
        print("{}: {}".format(rocket_name, launch_count))
