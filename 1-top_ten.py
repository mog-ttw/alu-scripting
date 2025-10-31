#!/usr/bin/python3
"""
Prints the titles of the first 10 hot posts for a subreddit.
"""

import requests


def top_ten(subreddit):
    """Display the top 10 hot post titles."""
    if subreddit is None or type(subreddit) is not str:
        print(None)
        return

    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {'User-Agent': 'ALUProjectBot/1.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        print(None)
        return

    data = response.json()
    posts = data.get("data", {}).get("children", [])
    for post in posts:
        print(post.get("data", {}).get("title"))
