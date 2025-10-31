#!/usr/bin/python3
"""
Return the number of subscribers for a given subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """Return total subscribers of a subreddit; 0 if invalid."""
    if subreddit is None or not isinstance(subreddit, str):
        return 0

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "ALUProjectBot/1.0"}
    try:
        r = requests.get(url, headers=headers, allow_redirects=False, timeout=10)
    except Exception:
        return 0

    if r.status_code != 200:
        return 0

    data = r.json().get("data", {})
    return data.get("subscribers", 0)

