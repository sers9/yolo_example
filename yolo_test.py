import cv2
import torch
from PIL import Image

import sys

if len(sys.argv) < 2:
	print('\nImage file is needed.\nExample usage: python yolo_test.py img_file_name')
	exit()

print('\nUploading model...')
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

img_file = sys.argv[1]
img = Image.open(img_file)

results = model(img, size=640)

results.print()  
results.save()