#
#   Copyright (C) 2024 Sellers Industries, Inc.
#   distributed under the MIT License
#
#   author: Evan Sellers <sellersew@gmail.com>
#   date: Wed Jan 31 2024
#   file: image.py
#   project: TikTok Meme Bot
#   purpose: Generate Image Videos
#
#


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


# Give careful thought to the paths for your feet and be steadfast in
# all your ways.
# - Proverbs 4:26
