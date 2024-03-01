#!/usr/bin/python3
"""This script fetches data from https://alx-intranet.hbtn.io/status"""

import urllib.request
import urllib.error

def fetch_data(url):
    try:
        with urllib.request.urlopen(url) as response:
            body = response.read()
            return body.decode('utf-8')
    except urllib.error.URLError as e:
        print(f"Failed to fetch data: {e}")
        return None

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    data = fetch_data(url)
    if data is not None:
        print("Body response:")
        print(f"\t- type: {type(data)}")
        print(f"\t- content: {data}")
