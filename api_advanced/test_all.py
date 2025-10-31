#!/usr/bin/python3
"""
Test all Reddit API tasks (0–3)
"""

from importlib.machinery import SourceFileLoader


def run_tests():
    print("\n--- [0] number_of_subscribers ---")
    mod0 = SourceFileLoader("0-subs", "./0-subs.py").load_module()
    print("programming:", mod0.number_of_subscribers("programming"))
    print("fake subreddit:", mod0.number_of_subscribers("this_is_a_fake_subreddit"))

    print("\n--- [1] top_ten ---")
    mod1 = SourceFileLoader("1-top_ten", "./1-top_ten.py").load_module()
    mod1.top_ten("programming")
    print("\nInvalid subreddit:")
    mod1.top_ten("this_is_a_fake_subreddit")

    print("\n--- [2] recurse ---")
    mod2 = SourceFileLoader("2-recurse", "./2-recurse.py").load_module()
    res = mod2.recurse("programming")
    print("Posts fetched:", len(res) if res else "None")

    print("\n--- [3] count_words ---")
    mod3 = SourceFileLoader("3-count", "./3-count.py").load_module()
    mod3.count_words("programming", ["python", "java", "javascript", "scala", "react"])


if __name__ == "__main__":
    run_tests()
