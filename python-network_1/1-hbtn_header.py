
#!/usr/bin/python3
import requests
import sys

if __name__ == "__main__":
    url = "https://intranet.hbtn.io/auth/sign_in"
    response = requests.get(url)
    content = response.text

    print(content)

