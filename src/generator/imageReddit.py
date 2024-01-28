from src.generator.utilities import Setup
from src.dejavu.index import Dajavu
from src.dejavu.utility import FingerprintImage
from src.properties.index import Properties
from src.renderer.image import ImageRenderer
from src.utility.reddit import GetRedditPost
from src.utility.error import LogError
from src.utility.files import GetImageFile


def GenerateImageReddit(redditURL:str, output:str=None, bgVideo:str=None, bgAudio:str=None, properties:Properties=Properties()):
    properties, output = Setup(properties, output)
    if "reddit.com" not in redditURL:
        raise LogError("Invalid Reddit URL")
    if "comments" not in redditURL:
        raise LogError("Invalid Reddit URL, must be a comment")
    post = GetRedditPost(redditURL)
    if not post:
        raise LogError("Invalid Reddit URL, must be a comment")
    if not post.url or post.url.split(".")[-1] not in ["jpg", "jpeg", "png"]:
        raise LogError("Invalid Reddit URL, post must contain an image")
    imageURL = GetImageFile(post.url)
    Dajavu.Add({ "reddit": post.id, "image": FingerprintImage(imageURL) })
    ImageRenderer(output, imageURL, bgVideo, bgAudio, properties)

