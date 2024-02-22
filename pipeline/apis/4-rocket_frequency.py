#!/usr/bin/env python3
"""Imports"""
if __name__ == "__main__":
    import requests
    from collections import Counter

    # Assuming v5 API provides both launches and rocket information
    LAUNCH_URL = 'https://api.spacexdata.com/v5/launches'

    # Fetch launch data
    launch_response = requests.get(LAUNCH_URL)
    launch_data = launch_response.json()

    # Extract rocket names and count launches per rocket
    rocket_launch_counts = Counter(launch['rocket'] for launch in launch_data)

    # Sort the results by the number of launches, in descending order
    sorted_result = sorted(rocket_launch_counts.items(), key=lambda x: (-x[1], x[0]))

    # Print the results
    for rocket_name, launch_count in sorted_result:
        print(f"{rocket_name}: {launch_count}")
