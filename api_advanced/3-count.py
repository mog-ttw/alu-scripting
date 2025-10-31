#!/usr/bin/python3
"""
Count keyword occurrences in all hot post titles of a subreddit.
"""

import re
import requests


def count_words(subreddit, word_list, after=None, counts=None):
    """
    Recursively count occurrences of words in all hot post titles.
    Prints results sorted by count (desc) then alphabetically.
    """
    if counts is None:
        counts = {}

    if not isinstance(subreddit, str) or subreddit is None:
        return

    # Normalize words (lowercase)
    word_list = [word.lower() for word in word_list]

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "ALUProjectBot/1.0"}
    params = {"after": after, "limit": 100}

    try:
        resp = requests.get(url, headers=headers, params=params,
                            allow_redirects=False, timeout=10)
    except Exception:
        return

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
        return count_words(subreddit, word_list, after, counts)

    # Print final sorted results
    sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
    for word, count in sorted_counts:
        if count > 0:
            print("{}: {}".format(word, count))

