# Fruit-Segregation-System-Using-Robotic-Arm
An AI-powered fruit segregation system using YOLOv3, OpenCV, Python, and Arduino-based robotic arm automation for real-time fruit detection and sorting.

# Fruit Segregation System Using Robotic Arm

An AI-powered fruit segregation system that combines Computer Vision, YOLOv3, OpenCV, Python, Arduino, and a robotic arm to automatically detect and sort fruits.

## Features

- Fruit detection using YOLOv3
- Real-time object detection with OpenCV
- Arduino-controlled robotic arm
- Automated fruit segregation
- Computer vision and embedded system integration

## Technologies Used

- Python
- OpenCV
- YOLOv3
- Arduino
- NumPy
- PySerial
- Computer Vision
- Robotics

## Project Workflow

1. Camera captures fruit images.
2. YOLOv3 detects and classifies fruits.
3. Python processes detection results.
4. Arduino receives commands via serial communication.
5. Robotic arm performs segregation based on detected fruit.

## Repository Structure

```text
Fruit-Segregation-System-Using-Robotic-Arm/
│
├── Software/
│   ├── Codes/
│   │   ├── python.py
│   │   └── PROJ061.ino
│   │
│   └── yolov3/
│       ├── classes.names
│       ├── coco.names
│       ├── yolov3.cfg
│       └── yolov3_custom.cfg
│
├── Reports/
│   ├── final brown book.pdf
│   └── report_5_sem.pdf
│
├── README.md
├── requirements.txt
└── .gitignore
```

## Dataset

The training dataset is not included in this repository due to size limitations.

## Model Files

YOLO weight files are not included because of GitHub file size restrictions.

## Future Improvements

- Multiple fruit classification
- Improved robotic arm accuracy
- Conveyor belt integration
- Deep learning model upgrades

## Author

Janhavi Unde
