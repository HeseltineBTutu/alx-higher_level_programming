#!/usr/bin/python3
"""
a Python script that evaluates candidates applying for a
back-end position with multiple technical challenges
"""

import requests
import sys


def get_repo_commits(repo_name, owner_name):
    """Fetches and prints the 10 most recent commits of a GitHub repository.

    Args:
        repo_name (str): The name of the repository.
        owner_name (str): The owner's username.
    """

    url = (f"https://api.github.com/repos/{owner_name}/"
           f"{repo_name}/commits?per_page=10")
    response = requests.get(url)

    if response.status_code == 200:
        commits = response.json()
        for commit in commits:
            sha = commit['sha']
            author = commit['commit']['author']['name']
            print(f"{sha}: {author}")
    else:
        print("Error: Request failed with status code", response.status_code)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: 100-github_commits.py <repository_name> <owner_name>")
    else:
        repo_name = sys.argv[1]
        owner_name = sys.argv[2]
        get_repo_commits(repo_name, owner_name)
