# standard library imports
from pprint import pprint
from PIL import Image
import io
from ultralytics import YOLO
import base64

# third party imports

# project imports
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.handlers.wsgi import WSGIRequest
from inference import general_bounding_box 

# Create your views here.
@csrf_exempt
def receive_image(request:WSGIRequest):
    breakpoint()
    
    return  JsonResponse({'resp':'success'})



@csrf_exempt
def draw_box(request:WSGIRequest):
    if bytes in type(request.body).mro():
        image_bytes = io.BytesIO(request.body)
        image = Image.open(image_bytes)
    
    image_with_boxes = general_bounding_box.draw_box(image)
    json_image = base64.b64encode(image_with_boxes).decode('utf-8')
    return JsonResponse({'image':json_image})
    
    