from src.generator.utilities import Cleanup, Setup
from src.dejavu.index import Dajavu
from src.dejavu.utility import FingerprintImage
from src.properties.index import Properties
from src.renderer.image import ImageRenderer
from src.utility.files import GetImageFile


def GenerateImage(imageURL:str, output:str=None, bgVideo:str=None, bgAudio:str=None, properties:Properties=None):
    properties, output = Setup(properties, output)
    imageURL           = GetImageFile(imageURL)
    Dajavu.Add({ "image": FingerprintImage(imageURL) })
    ImageRenderer(output, imageURL, bgVideo, bgAudio, properties)
    Cleanup(imageURL)

