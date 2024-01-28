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

