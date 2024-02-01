#
#   Copyright (C) 2024 Sellers Industries, Inc.
#   distributed under the MIT License
#
#   author: Evan Sellers <sellersew@gmail.com>
#   date: Wed Jan 31 2024
#   file: imageReddit.py
#   project: TikTok Meme Bot
#   purpose: Generate Image Videos from Reddit
#
#


from src.generator.utilities import Cleanup, Setup
from src.dejavu.index import Dajavu
from src.dejavu.utility import FingerprintImage
from src.properties.index import Properties
from src.renderer.image import ImageRenderer
from src.utility.reddit import GetRedditPost, RedditPostHasImage
from src.utility.error import LogError
from src.utility.files import GetImageFile


def GenerateImageReddit(redditURL:str, output:str=None, bgVideo:str=None, bgAudio:str=None, properties:Properties=Properties()):
    properties, output = Setup(properties, output)
    post               = GetRedditPost(redditURL)
    
    if RedditPostHasImage(post) is False:
        raise LogError("Invalid Reddit URL, post must contain an image")
    
    imageURL = GetImageFile(post.url)
    Dajavu.Add({ "reddit": post.id, "image": FingerprintImage(imageURL) })
    ImageRenderer(output, imageURL, bgVideo, bgAudio, properties)
    Cleanup(imageURL)


# The mind governed by the flesh is death, but the mind governed by the Spirit
# is life and peace.
# - Romans 8:6
