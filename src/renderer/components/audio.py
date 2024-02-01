#
#   Copyright (C) 2024 Sellers Industries, Inc.
#   distributed under the MIT License
#
#   author: Evan Sellers <sellersew@gmail.com>
#   date: Wed Jan 31 2024
#   file: audio.py
#   project: TikTok Meme Bot
#   purpose: Render Audio Component
#
#


import os
import random
from moviepy.editor import AudioFileClip
from src.static import ASSETS_DIR_BG_AUDIO
from src.properties.index import Properties


def RenderAudio(options:Properties, file:str=None, duration:int=0) -> AudioFileClip:
    clip = AudioFileClip(selectRandomAudio() if file is None else file)
    clip = trimRandomPosition(clip, duration)
    return clip


def trimRandomPosition(clip:AudioFileClip, duration:int) -> AudioFileClip:
    trim_start = random.randint(0, int(clip.duration) - duration)
    return clip.subclip(trim_start, trim_start + duration)


def selectRandomAudio() -> str:
    audios = []
    for filename in os.listdir(ASSETS_DIR_BG_AUDIO):
        if os.path.splitext(filename)[1] == ".mp3":
            audios.append(os.path.join(ASSETS_DIR_BG_AUDIO, filename))
    if len(audios) == 0:
        raise Exception(f"Please ensure there is .mp3 files in the {ASSETS_DIR_BG_AUDIO} directory.")
    return random.choice(audios)

