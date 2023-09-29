#!/usr/bin/python3
"""100-github_commits.py: Python script that takes 2 arguments"""
import requests
import sys


if __name__ == "__main__":
    repository = sys.argv[1]
    owner = sys.argv[2]

    url = f"https://api.github.com/repos/{owner}/{repository}/commits"
    request = requests.get(url)
    response_json = request.json()
    for idx in response_json[:10]:
        commit_sha = idx.get("sha")
        commit_author = idx.get("commit").get("author").get("name")
        print("{}: {}".format(commit_sha, commit_author))
