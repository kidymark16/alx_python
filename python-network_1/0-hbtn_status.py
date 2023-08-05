#!/usr/bin/python3
import requests

if __name__ == "__main__":
    url = "https://alu-intranet.hbtn.io/status"
    response = requests.get(url)

    if response.status_code == 200:
        response_body = response.json()
        for key, value in response_body.items():
            print(f"- {key}: {value}")
    else:
        print(f"Error: {response.status_code}")
