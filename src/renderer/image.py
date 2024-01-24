from moviepy.editor import CompositeVideoClip
from properties.default import Properties
from src.renderer.__abs__ import Renderer
from src.renderer.components.audio import RenderAudio
from src.renderer.components.background import RenderBackground
from src.renderer.components.image import RenderImage


class ImageRenderer():


    def __init__(self, output:str, bgVideo:type[str|None], bgAudio:type[str|None], properties:Properties):
        self.output     = output
        self.bgVideo    = bgVideo
        self.bgAudio    = bgAudio
        self.properties = properties


    def render(self, imageURL:str):
        length     = self.properties.CLIP_LENGTH_MIN
        background = RenderBackground(self.properties, self.bgVideo, length)
        audio      = RenderAudio(self.properties, self.bgAudio, length)
        meme       = RenderImage(self.properties, imageURL, length, background)

        compose = CompositeVideoClip([background, meme])
        compose = compose.set_duration(length)
        compose = compose.set_audio(audio)
        compose.write_videofile(self.output, remove_temp=True)
        compose.close()

