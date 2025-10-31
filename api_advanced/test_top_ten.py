	#!/usr/bin/python3
"""
Local tester for 1-top_ten.py
"""

top_ten = __import__('1-top_ten').top_ten

if __name__ == "__main__":
    print("--- Valid subreddit ---")
    top_ten('programming')

    print("\n--- Invalid subreddit ---")
    top_ten('this_is_a_fake_subreddit')
