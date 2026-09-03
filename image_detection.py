from pathlib import Path
from ultralytics import YOLO

IMAGE_PATH = Path("sample.jpg")
MODEL_PATH = "yolov8n.pt"

if not IMAGE_PATH.exists():
    raise FileNotFoundError(f"Image not found: {IMAGE_PATH}")

model = YOLO(MODEL_PATH)
results = model.predict(
    source=str(IMAGE_PATH),
    conf=0.4,
    verbose=False
)

result = results[0]

for box in result.boxes:
    class_id = int(box.cls[0])
    confidence = float(box.conf[0])
    class_name = result.names[class_id]
    coordinates = [round(value, 2) for value in box.xyxy[0].tolist()]

    print(
        f"Detected: {class_name} | "
        f"Confidence: {confidence:.2f} | "
        f"Box: {coordinates}"
    )

result.show()