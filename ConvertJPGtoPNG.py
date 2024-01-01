#pip install PILLOW

from PIL import Image

im = Image.open("sample_image.jpg").convert("RGB")
im.save("sample_image.png", "png")
