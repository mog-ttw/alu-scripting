#!/usr/bin/python3
"""
Print the titles of the first 10 hot posts for a subreddit.
"""

import requests


def top_ten(subreddit):
    """Print titles of top 10 hot posts for a subreddit."""
    if subreddit is None or not isinstance(subreddit, str):
        print(None)
        return

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "ALUProjectBot/1.0"}
    params = {"limit": 10}

    resp = requests.get(url, headers=headers, params=params,
                        allow_redirects=False)

    if resp.status_code != 200:
        print(None)
        return

    posts = resp.json().get("data", {}).get("children", [])
    if not posts:
        print(None)
        return

    for post in posts:
        title = post.get("data", {}).get("title")
        if title:
            print(title)
