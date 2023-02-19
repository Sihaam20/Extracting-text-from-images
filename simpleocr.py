import easyocr as ocr  #OCR
import cv2
import matplotlib.pyplot as plt

from pylab import rcParams

from IPython.display import Image
rcParams['figure.figsize'] = 8,16

from PIL import Image
im = Image.open("outliers.jpeg")

im

reader = ocr.Reader(['en'],model_storage_directory='.')

bounds = reader.readtext("outliers.jpeg")

from PIL import Image, ImageDraw, ImageFont

def draw_boxes(image,bounds, color = 'blue', width =2):
  draw = ImageDraw.Draw(image)
  for bound in bounds:
    p0,p1,p2,p3 = bound[0]
    draw.line([*p0,*p1,*p2,*p3,*p0], fill=color, width = width)
  return image

draw_boxes(im, bounds)


for x in bounds:
  print(x[1].strip())
