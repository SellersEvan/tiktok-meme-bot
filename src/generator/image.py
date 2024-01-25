from dejavu import Dajavu, FingerprintImage
from properties.default import Properties
from renderer.image import ImageRenderer


#! FIXME ADD CLI - self.DirectoryExist(OUTPUT_DIR, TEMP_DIR, ASSETS_DIR_BG_VIDEO, ASSETS_DIR_BG_AUDIO)

def GenerateImage(output:str, imageURL:str, bgVideo:str=None, bgAudio:str=None, properties:Properties=Properties()):
    Dajavu.Add({ "image": FingerprintImage(imageURL) })
    ImageRenderer(output, imageURL, bgVideo, bgAudio, properties)

