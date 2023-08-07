#!/usr/bin/python3
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

class MyClass:
    """
    A sample class for demonstration purposes.

    Attributes:
        attr1 (int): The first attribute.
        attr2 (str): The second attribute.

    Methods:
        method1(): Performs task 1.
        method2(): Performs task 2.
    """

    def __init__(self, attr1, attr2):
        """
        Initializes MyClass with the given attributes.

        Args:
            attr1 (int): The value for attr1.
            attr2 (str): The value for attr2.
        """
        self.attr1 = attr1
        self.attr2 = attr2

    def method1(self):
        """
        Performs task 1.

        Args:
            None

        Returns:
            None

        Raises:
            None
        """
        pass

    def method2(self):
        """
        Performs task 2.

        Args:
            None

        Returns:
            None

        Raises:
            None
        """
        pass

def my_function():
    """
    Performs a specific task.

    Args:
        None

    Returns:
        None

    Raises:
        None
    """
    pass

if __name__ == "__main__":
    url = "https://alu-intranet.hbtn.io/status"
    body = fetch_url(url)
    print("Body response:")
    print("\t- type:", type(body))
    print("\t- content:", body)
