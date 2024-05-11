from typing import Literal
import requests


def get(url: str) -> Literal['<Response [200]>']:
    return "<Response [200]>"


def make_request(url, mock=False):
    if mock:
        requests.get = get

    return requests.get(url)


if __name__ == "__main__":
    url = "http://www.google.com"
    print(make_request(url, mock=True))
