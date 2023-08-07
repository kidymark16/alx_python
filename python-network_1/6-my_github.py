#!/usr/bin/env python3
"""
Sends a request to a URL and displays the value of the X-Request-Id header in the response.
"""
import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]  # GitHub username
    password = sys.argv[2]  # Personal access token

    url = "https://api.github.com/user"
    response = requests.get(url, auth=(username, password))

    if response.status_code == 200:
        user_data = response.json()
        user_id = user_data.get("id")
        print(user_id)
    else:
        print("None")
