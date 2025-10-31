 #!/usr/bin/python3
top_ten = __import__('1-top_ten').top_ten

print("=== Valid subreddit ===")
top_ten('programming')

print("\n=== Invalid subreddit ===")
top_ten('this_is_a_fake_subreddit')

