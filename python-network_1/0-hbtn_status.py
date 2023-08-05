#!/usr/bin/python3
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]  # Get the URL from the command line argument
    response = requests.get(url)
    request_id = response.headers.get('X-Request-Id')  # Retrieve the value of the X-Request-Id header

    print(request_id)
