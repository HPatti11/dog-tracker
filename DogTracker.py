import torch
import cv2

# Load YOLOv5 model (small version)
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

# ----- IMAGE DETECTION -----
img_path = "lyacaon.jpg"          # your image file
results = model(img_path)       # run inference
results.print()                 # print detection results
results.show()                  # display result in a window
results.save()                  # save output to runs/detect/
