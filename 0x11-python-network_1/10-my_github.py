#!/usr/bin/python3
"""
Takes your GitHub credentials (username and personal access token)
and uses the GitHub API to display your id.
"""

import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]

    url = "https://api.github.com/user"
    auth = (username, password)

    response = requests.get(url, auth=auth)

    if response.status_code == 200:
        print(response.json().get('id'))
    else:
        print(None)
