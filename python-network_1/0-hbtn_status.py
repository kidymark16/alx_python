#!/usr/bin/python3
# my_module.py
import requests

if __name__ == "__main__":
    url = "https://alu-intranet.hbtn.io/status"
    response = requests.get(url)

    print("Body response:$")
    print("\t- type: <class 'str'>$")
    print("\t- content:", response.text + "$")
