#! python3
import praw
import json

MINIMUM_UPVOTE_RATIO = 0.78
MINIMUM_UPVOTES = 850


class RedditGamesScraper():

    def __init__(self):

        with open('config.json') as config_file:
            data = json.load(config_file)

        self.PUscript = data['reddit'][0]['PUscript']
        self.secret_key = data['reddit'][0]['secret_key']

        self.reddit = praw.Reddit(client_id=self.PUscript,
                                  client_secret=self.secret_key,
                                  user_agent='GamesBot')

    def getLinks(self):
        games = self.reddit.subreddit("games")
        submissions = []

        for submission in games.hot(limit=20):
            if (not submission.stickied and (not ("AMA" in submission.title))):
                if(submission.upvote_ratio > MINIMUM_UPVOTE_RATIO and submission.score > MINIMUM_UPVOTES):
                    submissions.append(submission)
        return submissions
