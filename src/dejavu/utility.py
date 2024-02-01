#
#   Copyright (C) 2024 Sellers Industries, Inc.
#   distributed under the MIT License
#
#   author: Evan Sellers <sellersew@gmail.com>
#   date: Wed Jan 31 2024
#   file: utility.py
#   project: TikTok Meme Bot
#   purpose: Dejavu Utilies - Fingerprint Generator
#
#


from PIL import Image
import imagehash


def FingerprintImage(imagepath:str) -> str:
    image = Image.open(imagepath)
    return str(imagehash.dhash(image))


# For as in Adam all die, so in Christ all will be made alive.
# - 1 Corinthians 15:22
