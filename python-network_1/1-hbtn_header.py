
#!/usr/bin/python3
import requests

if __name__ == "__main__":
    url = "https://alu-intranet.hbtn.io/status"
    response = requests.get(url)
    content_type = response.headers.get('Content-Type')
    content = response.text

    print("Body response:")
    print(f"    - type: {type(content).__name__}")
    print(f"    - content: {content}")
