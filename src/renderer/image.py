from moviepy.editor import CompositeVideoClip
from properties.default import Properties
from src.renderer.components.audio import RenderAudio
from src.renderer.components.background import RenderBackground
from src.renderer.components.image import RenderImage


def ImageRenderer(output:str, imageURL:str, bgVideo:type[str|None], bgAudio:type[str|None], properties:Properties):
    #! FIXME - verify imageURL is actually an image, either local or online
    length     = properties.CLIP_LENGTH_MIN
    background = RenderBackground(properties, bgVideo, length)
    audio      = RenderAudio(properties, bgAudio, length)
    meme       = RenderImage(properties, imageURL, length, background)

    compose = CompositeVideoClip([background, meme])
    compose = compose.set_duration(length)
    compose = compose.set_audio(audio)
    compose.write_videofile(output, remove_temp=True)
    compose.close()

