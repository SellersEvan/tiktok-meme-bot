#
#   Copyright (C) 2024 Sellers Industries, Inc.
#   distributed under the MIT License
#
#   author: Evan Sellers <sellersew@gmail.com>
#   date: Thu Feb 01 2024
#   file: image.py
#   project: TikTok Meme Bot
#   purpose: Render Image Component
#
#


from moviepy.editor import ImageClip
from src.properties.index import Properties


def RenderImage(options:Properties, file:str, duration:int=0, background:ImageClip=None) -> ImageClip:
    clip = ImageClip(file)
    clip = clip.set_duration(duration)
    clip = clip.set_position(("center", "center"), relative=True)
    if background is not None:
        clip = clip.resize(width=background.w - (2 * options.IMAGE_PADDING))
    return clip


# Whoever pursues righteousness and love finds life, prosperity and honor.
# - Proverbs 21:21
