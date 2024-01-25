from moviepy.editor import ImageClip
from properties.index import Properties


def RenderImage(options:Properties, file:str, duration:int=0, background:ImageClip=None) -> ImageClip:
    clip = ImageClip(file)
    clip = clip.set_duration(duration)
    clip = clip.set_position(("center", "center"), relative=True)
    if background is not None:
        clip = clip.resize(width=background.w - (2 * options.IMAGE_PADDING))
    return clip

