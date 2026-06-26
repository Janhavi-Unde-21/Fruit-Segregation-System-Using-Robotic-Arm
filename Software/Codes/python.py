import numpy as np
import cv2
import serial
import time

# Load YOLOv3 model and configuration
net = cv2.dnn.readNet("E:\\PROJECT\\yolov3\\yolov3.weights", "E:\\PROJECT\\yolov3\\yolov3.cfg")
layer_names = net.getLayerNames()

# Load class names
classes = []
with open("E:\\PROJECT\\yolov3\\coco.names", "r") as f:
    classes = [line.strip() for line in f.readlines()]

# Configure output layers
output_layers = net.getUnconnectedOutLayersNames()

# Open a serial connection to Arduino
arduino = serial.Serial('COM7', 9600, timeout=1)
time.sleep(2)  # Wait for Arduino to initialize

# Capturing video through webcam
webcam = cv2.VideoCapture(1)

# Set up window properties
window_name = "APPLE DETECTION WINDOW"
cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
cv2.resizeWindow(window_name, 800, 600)  # Set window size

object_detected = False
command_sent = False
command_time = 0





while True:
    ret, frame = webcam.read()
    if not ret:
        break

    height, width, channels = frame.shape

    # Preprocess frame
    blob = cv2.dnn.blobFromImage(frame, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
    net.setInput(blob)
    outs = net.forward(output_layers)

    # Initialize variables
    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]

            if confidence > 0.5 and class_id == 47:  # Check if detected object is an apple
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)

                # Extract region of interest (ROI) for the apple
                roi = frame[max(center_y - h // 2, 0): min(center_y + h // 2, height),
                            max(center_x - w // 2, 0): min(center_x + w // 2, width)]
                                # Convert ROI to HSV color space
                hsv_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)

            
                # Calculate total pixels in the ROI
                total_pixels = hsv_roi.shape[0] * hsv_roi.shape[1]

                # Create color masks
                red_mask = cv2.inRange(hsv_roi, np.array([0, 100, 100]), np.array([10, 255, 255])) + \
                           cv2.inRange(hsv_roi, np.array([160, 100, 100]), np.array([180, 255, 255]))

                yellow_mask = cv2.inRange(hsv_roi, np.array([20, 100, 100]), np.array([35, 255, 255]))

                brown_mask = cv2.inRange(hsv_roi, np.array([10, 30, 20]), np.array([30, 100, 80]))

                orange_mask = cv2.inRange(hsv_roi, np.array([10, 100, 20]), np.array([25, 255, 255]))

                red_percentage = (np.count_nonzero(red_mask) / total_pixels) * 100
                yellow_percentage = (np.count_nonzero(yellow_mask) / total_pixels) * 100
                brown_percentage = (np.count_nonzero(brown_mask) / total_pixels) * 100
                orange_percentage = (np.count_nonzero(orange_mask) / total_pixels) * 100



                label = "Fruit"
                if red_percentage > 5:
                    label += " (Apple)"

                # Draw bounding boxes and labels
                font = cv2.FONT_HERSHEY_PLAIN
                color = (0, 255, 0)  # Green color for apple
                cv2.rectangle(frame, (max(center_x - w // 2, 0), max(center_y - h // 2, 0)),
                              (min(center_x + w // 2, width), min(center_y + h // 2, height)), color, 2)
                cv2.putText(frame, label, (max(center_x - w // 2, 0), max(center_y - h // 2, 0) + 30), font, 2, color, 2)

                # Determine if the apple is ripe or unripe and send command to Arduino
                if red_percentage > 5:
                    if not object_detected:
                        command_time = time.time()
                        object_detected = True

                    if object_detected and (time.time() - command_time) >= 5 and not command_sent:
                        arduino.write(b'1')
                        print("Command Sent: 1")
                        command_sent = True
            elif confidence > 0.5 and class_id == 49:  # Check if detected object is an apple
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)

                # Extract region of interest (ROI) for the apple
                roi = frame[max(center_y - h // 2, 0): min(center_y + h // 2, height),
                            max(center_x - w // 2, 0): min(center_x + w // 2, width)]
                                # Convert ROI to HSV color space
                hsv_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)

            
                # Calculate total pixels in the ROI
                total_pixels = hsv_roi.shape[0] * hsv_roi.shape[1]

                # Create color masks
                red_mask = cv2.inRange(hsv_roi, np.array([0, 100, 100]), np.array([10, 255, 255])) + \
                           cv2.inRange(hsv_roi, np.array([160, 100, 100]), np.array([180, 255, 255]))

                yellow_mask = cv2.inRange(hsv_roi, np.array([20, 100, 100]), np.array([35, 255, 255]))

                brown_mask = cv2.inRange(hsv_roi, np.array([10, 30, 20]), np.array([30, 100, 80]))

                orange_mask = cv2.inRange(hsv_roi, np.array([10, 100, 20]), np.array([25, 255, 255]))
                red_percentage = (np.count_nonzero(red_mask) / total_pixels) * 100
                yellow_percentage = (np.count_nonzero(yellow_mask) / total_pixels) * 100
                brown_percentage = (np.count_nonzero(brown_mask) / total_pixels) * 100
                orange_percentage = (np.count_nonzero(orange_mask) / total_pixels) * 100

                label = "Fruit"
                if yellow_percentage > 0.5:
                    label += " (Lemon)"
                elif orange_percentage > 3:
                    label += " (Orange)"

                # Draw bounding boxes and labels
                font = cv2.FONT_HERSHEY_PLAIN
                color = (0, 255, 0)  # Green color for apple
                cv2.rectangle(frame, (max(center_x - w // 2, 0), max(center_y - h // 2, 0)),
                              (min(center_x + w // 2, width), min(center_y + h // 2, height)), color, 2)
                cv2.putText(frame, label, (max(center_x - w // 2, 0), max(center_y - h // 2, 0) + 30), font, 2, color, 2)

                # Determine if the apple is ripe or unripe and send command to Arduino
                if yellow_percentage > 1 or orange_percentage > 4:
                    if not object_detected:
                        command_time = time.time()
                        object_detected = True

                    if object_detected and (time.time() - command_time) >= 5 and not command_sent:
                        arduino.write(b'2')
                        print("Command Sent: 1")
                        command_sent = True

    # Check for response from Arduino
    if command_sent:
        response = arduino.readline().decode('utf-8').strip()
        if response == 'Finished':
            print("Arduino response: Finished")
            object_detected = False
            command_sent = False

    # Display output frame
    cv2.imshow(window_name, frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
webcam.release()
cv2.destroyAllWindows()
arduino.close()
