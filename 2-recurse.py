#!/usr/bin/python3
"""
Recursively queries the Reddit API and returns all hot article titles.
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """Return list of hot post titles or None if invalid subreddit."""
    if subreddit is None or type(subreddit) is not str:
        return None

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'ALUProjectBot/1.0'}
    params = {'after': after, 'limit': 100}

    response = requests.get(
        url, headers=headers, params=params, allow_redirects=False
    )

    if response.status_code != 200:
        return None

    data = response.json().get("data", {})
    children = data.get("children", [])

    for post in children:
        hot_list.append(post.get("data", {}).get("title"))

    after = data.get("after")
    if after:
        return recurse(subreddit, hot_list, after)
    return hot_list
