# 🎯 Real-Time Object Detection & Counting
### YOLOv8 + OpenCV • Image, Video, and Live Webcam Inference

> A hands-on Computer Vision project that converts images and video frames into real-time object detections using YOLOv8 and OpenCV.

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![YOLOv8](https://img.shields.io/badge/YOLOv8-Ultralytics-111F68?style=for-the-badge)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)
![Status](https://img.shields.io/badge/Status-Working-2ea44f?style=for-the-badge)

---

## ✨ Overview

This project is a practical Computer Vision application built with a pretrained **YOLOv8 Nano** model and **OpenCV**. It performs object detection on three input types:

- Static images
- Recorded video files
- Live webcam streams

For every recognized object, the application extracts and visualizes:

- A **bounding box** that identifies the object location
- A predicted **class label**, such as `person`, `car`, `bus`, `book`, `bottle`, or `backpack`
- A **confidence score** for the prediction
- **Per-frame object counts** in the webcam-counting mode
- Approximate **FPS** for monitoring local real-time performance

> **Important:** The webcam counting feature counts objects visible in the current frame. It does not currently assign persistent IDs or calculate unique object counts across multiple frames.

---

## 🧠 System Flow

```text
┌──────────────────────────────┐
│  Image / Video / Live Webcam │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│      Input Frame Capture     │
│  OpenCV reads image / frames │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│      YOLOv8 Model Inference  │
│  Classes, boxes, confidence  │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│      Post-Processing Layer   │
│ Labels, boxes, counts, FPS   │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│      OpenCV Visualization    │
│  Annotated real-time output  │
└──────────────────────────────┘
```

---

## 🚀 Features

| Feature | Description |
|---|---|
| 🖼️ Image detection | Detects objects in a static image and prints the class label, confidence score, and bounding-box coordinates |
| 🎞️ Video detection | Processes a local video frame by frame and displays annotated detections |
| 📷 Webcam detection | Runs live object detection using the default system webcam |
| 🔢 Per-frame counting | Counts detected classes that are visible in the current webcam frame |
| 📦 Bounding boxes | Draws object-location boxes and readable labels on the frame |
| 📊 Confidence scores | Displays model confidence for every detected object |
| ⚡ FPS monitoring | Displays approximate frames per second in the webcam-counting application |

---

## 🎬 Live Demo Gallery

The project supports static image inference, recorded road-scene video inference, and live webcam detection with per-frame object counting.

### 🖼️ Image Detection

<img width="394" height="423" alt="Image" src="https://github.com/user-attachments/assets/3d8c362e-7c7b-4225-9f4b-6dd12fb5cf7c" />

*YOLOv8 detects recognizable objects in a static image and returns their class labels, confidence values, and bounding-box coordinates.*

---

### 🎞️ Video Detection

[https://github.com/user-attachments/assets/63b1dc54-8ced-4174-9c3c-0dd1df37ab11](https://github.com/user-attachments/assets/63b1dc54-8ced-4174-9c3c-0dd1df37ab11)

*The recorded road-scene video is processed sequentially, frame by frame. YOLOv8 detects objects such as people, cars, buses, trucks, trains, and traffic lights, while OpenCV renders the bounding boxes, class labels, and confidence scores.*

---

### 📷 Webcam Detection and Per-Frame Counting

[https://github.com/user-attachments/assets/8b9707ec-34d0-4944-961b-83251ea7c7fe](https://github.com/user-attachments/assets/8b9707ec-34d0-4944-961b-83251ea7c7fe)

*The live webcam pipeline detects visible objects, overlays bounding boxes, class labels, and confidence scores, reports object counts for the current frame, and displays approximate FPS.*

---

## 🗂️ Project Structure

```text
Realtime-YOLO-Object-Counting/
│
├── image_detection.py       # Object detection on a static image
├── video_detection.py       # Frame-by-frame inference on a local video
├── webcam_detection.py      # Real-time object detection from webcam
├── webcam_counting.py       # Webcam detection, per-frame counting, and FPS
├── requirements.txt         # Project dependencies
├── .gitignore               # Excludes local media, model weights, and virtual environment
├── README.md                # Project documentation
└── assets/                  # Optional images/GIFs used in README
```

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| Python | Primary programming language |
| Ultralytics YOLOv8 | Pretrained deep-learning model for object detection |
| OpenCV | Image/video capture, frame display, annotation, and keyboard input |
| PyTorch | Deep-learning framework used by the Ultralytics implementation |
| `collections.Counter` | Counts detected object classes in the current webcam frame |
| `time` | Calculates approximate FPS |

---

## ⚙️ Setup on Windows

### 1. Clone the repository

```powershell
git clone https://github.com/manasiwaghmare18/Realtime-YOLO-Object-Counting.git
cd Realtime-YOLO-Object-Counting
```

### 2. Create a virtual environment

```powershell
python -m venv cv-env
```

### 3. Activate the environment

```powershell
.\cv-env\Scripts\Activate.ps1
```

If PowerShell blocks the activation script, run this command once for your Windows user account:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Then activate the environment again.

### 4. Install dependencies

```powershell
pip install -r requirements.txt
```

The pretrained `yolov8n.pt` model downloads automatically the first time you run an inference script.

---

## ▶️ Run the project

### Image detection

1. Place a test image named `sample.jpg` in the project root, or update the image filename inside `image_detection.py`.
2. Run:

```powershell
python image_detection.py
```

### Video detection

1. Place a test video named `vs4.mp4` in the project root, or update `VIDEO_PATH` inside `video_detection.py`.
2. Run:

```powershell
python video_detection.py
```

### Live webcam detection

```powershell
python webcam_detection.py
```

### Webcam detection with per-frame counting

```powershell
python webcam_counting.py
```

Press **`q`** while an OpenCV window is active to stop the video or webcam application.

---

## 🔍 How it works

1. **Read input:** The application receives a static image, a local video frame, or a live webcam frame.
2. **Run inference:** YOLOv8 analyzes the frame and returns detections for supported object classes.
3. **Extract results:** The code reads class IDs, confidence scores, and bounding-box coordinates in `xyxy` format.
4. **Draw annotations:** OpenCV draws the boxes and object labels over the source frame.
5. **Calculate frame counts:** In `webcam_counting.py`, `Counter` groups detected labels and counts them for the current frame.
6. **Display output:** OpenCV shows the annotated image, video frame, or webcam stream in a local window.

---

## 📌 Understanding a detection

Example terminal output:

```text
Detected: person | Confidence: 0.92 | Box: [101.5, 40.2, 437.8, 478.1]
```

| Output part | Meaning |
|---|---|
| `person` | Class label predicted by YOLOv8 |
| `0.92` | Confidence score; the model is highly confident in this prediction |
| `[x1, y1, x2, y2]` | Bounding-box coordinates: left, top, right, and bottom points |

---

## ⚠️ Current limitations

- The project uses a **pretrained YOLOv8 Nano model** and does not train a custom model.
- It supports the standard object classes learned from the COCO dataset, not domain-specific categories.
- Webcam counts are **per-frame** and are not unique counts across an entire video stream.
- Object tracking, persistent IDs, and line-crossing analytics are not implemented yet.
- Results can vary with lighting, occlusion, image quality, object scale, and camera angle.
- Inference speed depends on local hardware; CPU inference is usually slower than GPU inference.

---

## 🔮 Future Improvements

- [ ] Add object tracking with ByteTrack or BoT-SORT
- [ ] Add unique person/vehicle counting across a virtual line
- [ ] Save annotated video/webcam output as MP4
- [ ] Build a Streamlit interface for uploading images and videos
- [ ] Export the model to ONNX and compare inference performance
- [ ] Fine-tune YOLO on a custom domain-specific dataset
- [ ] Add Docker support for reproducible setup and deployment

---

## 🎓 Key Learning Outcomes

Through this project, I practiced:

- Using a pretrained deep-learning model for object detection
- Processing static images, recorded videos, and live webcam streams
- Working with YOLO class IDs, bounding boxes, and confidence scores
- Using OpenCV for visualization and real-time frame processing
- Implementing per-frame object counting and approximate FPS measurement
- Building a complete Computer Vision inference pipeline
- Managing a reproducible Python project with virtual environments, Git, and GitHub

---

## 👤 Author

**Manasi Waghmare**

If you find this project useful, consider giving the repository a ⭐.