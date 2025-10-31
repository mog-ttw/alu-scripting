#!/usr/bin/python3
"""
Count keyword occurrences in all hot post titles.
"""

import requests
import re


def count_words(subreddit, word_list, after=None, counts=None):
    """Count keywords recursively and print sorted results."""
    if counts is None:
        counts = {}

    # Normalize word list
    word_list = [word.lower() for word in word_list]

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "ALUProjectBot/1.0"}
    params = {"after": after, "limit": 100}

    resp = requests.get(url, headers=headers, params=params,
                        allow_redirects=False)

    if resp.status_code != 200:
        return

    data = resp.json().get("data", {})
    posts = data.get("children", [])

    for post in posts:
        title = post.get("data", {}).get("title", "").lower()
        words = re.findall(r"[a-z]+", title)
        for word in word_list:
            counts[word] = counts.get(word, 0) + words.count(word)

    after = data.get("after")
    if after:
        count_words(subreddit, word_list, after, counts)
        return

    # Print sorted results
    for word, count in sorted(counts.items(),
                              key=lambda x: (-x[1], x[0])):
        if count > 0:
            print("{}: {}".format(word, count))
