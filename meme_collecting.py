import os, random, scrapetube, praw, requests, urllib.request
from pytube import YouTube
from instaloader import Instaloader, Profile


# Reads the dejavu txt file and returns a list of the contents
def get_dejavu():
    with open("dejavu.txt", "r") as f:
        return f.read().splitlines()


# Adds a new value to the dejavu txt file
def add_to_dejavu(s):
    with open("dejavu.txt", "a") as f:
        f.write(s + "\n")



# Holds information relevent to using the Reddit library
class RedditInfo:
    # Constructor
    def __init__(self, client_id, secret, reddit_username, reddit_password, user_agent):
        self.client_id = client_id
        self.secret = secret
        self.reddit_username = reddit_username
        self.reddit_password = reddit_password
        self.user_agent = user_agent


# Retrieves memes
class MemeMachine:
    # filenames = name it saves the memes as
    # reddit_ids = list of subreddits it searches
    # reddit_info = RedditInfo class containing info needed to use Praw
    def __init__(self, filenames, reddit_ids, reddit_info):
        if len(reddit_ids) == 0:
            raise Exception("Please give at least one subreddit for the bot to pick from.")
        self.filenames   = filenames
        self.reddit_ids  = reddit_ids
        self.reddit_info = reddit_info
    

    # Retrieves a reddit meme
    def reddit_meme(self):
        # Initializes the reddit variable
        reddit = praw.Reddit(
            client_id=self.reddit_info.client_id,
            client_secret=self.reddit_info.secret,
            username=self.reddit_info.reddit_username,
            password=self.reddit_info.reddit_password,
            user_agent=self.reddit_info.user_agent
        )

        # Finds a reddit post
        reddit_url = ""
        meme_type = ""
        dejavu = get_dejavu()
        subreddit_pick = random.choice(self.reddit_ids)
        subreddit = reddit.subreddit(subreddit_pick).hot(limit=40)
        for submission in subreddit:
            print(submission.__dict__)
            if not (submission.is_self or submission.stickied or submission.url in dejavu):
                meme_type = submission.url.split(".")[-1]
                if meme_type == "png" or meme_type == "jpg":
                    reddit_url = submission.url
                    add_to_dejavu(reddit_url)
                    break
        
        # Downloads the reddit meme, or throws an exception if an image could not be found
        if reddit_url == "":
            raise Exception(f"Unable to find Reddit image for subreddit {subreddit_pick}")
        else:
            img_data = requests.get(reddit_url).content
            with open(f"{self.filenames}.{meme_type}", "wb") as handler:
                handler.write(img_data)
        
        # Returns the name of the saved file
        return f"{self.filenames}.{meme_type}"


    def new_meme(self):
        return self.reddit_meme()

