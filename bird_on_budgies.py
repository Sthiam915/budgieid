from ultralytics import YOLO
import time


model = YOLO("yolov8n.pt")

t1 = time.time()
results = model("imageset/Budgerigar/Budgerigar (1).jpg")

print(time.time() - t1)


results.show()