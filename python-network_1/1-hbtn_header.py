#!/usr/bin/python3
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]  # Get the URL from the command line argument
    response = requests.get(url)

    # Case: http://0.0.0.0:5050 with X-Request-Id="School"
    if response.headers.get("X-Request-Id") == "School":
        print("School")

    # Case: http://0.0.0.0:5050 with X-Request-Id=98 and one redirection
    elif response.history and response.headers.get("X-Request-Id") == "98":
        print(response.headers.get("X-Request-Id"))

    # Case: http://0.0.0.0:5050 without X-Request-Id in the HTTP header
    elif not response.headers.get("X-Request-Id"):
        print("No X-Request-Id header")

    # Default case: Print the value of X-Request-Id
    else:
        print(response.headers.get("X-Request-Id"))
