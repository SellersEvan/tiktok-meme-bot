#
#   Copyright (C) 2024 Sellers Industries, Inc.
#   distributed under the MIT License
#
#   author: Evan Sellers <sellersew@gmail.com>
#   date: Thu Feb 01 2024
#   file: image.py
#   project: TikTok Meme Bot
#   purpose: Render Video for Image
#
#


from moviepy.editor import CompositeVideoClip
from src.properties.index import Properties
from src.renderer.components.audio import RenderAudio
from src.renderer.components.background import RenderBackground
from src.renderer.components.image import RenderImage


def ImageRenderer(output:str, imageURL:str, bgVideo:type[str|None], bgAudio:type[str|None], properties:Properties):
    length     = properties.CLIP_LENGTH_MIN
    background = RenderBackground(properties, bgVideo, length)
    audio      = RenderAudio(properties, bgAudio, length)
    meme       = RenderImage(properties, imageURL, length, background)

    compose = CompositeVideoClip([background, meme])
    compose = compose.set_duration(length)
    compose = compose.set_audio(audio)
    compose.write_videofile(output, remove_temp=True)
    compose.close()


# You are to be holy to me because I, the Lord, am holy, and I have set you
# apart from the nations to be my own.
# - Leviticus 20:26
