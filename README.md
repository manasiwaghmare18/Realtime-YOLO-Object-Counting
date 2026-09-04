# 🎯 Real-Time Object Detection & Counting
### YOLOv8 + OpenCV • Image, Video & Webcam Inference

> Turn pixels into insights — detect everyday objects, visualize predictions, count what is visible, and measure real-time performance.

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![YOLOv8](https://img.shields.io/badge/YOLOv8-Ultralytics-111F68?style=for-the-badge)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)
![Status](https://img.shields.io/badge/Status-Working-2ea44f?style=for-the-badge)

---

## ✨ What does this project do?

This project is a hands-on Computer Vision application built with a pretrained **YOLOv8 Nano** model and **OpenCV**. It detects common objects from an image, a stored video, or a live webcam stream.

For every detection, the application can display:

- A **bounding box** showing the location of the object
- The predicted **class name** such as `person`, `cat`, `book`, `bottle`, or `laptop`
- A **confidence score** showing how confident the model is
- A **per-frame class count** in the webcam-counting mode
- An approximate **FPS** value to monitor real-time performance

> **Note:** The counting feature reports objects visible in the current frame. It does not yet track a person or object persistently across frames.

---

## 🧠 System Flow

```text
┌──────────────────────────────┐
│  Image / Video / Live Webcam │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│     OpenCV Input Capture     │
│  Reads image or video frames │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│      YOLOv8 Model Inference  │
│ Detects classes + locations  │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│     Result Post-Processing   │
│ Boxes, labels, confidence,   │
│ counting and FPS calculation │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│      OpenCV Visualization    │
│  Real-time annotated output  │
└──────────────────────────────┘
```

---

## 🚀 Features

| Feature | Description |
|---|---|
| 🖼️ Image detection | Detect objects in a static image and print class, confidence, and box coordinates |
| 🎞️ Video detection | Process a local video frame by frame and display annotated output |
| 📷 Webcam detection | Run live object detection from the default webcam |
| 🔢 Per-frame counting | Count detected object classes visible in each live frame |
| 📦 Bounding boxes | Draw object locations with readable labels |
| 📊 Confidence scores | Show model confidence for each prediction |
| ⚡ FPS monitoring | Display approximate frames per second in the counting application |

----

## 🎬 Live Demo Gallery

The project supports three inference modes: static image detection, recorded-video detection, and live webcam detection with per-frame object counts.

### 🖼️ Image Detection
<img width="394" height="423" alt="Image" src="https://github.com/user-attachments/assets/3d8c362e-7c7b-4225-9f4b-6dd12fb5cf7c" />

*YOLOv8 identifies objects in a static image and returns the class label, confidence score, and bounding-box coordinates.*

---

### 🎞️ Video Detection

https://github.com/user-attachments/assets/63b1dc54-8ced-4174-9c3c-0dd1df37ab11

*The recorded video is processed frame by frame. Each frame passes through the YOLOv8 inference pipeline, and OpenCV displays bounding boxes, class labels, and confidence values in real time.*

---

### 📷 Webcam Detection and Counting

![Webcam detection and counting demo](assets/webcam-counting.png)

*The live webcam pipeline detects visible objects, overlays bounding boxes and confidence scores, counts classes in the current frame, and displays approximate FPS.*
Add your own screenshots or short GIFs to make this section visual. Follow the instructions directly below this gallery to add them safely.



---

## 🗂️ Project Structure

```text
Realtime-YOLO-Object-Counting/
│
├── image_detection.py       # Object detection on a still image
├── video_detection.py       # Frame-by-frame object detection on video
├── webcam_detection.py      # Live webcam object detection
├── webcam_counting.py       # Live detection, per-frame counting, and FPS
├── requirements.txt         # Python dependencies
├── .gitignore               # Excludes local media, model weights, and venv
├── README.md                # Project documentation
└── assets/                  # Demo screenshots/GIFs used in this README
```

---

## 🛠️ Tech Stack

| Tool | Role in this project |
|---|---|
| Python | Application language |
| Ultralytics YOLOv8 | Pretrained deep-learning object-detection model |
| OpenCV | Image/video capture, rendering, drawing, and keyboard input |
| PyTorch | Underlying deep-learning framework used by Ultralytics |
| `collections.Counter` | Per-frame counting of detected object classes |
| `time` | Approximate FPS measurement |

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

### 3. Activate it

```powershell
.\cv-env\Scripts\Activate.ps1
```

If PowerShell blocks the activation script, run this **once** for your Windows user account:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Then activate the environment again.

### 4. Install dependencies

```powershell
pip install -r requirements.txt
```

The pretrained `yolov8n.pt` model downloads automatically the first time you run a script.

---

## ▶️ Run the project

### Image detection

1. Place a test image named `sample.jpg` in the project root, or update the input filename in `image_detection.py`.
2. Run:

```powershell
python image_detection.py
```

### Video detection

1. Place a test video named `vs2.mp4` in the project root, or update the input filename in `video_detection.py`.
2. Run:

```powershell
python video_detection.py
```

### Webcam detection

```powershell
python webcam_detection.py
```

### Webcam detection with per-frame counting

```powershell
python webcam_counting.py
```

Press **`q`** while the OpenCV window is active to exit a video or webcam program.

---

## 🔍 How it works

1. **Capture input:** OpenCV reads an image, a stored video frame, or a webcam frame.
2. **Run inference:** YOLOv8 receives the frame and predicts objects it recognizes.
3. **Extract predictions:** The program reads class IDs, confidence values, and `xyxy` bounding-box coordinates.
4. **Annotate:** OpenCV draws rectangles and labels over the source frame.
5. **Count objects:** `Counter` groups detected labels and calculates the number of objects in the current frame.
6. **Display output:** OpenCV opens a window with the annotated real-time result.

---

## 📌 Understanding the output

A terminal result such as:

```text
Detected: person | Confidence: 0.92 | Box: [101.5, 40.2, 437.8, 478.1]
```

means:

- **person:** The class predicted by the YOLO model
- **0.92:** The confidence score — the model is approximately 92% confident in this detection
- **Box:** The bounding-box coordinates in the format `[x1, y1, x2, y2]`

---

## ⚠️ Current limitations

- This project uses a **pretrained** YOLOv8 model; it does not train a custom model.
- It detects standard COCO dataset classes, so it may not recognize domain-specific objects.
- Per-frame counting is not the same as unique-object counting over time.
- Performance depends on your hardware. CPU inference is typically slower than GPU inference.
- Lighting, object size, camera quality, and occlusion can affect detection quality.

---

## 🔮 Future improvements

- [ ] Add object tracking with ByteTrack or BoT-SORT for persistent IDs
- [ ] Implement unique people/vehicle counting across a virtual line
- [ ] Save annotated webcam/video output to an MP4 file
- [ ] Add a Streamlit dashboard for uploaded image/video inference
- [ ] Export the model to ONNX and benchmark deployment performance
- [ ] Train or fine-tune on a custom dataset for a domain-specific use case
- [ ] Add Docker support for reproducible deployment

---

## 🎓 Key learning outcomes

Through this project, I practiced:

- Using a pretrained deep-learning model for object detection
- Processing images, videos, and live webcam streams
- Working with YOLO class labels, confidence scores, and bounding boxes
- Using OpenCV for visualization and real-time frame processing
- Building a basic end-to-end Computer Vision inference pipeline
- Managing a reproducible Python project with virtual environments, Git, and GitHub

---

## 👤 Author

**Manasi Waghmare**

If you found this project useful, consider giving the repository a ⭐.
