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

        submissions = self.getUniqueIDs(submissions)
        return [sub for sub in submissions]

    def getUniqueIDs(self, submissions):

        f = open('ids.txt', 'r')
        data = f.readlines()
        curr_ids = []
        for id in data:
            curr_ids.append(id[:-1])

        return_subs = []
        for sub in submissions:
            if sub.id not in curr_ids:
                curr_ids.append(sub.id)
                return_subs.append(sub)

        with open('ids.txt', 'w') as f:
            for id in curr_ids:
                f.write("%s\n" % id)

        return return_subs


'''

    JSON Version of getUniqueIDs, will return to this later


    def getUniqueIDs(self, submissions):
        with open('ids.json') as submission_ids:
            data = json.load(submission_ids)
            curr_ids = data['ids']

            return_subs = []
            for sub in submissions:
                if sub.id not in curr_ids:
                    curr_ids.append(sub.id)
                    return_subs.append(sub)
            data.update({"ids": curr_ids})
            json.dumps(data)

        return return_subs
        '''
