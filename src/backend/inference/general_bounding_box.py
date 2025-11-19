# standard lib imports

# third party imports
from ultralytics import YOLO
import numpy as np

# project imports
import model_paths

model = YOLO(model_paths.yolov9e)

def draw_box(image, model=model):
    result = model(image)
    image_with_boxes = result[0].plot()
    
    return image_with_boxes