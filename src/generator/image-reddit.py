

import os
import time
from config.core import OUTPUT_DIR, TEMP_DIR, ASSETS_DIR_BG_VIDEO, ASSETS_DIR_BG_AUDIO
from dejavu import Dajavu, FingerprintImage
from properties.default import Properties
from renderer.image import ImageRenderer


class Generator:


    def __init__(self, output:str=None, bgVideo:str=None, bgAudio:str=None, properties:Properties=Properties()):
        self.output     = output if output is not None else Generator.Defaultfilename()
        self.bgVideo    = bgVideo
        self.bgAudio    = bgAudio
        self.properties = properties
        self.DirectoryExist(OUTPUT_DIR, TEMP_DIR, ASSETS_DIR_BG_VIDEO, ASSETS_DIR_BG_AUDIO)

    #! FIXME - IMPLEMENT ABS OF IMAGE
    #! FIXME - IMPLEMENT ABS OF IMAGE
    #! FIXME - IMPLEMENT ABS OF IMAGE
    #! FIXME - IMPLEMENT ABS OF IMAGE
    #! FIXME - IMPLEMENT ABS OF IMAGE
    #! FIXME - IMPLEMENT ABS OF IMAGE
    #! FIXME - IMPLEMENT ABS OF IMAGE
    #! FIXME - IMPLEMENT ABS OF IMAGE
    #! FIXME - IMPLEMENT ABS OF IMAGE

    #! FIXME TAKE IN REDDIT URL OR ID AND GET IMAGE URL SAVING BOTH TO DAJAVU
    def RedditImage(self, url:str, properties:Properties=Properties()):
        if "reddit.com" not in url:
            raise Exception("Invalid Reddit URL")
        if "comments" not in url:
            raise Exception("Invalid Reddit URL, must be a comment")
        redditID = url.split("comments/")[1].split("/")[0]



        Dajavu.Add({ "image": FingerprintImage(url) })
        ImageRenderer(self.output, self.bgVideo, self.bgAudio, properties).render(url)
        return 


    @staticmethod
    def Defaultfilename() -> str:
        return os.path.join(OUTPUT_DIR, str(int(time.time())) + ".mp4")


    @staticmethod
    def DirectoryExist(*directories:str):
        for directory in directories:
            os.makedirs(directory, exist_ok=True)


    @staticmethod
    def GetRedditComment():
        return None

