#i!/usr/bin/python3
"""
impor of the first 10 hot posts for a subreddit.
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
        posts = data.get("data", {}).get("children", [])
        if not posts:
            print(None)
            return
        for post in posts:
            print(post.get("data", {}).get("title"))
    except Exception:
        print(None)
