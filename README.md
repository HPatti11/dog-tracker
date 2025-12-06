# 🐶 YOLOv5 Live Webcam Object Detection

This project runs a **real-time object detector** using a webcam and the YOLOv5 deep learning model.  
It can recognize common objects such as dogs, people, cars, and more — directly from your camera feed.

---

## 📌 Features
- Real-time camera input  
- Uses YOLOv5 (small version — fast and lightweight)  
- Draws bounding boxes around detected objects  
- Beginner-friendly and easy to modify

---

## 📸 How It Works
1. The program loads YOLOv5s (small model) using PyTorch.
2. It opens your computer’s default webcam.
3. Each video frame is passed into YOLOv5.
4. The model returns predictions (objects + confidence scores).
5. The results are drawn on top of the video stream so you can see detections in real time.

➡️ Press **Q** to exit the live window.

---

## 🧰 Requirements

Make sure Python 3.7+ is installed.

Install required packages:

```bash
pip install torch torchvision opencv-python pillow numpy
