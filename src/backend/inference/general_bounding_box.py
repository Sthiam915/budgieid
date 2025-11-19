# standard lib imports

# third party imports
from ultralytics import YOLO
from PIL import Image
import numpy as np
import io

# project imports
from inference import model_paths

model = YOLO(model_paths.yolov9e)

def draw_box(image:Image, model:YOLO=model) -> bytes:
    result = model(image)
    image_with_boxes = result[0].plot(labels=False)
    img_pil = Image.fromarray(image_with_boxes)
    r, g, b = img_pil.split()
    img_pil = Image.merge("RGB", (b, g, r)) 
    buffer = io.BytesIO()
    img_pil.save(buffer, format='JPEG')
    image_bytes = buffer.getvalue()
    print("...")
    return image_bytes