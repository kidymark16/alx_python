#!/usr/bin/python3
import requests
import sys


if __name__ == "__main__":
    url = "https://intranet.hbtn.io/status"
    response = requests.get(url)
    content = response.content
    utf8_content = content.decode("utf-8")

    print("Body response:")
    print("- type:", type(content))
    print("- content:", content)
    print("- utf8 content:", utf8_content)
