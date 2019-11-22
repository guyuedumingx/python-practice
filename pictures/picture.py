#微信集赞
from PIL import ImageColor, Image
import logging

imageCati = Image.open('1.jpg')
imageCat = imageCati.convert("RGBA")
imageCat.show()