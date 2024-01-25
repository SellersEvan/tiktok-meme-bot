import os
import time
import typing
from src.config.core import OUTPUT_DIR


def DirectoriesExist(*directories:str):
    for directory in directories:
        os.makedirs(directory, exist_ok=True)


def OutputFilename(filename:typing[str|None]) -> str:
    filename = str(int(time.time())) if filename is None else filename
    return os.path.join(OUTPUT_DIR, filename + ".mp4")

