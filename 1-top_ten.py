i!/usr/bin/python3
""" of the firs of the first 10 hot posts for a subreddit.
"""

import requests


def top_ten(subreddit):
    """Print titles of top 10 hot posts for a subreddit."""
    if subreddit is None or not isinstance(subreddit, str):
        return

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "ALUProjectBot/1.0"}
    params = {"limit": 10}

    try:
        resp = requests.get(
            url,
            headers=headers,
            params=params,
            allow_redirects=False,
            timeout=10
        )
    except Exception:
        return

    if resp.status_code != 200:
        return

    payload = resp.json().get("data", {})
    posts = payload.get("children", [])
    if not posts:
        return

    for post in posts[:10]:
        title = post.get("data", {}).get("title")
        if title:
            print(title)
 10 hot posts for a subreddit.
"""

import requests


def top_ten(subreddit):
    """Print titles of top 10 hot posts for a subreddit."""
    if subreddit is None or not isinstance(subreddit, str):
        return

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "ALUProjectBot/1.0"}
    params = {"limit": 10}

    try:
        resp = requests.get(
            url,
            headers=headers,
            params=params,
            allow_redirects=False,
            timeout=10
        )
    except Exception:
        return

    if resp.status_code != 200:
        return

    payload = resp.json().get("data", {})
    posts = payload.get("children", [])
    if not posts:
        return

    for post in posts[:10]:
        title = post.get("data", {}).get("title")
        if title:
            print(title)

Prints the titles of the first 10 hot posts for a subreddit.
"""

import requests


def top_ten(subreddit):
    """Display the top 10 hot post titles."""
    if subreddit is None or type(subreddit) is not str:
        print(None)
        return

    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {'User-Agent': 'ALUProjectBot/1.0 (by u/mog-ttw)'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    # Check for valid response
    if response.status_code != 200:
        print(None)
        return

    try:
        data = response.json()
        posts 

