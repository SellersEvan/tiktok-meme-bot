#
#   Copyright (C) 2024 Sellers Industries, Inc.
#   distributed under the MIT License
#
#   author: Evan Sellers <sellersew@gmail.com>
#   date: Thu Feb 01 2024
#   file: background.py
#   project: TikTok Meme Bot
#   purpose: Render Background Component
#
#


import os
import random
from moviepy.editor import VideoFileClip
from src.static import ASSETS_DIR_BG_VIDEO
from src.properties.index import Properties


def RenderBackground(options:Properties, file:str=None, duration:int=0) -> VideoFileClip:
    clip = VideoFileClip(selectRandomVideo() if file is None else file)
    clip = trimRandomPosition(clip, duration)
    clip = cropToRatio(clip, options.SCREEN_RATIO)
    return clip


def trimRandomPosition(clip:VideoFileClip, duration:int) -> VideoFileClip:
    trim_start = random.randint(0, int(clip.duration) - duration)
    return clip.subclip(trim_start, trim_start + duration)


def cropToRatio(clip:VideoFileClip, ratio:float) -> VideoFileClip:
    width  = int(clip.size[1] * ratio)
    height = clip.size[1]
    x1     = int((clip.size[0] - width) / 2)
    x2     = x1 + width
    return clip.crop(x1=x1, y1=0, x2=x2, y2=height)


def selectRandomVideo() -> str:
    videos = []
    for filename in os.listdir(ASSETS_DIR_BG_VIDEO):
        if os.path.splitext(filename)[1] == ".mp4":
            videos.append(os.path.join(ASSETS_DIR_BG_VIDEO, filename))
    if len(videos) == 0:
        raise Exception(f"Please ensure there is .mp4 files in the {ASSETS_DIR_BG_VIDEO} directory.")
    return random.choice(videos)


# Surely God is my help; the Lord is the one who sustains me.
# - Psalm 54:4
