from ultralytics import YOLO
model = YOLO("../Yolo-Weights/yolov8n.pt")
print(model.names)