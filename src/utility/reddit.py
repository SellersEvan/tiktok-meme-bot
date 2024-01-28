import praw
from src.config.index import Config
from src.static import REDDIT_USER_AGENT


def GetRedditPost(url:str) -> praw.Reddit.submission:
    return GetReddit().submission(url=url)


def GetReddit() -> praw.Reddit:
    config = Config()
    return praw.Reddit(
        client_id=config.REDDIT_CLIENT_ID,
        client_secret=config.REDDIT_SECRET,
        username=config.REDDIT_USERNAME,
        password=config.REDDIT_PASSWORD,
        user_agent=REDDIT_USER_AGENT
    )

