import sys
import os
from PIL import Image, ImageOps

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

valid_ext = (".jpg", ".jpeg", ".png")
ext1 = os.path.splitext(sys.argv[1])[1].lower()
ext2 = os.path.splitext(sys.argv[2])[1].lower()

if ext1 not in valid_ext or ext2 not in valid_ext:
    sys.exit("file not in extension")
if ext1 != ext2:
    sys.exit("input and output have different extensions")

shirt = Image.open("shirt.png").convert("RGBA")
photo = Image.open(sys.argv[1])
photo = ImageOps.fit(photo, shirt.size)
photo.paste(shirt, shirt)
photo.convert("RGB").save(sys.argv[2])



