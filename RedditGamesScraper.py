#! python3
import praw

MINIMUM_UPVOTE_RATIO = 0.78
MINIMUM_UPVOTES = 850

PUscript = 'Pq_F46VlaaQz2A'
secret_key = 'ZFEhKhcl-_AVkY0907yCaz22sSw'

reddit = praw.Reddit(client_id=PUscript,
                     client_secret=secret_key,
                     user_agent='GamesBot')

games = reddit.subreddit("games")


def print_links():
    for submission in games.hot(limit=20):
        if (not submission.stickied and (not ("AMA" in submission.title))):
            if(submission.upvote_ratio > MINIMUM_UPVOTE_RATIO and submission.score > MINIMUM_UPVOTES):
                print(submission.title)
