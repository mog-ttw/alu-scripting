#!/usr/bin/python3
"""
Print the titles of the first 10 hot posts for a subreddit.
"""

import requests


def top_ten(subreddit):
    """Prints the titles of the top 10 hot posts for a subreddit."""
    if subreddit is None or not isinstance(subreddit, str):
        print(None)
        return

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "ALUProjectBot/1.0"}
    params = {"limit": 10}

    try:
        response = requests.get(
            url,
            headers=headers,
            params=params,
            allow_redirects=False,
            timeout=10
        )
    except Exception:
        print(None)
        return

    # Reddit returns 302 or 404 for invalid subreddits
    if response.status_code != 200:
        print(None)
        return

    data = response.json().get("data")
    if not data:
        print(None)
        return

    posts = data.get("children", [])
    if not posts:
        print(None)
        return

    for post in posts:
        print(post.get("data", {}).get("title"))
