# Trinetra
object detection model 
# 👁️‍🗨️ Trinetra – Real-Time Human Detection Surveillance System

Welcome to **Trinetra**, a smart surveillance system that detects humans using YOLO and OpenCV via a live webcam feed. Whether it's for restricted areas, home security, or just fun ML experimentation, Trinetra gives you a simple web interface to monitor and be alerted when someone is detected.

---

## 🚀 Features

- 🔍 Real-time **person detection** using YOLOv3-
- 📷 Live webcam feed via a Flask web interface
- 🛑 Alert mechanism (beep sound or browser popup) when a person is detected
- 🧠 Built using Python, OpenCV, Flask, and Socket.IO
- 🎵 Optional audio alert system for real-time notification
- 👥 Counts number of people and displays it on the feed
- 💡 Easy to customize and extend

---

## 🛠️ Tech Stack

- **Backend:** Python, Flask, OpenCV, Flask-SocketIO
- **Frontend:** HTML, JavaScript
- **AI Model:** YOLOv3- for lightweight real-time person detection

---

### 1. Clone the repository
```bash
git clone https://github.com/SriramGhadiyaram/trinetra.git
cd trinetra
### **2. Download YOLOv3 weights and config**

Place the following files in your project root:

- `yolov3.cfg`  
- `yolov3.weights`  
- `coco.names` (which contains class labels, like "person")

You can download them from:
- [**YOLOv3 Config**](https://github.com/pjreddie/darknet/blob/master/cfg/yolov3.cfg)
- [**YOLOv3 Weights**](https://pjreddie.com/media/files/yolov3.weights)
- [**COCO Names File**](https://github.com/pjreddie/darknet/blob/master/data/coco.names)
