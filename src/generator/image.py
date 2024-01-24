

import os
import time
from config.core import OUTPUT_DIR, TEMP_DIR, ASSETS_DIR_BG_VIDEO, ASSETS_DIR_BG_AUDIO
from dejavu import Dajavu, FingerprintImage
from properties.default import Properties
from renderer.image import ImageRenderer


class Generator:


    def __init__(self, output:str=None, bgVideo:str=None, bgAudio:str=None, properties:Properties=Properties()):
        #! Move Logic to Super
        self.output     = output if output is not None else Generator.Defaultfilename()
        self.bgVideo    = bgVideo
        self.bgAudio    = bgAudio
        self.properties = properties
        self.DirectoryExist(OUTPUT_DIR, TEMP_DIR, ASSETS_DIR_BG_VIDEO, ASSETS_DIR_BG_AUDIO)

    #! IMPLEMENT ABS CLASS
    #! Add Set Function
    #! Add Dajavu Function
    #! Add Render Function

    def Image(self, url:str, properties:Properties=Properties()):
        Dajavu.Add({ "image": FingerprintImage(url) })
        ImageRenderer(self.output, self.bgVideo, self.bgAudio, properties).render(url)
        return

