#!/usr/bin/python3
"""
Recursive function that queries Reddit API, parses titles,
and prints a sorted count of given keywords.
"""

import requests


def count_words(subreddit, word_list, after=None, counts=None):
    """Recursively count keyword occurrences in hot article titles."""
    if counts is None:
        counts = {}

    if subreddit is None or type(subreddit) is not str:
        return

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'ALUProjectBot/1.0'}
    params = {'after': after, 'limit': 100}

    response = requests.get(
        url, headers=headers, params=params, allow_redirects=False
    )

    if response.status_code != 200:
        return

    data = response.json().get("data", {})
    posts = data.get("children", [])
    after = data.get("after")

    # Count words in titles
    for post in posts:
        title = post.get("data", {}).get("title", "").lower().split()
        for word in word_list:
            key = word.lower()
            counts[key] = counts.get(key, 0) + title.count(key)

    if after:
        count_words(subreddit, word_list, after, counts)
    else:
        sorted_counts = sorted(
            [(k, v) for k, v in counts.items() if v > 0],
            key=lambda x: (-x[1], x[0])
        )
        for k, v in sorted_counts:
            print("{}: {}".format(k, v))
