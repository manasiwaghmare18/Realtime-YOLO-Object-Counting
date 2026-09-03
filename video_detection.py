from pathlib import Path
import cv2
from ultralytics import YOLO

VIDEO_PATH = Path("vs2.mp4")
MODEL_PATH = "yolov8n.pt"

if not VIDEO_PATH.exists():
    raise FileNotFoundError(f"Video not found: {VIDEO_PATH}")

model = YOLO(MODEL_PATH)
video_results = model.predict(
    source=str(VIDEO_PATH),
    stream=True,
    conf=0.5,
    imgsz=640,
    verbose=False
)

for result in video_results:
    annotated_frame = result.plot()

    cv2.imshow("YOLO Video Detection", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cv2.destroyAllWindows()