#
#   Copyright (C) 2024 Sellers LLC - All Rights Reserved
#   Unauthorized copying of this file, via any medium is strictly
#   prohibited. Proprietary and confidential.
#
#   author: Evan Sellers <sellersew@gmail.com>
#   date: Wed Jan 31 2024
#   file: utilities.py
#   project: TikTok Meme Bot
#   purpose: Generator Utilities
#
#


import os
from src.config.index import Config
from src.properties.index import Properties
from src.utility.files import DirectoriesExist, OutputFilename
from src.static import ASSETS_DIR_BG_AUDIO, ASSETS_DIR_BG_VIDEO, OUTPUT_DIR, TEMP_DIR


def Setup(properties:Properties=None, output:str=None) -> Properties:
    Config()
    DirectoriesExist(OUTPUT_DIR, TEMP_DIR, ASSETS_DIR_BG_VIDEO, ASSETS_DIR_BG_AUDIO)
    properties = Properties() if properties is None else properties
    output     = OutputFilename(output)
    return properties, output


def Cleanup(file:str):
    if os.path.exists(file):
        os.remove(file)


# For you were once darkness, but now you are light in the Lord. Live as
# children of light.
# - Ephesians 5:8
