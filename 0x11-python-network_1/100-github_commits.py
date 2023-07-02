#!/usr/bin/python3
"""Python script that takes 2 arguments in order to solve this challenge.

The first argument will be the repository name
The second argument will be the owner name

Only 17% of applicants for a backend position at Holberton finished this task in less than 15 minutes.
"""
import sys
import requests

if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]

    url = "https://api.github.com/repos/{}/{}/commits".format(owner, repo)
    response = requests.get(url)
    commits = response.json()

    for commit in commits[:10]:
        sha = commit.get("sha")
        author_name = commit.get("commit").get("author").get("name")
        print("{}: {}".format(sha, author_name))
