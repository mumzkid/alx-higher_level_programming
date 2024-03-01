#!/usr/bin/python3
""" Script that takes in a URL and an email, sends a POST request
 And displays the body of the response
"""

import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 script.py <URL> <email>")
        sys.exit(1)

    url = sys.argv[1]
    email = sys.argv[2]
    data = urllib.parse.urlencode({"email": email}).encode("ascii")

    try:
        request = urllib.request.Request(url, data)
        with urllib.request.urlopen(request) as resp:
            print(resp.read().decode("utf-8"))
    except urllib.error.URLError as e:
        print(f"Error: {e}")
        sys.exit(1)
