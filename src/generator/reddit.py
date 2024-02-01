#
#   Copyright (C) 2024 Sellers Industries, Inc.
#   distributed under the MIT License
#
#   author: Evan Sellers <sellersew@gmail.com>
#   date: Wed Jan 31 2024
#   file: reddit.py
#   project: TikToke Meme Bot
#   purpose: Generate Meme Videos from scrapping Subreddits
#
#


import praw
import random
from src.generator.utilities import Cleanup, Setup
from src.dejavu.index import Dajavu
from src.dejavu.utility import FingerprintImage
from src.properties.index import Properties
from src.renderer.image import ImageRenderer
from src.utility.reddit import GetReddit, RedditPostHasImage
from src.utility.files import GetImageFile, OutputFilename


def GenerateReddit(subreddits:list[str], iterations:int=1, bgVideo:str=None, bgAudio:str=None, properties:Properties=Properties()):
    properties, output = Setup(properties, None)

    for _ in range(iterations):
        post     = getRandomPost(subreddits)
        output   = OutputFilename(None)
        imageURL = GetImageFile(post.url)
        Dajavu.Add({ "reddit": post.id, "image": FingerprintImage(imageURL) })
        ImageRenderer(output, imageURL, bgVideo, bgAudio, properties)
        Cleanup(imageURL)


def getRandomPost(subreddits:list[str]) -> praw.Reddit.submission:
    subreddit = GetReddit().subreddit(random.choice(subreddits)).hot(limit=40)
    for post in subreddit:
        if RedditPostHasImage(post) is False:
            continue

        imageURL = GetImageFile(post.url)
        exists   = Dajavu.Contains({ "reddit": post.id, "image": FingerprintImage(imageURL) })
        Cleanup(imageURL)
        if exists:
            continue
        # ? (FUTURE) ADD MEME Detection
        # ? (FUTURE) ADD PROFANITY DETECTION
        return post


# Blessed are those whose ways are blameless, who walk according to the law
# of the Lord.
# - Psalm 119:1
