from dejavu import Dajavu, FingerprintImage
from properties.default import Properties
from renderer.image import ImageRenderer


def RedditImage(output:str, redditURL:str, bgVideo:str=None, bgAudio:str=None, properties:Properties=Properties()):
    if "reddit.com" not in redditURL:
        raise Exception("Invalid Reddit URL")
    if "comments" not in redditURL:
        raise Exception("Invalid Reddit URL, must be a comment")
    redditID = redditURL.split("comments/")[1].split("/")[0]
    #! VALIDATE REDDIT HAS IMAGE
    imageURL = ""
    #! VALIDATE REDDIT HAS IMAGE
    Dajavu.Add({ "reddit": redditID, "image": FingerprintImage(imageURL) })
    ImageRenderer(output, imageURL, bgVideo, bgAudio, properties)

