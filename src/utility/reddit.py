#
#   Copyright (C) 2024 Sellers Industries, Inc.
#   distributed under the MIT License
#
#   author: Evan Sellers <sellersew@gmail.com>
#   date: Thu Feb 01 2024
#   file: reddit.py
#   project: TikTok Meme Bot
#   purpose: Reddit Utilities
#
#


import praw
from src.config.index import Config
from src.static import REDDIT_USER_AGENT
from src.utility.error import LogError


def GetRedditPost(url:str) -> praw.Reddit.submission:
    if "reddit.com" not in url:
        raise LogError("Invalid Reddit URL")
    if "comments" not in url:
        raise LogError("Invalid Reddit URL, must be a comment")
    post = GetReddit().submission(url=url)
    if not post:
        raise LogError("Invalid Reddit URL, must be a comment")
    return post


def GetReddit() -> praw.Reddit:
    config = Config()
    return praw.Reddit(
        client_id=config.REDDIT_CLIENT_ID,
        client_secret=config.REDDIT_SECRET,
        username=config.REDDIT_USERNAME,
        password=config.REDDIT_PASSWORD,
        user_agent=REDDIT_USER_AGENT
    )


def RedditPostHasImage(post:praw.Reddit.submission) -> bool:
    if not post.url:
        return False
    if post.url.split(".")[-1].lower() not in ["jpg", "jpeg", "png"]:
        return False
    return True


# Show me your ways, Lord, teach me your paths.
# - Psalm 25:4
