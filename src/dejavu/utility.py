from PIL import Image
import imagehash


def FingerprintImage(imagepath:str) -> str:
    image = Image.open(imagepath)
    return str(imagehash.dhash(image))

