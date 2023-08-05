import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]  # URL received as the command-line argument

    response = requests.get(url)

    if response.status_code >= 400:
        print("Error code:", response.status_code)
    else:
        print(response.text)
