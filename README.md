# Real-Time YOLO Object Detection and Counting

A beginner-friendly Computer Vision project that uses a pretrained YOLO model and OpenCV to detect and count objects from images, videos, and a webcam stream.

## Features

- Object detection from images
- Object detection from video files
- Real-time webcam detection
- Per-frame object counting
- Confidence score display
- Bounding-box visualization
- Basic FPS measurement

## Architecture

```text
Image / Video / Webcam
          |
          v
OpenCV frame capture
          |
          v
YOLO inference
          |
          v
Bounding boxes, class labels, confidence scores
          |
          v
OpenCV visualization and per-frame counting
```

## Technology Stack

- Python
- Ultralytics YOLO
- OpenCV
- NumPy
- PyTorch through Ultralytics

## Project Structure

```text
.
├── main.py
├── video_detection.py
├── webcam_detection.py
├── webcam_counting.py
├── requirements.txt
└── README.md
```

## Setup on Windows

Create a virtual environment:

```powershell
python -m venv cv-env
```

Activate it:

```powershell
.\cv-env\Scripts\Activate.ps1
```

Install dependencies:

```powershell
pip install -r requirements.txt
```

## Usage

Run image detection:

```powershell
python main.py
```

Run video detection:

```powershell
python video_detection.py
```

Run webcam detection:

```powershell
python webcam_detection.py
```

Run webcam detection with per-frame counting:

```powershell
python webcam_counting.py
```

Press `q` in the OpenCV window to exit.

## How It Works

1. OpenCV obtains an image or video frame.
2. The pretrained YOLO model performs object detection.
3. YOLO returns bounding boxes, class IDs, and confidence scores.
4. OpenCV draws the detection results.
5. The application counts detected classes in the current frame.
6. The annotated frame is displayed to the user.

## Important Limitation

The counting module performs per-frame counting. It does not track persistent object identities across frames. Unique-object counting would require an object-tracking algorithm such as ByteTrack or BoT-SORT.

## Learning Outcomes

- Loading a pretrained object-detection model
- Understanding YOLO inference
- Working with image and video input
- Processing webcam frames with OpenCV
- Reading bounding boxes and confidence scores
- Building a basic real-time Computer Vision pipeline