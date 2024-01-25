from dejavu import Dajavu, FingerprintImage
from properties.index import Properties
from renderer.image import ImageRenderer


def GenerateImage(output:str, imageURL:str, bgVideo:str=None, bgAudio:str=None, properties:Properties=Properties()):
    #! FIXME - verify imageURL is actually an image, either local or online
    Dajavu.Add({ "image": FingerprintImage(imageURL) })
    ImageRenderer(output, imageURL, bgVideo, bgAudio, properties)

