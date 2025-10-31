#!/usr/bin/python3
"""Recursively return all hot post titles for a subreddit."""

import requests


def recurse(subreddit, hot_list=None, after=None):
    """Return a list of all hot post titles."""
    if hot_list is None:
        hot_list = []

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "ALUProjectBot/1.0"}
    params = {"after": after, "limit": 100}

    resp = requests.get(url, headers=headers, params=params,
                        allow_redirects=False)

    if resp.status_code != 200:
        return None

    data = resp.json().get("data", {})
    children = data.get("children", [])

    for post in children:
        hot_list.append(post.get("data", {}).get("title"))

    after = data.get("after")
    if after:
        return recurse(subreddit, hot_list, after)
    return hot_list
