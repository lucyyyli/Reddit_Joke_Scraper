import praw
import pandas as pd
from datetime import datetime

# read only instance
reddit_read_only = praw.Reddit(client_id="",         # client id
                               client_secret="",      # client secret
                               user_agent="")        # user agent
print(reddit_read_only.read_only) # output: True

posts = []
jokes_subreddits = reddit_read_only.subreddit('dadjokes+Jokes')

for post in jokes_subreddits.top(time_filter="week"):
    epoch_time = datetime.utcfromtimestamp(post.created).strftime('%Y-%m-%d %H:%M:%S')
    if not ("\r" in post.selftext or "\n" in post.selftext or post.over_18):
        posts.append([post.subreddit, post.score, post.title, post.selftext, post.url, post.id, epoch_time])

posts = pd.DataFrame(posts,columns=['subreddit', 'upvotes', 'setup', 'punchline', 'url', 'id', 'created'])
print(posts)

posts.to_csv("jokes.csv", encoding='utf-8', index=False)