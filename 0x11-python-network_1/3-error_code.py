#!/usr/bin/python3
"""
Script that takes in a URL, sends a request to the URL, and displays the body
"""

import sys
from urllib import request, error

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <URL>")
        sys.exit(1)

    url = sys.argv[1]
    try:
        with request.urlopen(url) as resp:
            print(resp.read().decode('utf-8'))
    except error.HTTPError as er:
        print('Error code:', er.code)
    except error.URLError as e:
        print('URL Error:', e.reason)
