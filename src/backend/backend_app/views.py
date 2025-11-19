# standard library imports
from pprint import pprint
from PIL import Image
import io
from ultralytics import YOLO

# third party imports

# project imports
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.handlers.wsgi import WSGIRequest

# Create your views here.
@csrf_exempt
def receive_image(request:WSGIRequest):
    breakpoint()
    
    return  JsonResponse({'resp':'success'})


def detect_budgerigar(image, model):
    pass
@csrf_exempt
def draw_box(request:WSGIRequest):
    image_bytes = io.BytesIO(request.body)
    image = Image.open(image_bytes)
    
    
    