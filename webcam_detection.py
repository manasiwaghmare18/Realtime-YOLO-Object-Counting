from ultralytics import YOLO

model = YOLO("yolov8n.pt")

results = model.predict(
    source=0,
    stream=True,
    imgsz=320,
    conf=0.5,
    verbose=False
)

for result in results:
    result.show()