#!/usr/bin/env python3
"""Imports"""
import requests
import sys
import time


def print_user_location(api_url):
    """script that prints the location of a specific user"""
    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            user_data = response.json()
            if 'location' in user_data:
                print(user_data['location'])
            else:
                print("Location not available for this user.")
        elif response.status_code == 404:
            print("Not found")
        elif response.status_code == 403:
            reset_time = response.headers.get('X-RateLimit-Reset')
            if reset_time:
                print("Reset in {} min".format((int
                                                (reset_time) - int(time.time())) // 60))
            else:
                print("Rate limit exceeded, but reset time not provided.")
        else:
            print("Unexpected status code: {}".format(response.status_code))
    except requests.exceptions.RequestException as e:
        print("An error occurred: {}".format(e))
    except ValueError:
        print("Invalid response from server.")


if __name__ == "__main__":
    # Default URL for a GitHub user
    default_url = "https://api.github.com/users/octocat"

    api_url = sys.argv[1] if len(sys.argv) > 1 else default_url

    print_user_location(api_url)
