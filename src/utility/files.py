#
#   Copyright (C) 2024 Sellers Industries, Inc.
#   distributed under the MIT License
#
#   author: Evan Sellers <sellersew@gmail.com>
#   date: Thu Feb 01 2024
#   file: files.py
#   project: TikTok Meme Bots
#   purpose: File Utilities
#
#


import os
import time
import requests
from urllib.parse import urlparse
from PIL import Image
from io import BytesIO
from src.static import OUTPUT_DIR, TEMP_DIR
from src.utility.error import LogError


SUPPORTED_IMAGE_FORMAT = ["PNG", "JPEG", "JPG", "GIF", "BMP"]


def DirectoriesExist(*directories:str):
    for directory in directories:
        os.makedirs(directory, exist_ok=True)


def OutputFilename(filename:type[str|None]) -> str:
    if filename is not None:
        if "." in filename or "/" in filename:
            raise LogError("Please do not include a file extension or directory in the filename.")
    filename = str(int(time.time())) if filename is None else filename
    return os.path.join(OUTPUT_DIR, filename + ".mp4")


def GetImageFile(path:str) -> str:
    if os.path.isfile(path):
        if os.path.splitext(path)[1].replace(".", "").upper() in SUPPORTED_IMAGE_FORMAT:
            return path
        else:
            raise LogError("Image file is not a valid image type")
    
    parsedURL = urlparse(path)
    if parsedURL.scheme not in ("http", "https"):
        raise LogError("Image is neither a local file or a valid URL")
    
    response = requests.get(path)
    if response.status_code != 200:
        raise LogError("Failed to download the image from the URL")

    img = Image.open(BytesIO(response.content))
    if img.format not in SUPPORTED_IMAGE_FORMAT:
        raise LogError("Image URL does not point to an image")
    
    filename = os.path.join(TEMP_DIR, f"{int(time.time())}.{img.format.lower()}")
    img.save(filename)
    return filename


# The Lord has done it this very day; let us rejoice today and be glad.
# - Psalm 118:24
