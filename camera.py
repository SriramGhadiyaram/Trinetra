import cv2
import numpy as np
import winsound

class VideoCamera:
    def __init__(self, socketio):
        self.socketio = socketio
        self.cap = cv2.VideoCapture(0)
        self.net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")

        self.classes = []
        with open("coco.names", "r") as f:
            self.classes = [line.strip() for line in f.readlines()]
        self.layer_names = self.net.getUnconnectedOutLayersNames()

    def __del__(self):
        self.cap.release()

    def get_frame(self):
        ret, frame = self.cap.read()
        height, width, _ = frame.shape

        # Detect people in the frame
        blob = cv2.dnn.blobFromImage(frame, 1/255.0, (416, 416), swapRB=True, crop=False)
        self.net.setInput(blob)
        outs = self.net.forward(self.layer_names)

        class_ids = []
        confidences = []
        boxes = []

        for out in outs:
            for detection in out:
                scores = detection[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]
                if confidence > 0.5:
                    center_x = int(detection[0] * width)
                    center_y = int(detection[1] * height)
                    w = int(detection[2] * width)
                    h = int(detection[3] * height)
                    x = int(center_x - w / 2)
                    y = int(center_y - h / 2)

                    boxes.append([x, y, w, h])
                    confidences.append(float(confidence))
                    class_ids.append(class_id)

        indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

        person_count = 0
        for i in indexes.flatten():
            label = str(self.classes[class_ids[i]])
            if label == "person":
                person_count += 1
                x, y, w, h = boxes[i]
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv2.putText(frame, f'{label}', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

        cv2.putText(frame, f'People: {person_count}', (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

        # Emit alert if person detected
        if person_count > 0:
            self.socketio.emit('alert')
            winsound.Beep(1000, 5000)
        _, jpeg = cv2.imencode('.jpg', frame)
        return jpeg.tobytes()
