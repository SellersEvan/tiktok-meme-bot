# import os
# from src.config.core import OUTPUT_DIR
# from src.renderer.image import ImageRenderer
from src.config.index import Config
from src.properties.index import Properties

# ImageRenderer(os.path.join(OUTPUT_DIR, "food" + ".mp4"), None, None, None).render("meme.png")
print(Config())
print(Properties())