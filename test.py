import os
from src.config.core import OUTPUT_DIR
from src.renderer.image import ImageRenderer


ImageRenderer(os.path.join(OUTPUT_DIR, "food" + ".mp4"), None, None, None).render("meme.png")