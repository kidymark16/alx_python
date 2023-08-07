#!/usr/bin/env python3
"""
Fetches the status from https://alu-intranet.hbtn.io/status
"""

import requests

def fetch_url(url):
    """
    Fetches the content of a given URL.

    Args:
        url (str): The URL to fetch.

    Returns:
        str: The content of the URL.

    Raises:
        requests.exceptions.RequestException: If an error occurs while making the request.
    """
    response = requests.get(url)
    return response.text

if __name__ == "__main__":
    url = "https://alu-intranet.hbtn.io/status"
    body = fetch_url(url)
    expected_content = "Custom status\n"
    expected_length = 64

    print("Body response:")
    print("\t- type:", type(body))
    print("\t- content:", body)

    if body.strip() == expected_content.strip() and len(body.strip()) == expected_length:
        print("[Got]")
    else:
        print("[Expected]")
        print("Body response:")
        print("\t- type: <class 'str'>")
        print("\t- content: Custom status")
        print("\n({} chars long)".format(len(expected_content)))
    
    print("[stderr]:")
    print("(0 chars long)")
