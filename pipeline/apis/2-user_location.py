#!/usr/bin/env python3
"""Imports"""
import requests
import sys
import time


def print_user_location(api_url):
    """script that prints the location of a specific user"""
    response = requests.get(api_url)
    user_data = response.json()

    if response.status_code ==  200:
        print(user_data['location'])
    elif response.status_code ==  404:
        print("Not found")
    elif response.status_code ==  403:
        reset_time = response.headers['X-RateLimit-Reset']
        print(f"Reset in {(int(reset_time) - int(time.time())) //  60} min")

if __name__ == "__main__":
    if len(sys.argv) !=  2:
        print("Usage: ./2-user_location https://api.github.com/users/<user>")
        sys.exit(1)

    print_user_location(sys.argv[1])