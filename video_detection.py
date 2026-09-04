from pathlib import Path

import cv2
from ultralytics import YOLO


VIDEO_PATH = Path("vs4.mp4")
MODEL_PATH = "yolov8n.pt"
CONFIDENCE_THRESHOLD = 0.5
IMAGE_SIZE = 640


if not VIDEO_PATH.exists():
    raise FileNotFoundError(f"Video not found: {VIDEO_PATH}")


model = YOLO(MODEL_PATH)

video_results = model(
    source=str(VIDEO_PATH),
    stream=True,
    conf=CONFIDENCE_THRESHOLD,
    imgsz=IMAGE_SIZE,
    verbose=False
)


for result in video_results:
    annotated_frame = result.plot()

    cv2.imshow("YOLO Video Detection", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


cv2.destroyAllWindows()