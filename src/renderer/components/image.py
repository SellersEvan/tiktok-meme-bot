from moviepy.editor import ImageClip
from src.properties.default import Properties


def RenderImage(options:Properties, file:str, duration:int=0) -> ImageClip:
    clip = ImageClip(file)
    clip.set_position(("center", "center"))
    # meme.resize(background.w - (2 * MEME_PADDING))
    clip.set_duration(duration)
    return clip

