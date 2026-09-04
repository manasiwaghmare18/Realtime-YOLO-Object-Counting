import time
from collections import Counter

import cv2
from ultralytics import YOLO


MODEL_PATH = "yolov8n.pt"
CONFIDENCE_THRESHOLD = 0.3
IMAGE_SIZE = 320

model = YOLO(MODEL_PATH)
camera = cv2.VideoCapture(0)

if not camera.isOpened():
    raise RuntimeError(
        "Could not open the webcam. Close other camera applications "
        "or try changing VideoCapture(0) to VideoCapture(1)."
    )

previous_time = time.perf_counter()

while True:
    success, frame = camera.read()

    if not success:
        print("Could not read a frame from the webcam.")
        break

    results = model.predict(
        source=frame,
        imgsz=IMAGE_SIZE,
        conf=CONFIDENCE_THRESHOLD,
        
    )

    result = results[0]
    class_names = result.names
    detected_objects = []

    if result.boxes is not None:
        class_ids = result.boxes.cls.cpu().numpy().astype(int)
        confidences = result.boxes.conf.cpu().numpy()
        coordinates = result.boxes.xyxy.cpu().numpy()

        for class_id, confidence, box in zip(
            class_ids, confidences, coordinates
        ):
            x1, y1, x2, y2 = map(int, box)
            class_name = class_names[class_id]
            detected_objects.append(class_name)

            cv2.rectangle(
                frame,
                (x1, y1),
                (x2, y2),
                (0, 255, 0),
                2
            )

            label = f"{class_name} {confidence:.2f}"

            cv2.putText(
                frame,
                label,
                (x1, max(y1 - 10, 20)),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.55,
                (0, 255, 0),
                2
            )

    counts = Counter(detected_objects)

    y_position = 30
    for class_name, count in counts.items():
        text = f"{class_name}: {count}"

        cv2.putText(
            frame,
            text,
            (10, y_position),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (255, 255, 255),
            2
        )

        y_position += 30

    current_time = time.perf_counter()
    fps = 1 / max(current_time - previous_time, 1e-6)
    previous_time = current_time

    cv2.putText(
        frame,
        f"FPS: {fps:.1f}",
        (10, y_position + 10),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (0, 255, 255),
        2
    )

    cv2.imshow("YOLO Object Detection and Counting", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()