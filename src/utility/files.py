import os
import time
from src.config.core import OUTPUT_DIR


def DirectoriesExist(*directories:str):
    for directory in directories:
        os.makedirs(directory, exist_ok=True)


def DefaultOutputFilename() -> str:
    return os.path.join(OUTPUT_DIR, str(int(time.time())) + ".mp4")

