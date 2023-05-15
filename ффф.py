

from PIL import Image, ImageFilter
def ypr1():

 image = Image.open('
 width, height = image.size
 forma = image.format
 mode = image.mode

 print("ширина", width)
 print("высота", height)
 print("формат", forma)
 print("цветовая модель", mode)

ypr1()
