import cv2
import numpy as np

confidence = 0.4
nms = 0.4

with open('coco.names', 'rt') as f:
    classes = f.read().rstrip('\n').split('\n')

net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg", "darknet")
layernames = net.getUnconnectedOutLayersNames()

def is_person_detected(frame):
    frameHeight = frame.shape[0]
    frameWidth = frame.shape[1]
    classids = []
    confidences = []
    boxes = []
    detected = False

    blob = cv2.dnn.blobFromImage(frame, 1/255.0, (416,416), swapRB=True, crop=False)
    net.setInput(blob)
    outputs = net.forward(layernames)

    for out in outputs:
        for detection in out:
            scores = detection[5:]
            classid = np.argmax(scores)
            conf = scores[classid]
            if conf > confidence:
                center_x = int(detection[0]*frameWidth)
                center_y = int(detection[1]*frameHeight)
                width = int(detection[2]*frameWidth)
                height = int(detection[3]*frameHeight)
                left = int(center_x - width/2)
                top = int(center_y - height/2)
                classids.append(classid)
                confidences.append(float(conf))
                boxes.append([left, top, width, height])

    indices = cv2.dnn.NMSBoxes(boxes, confidences, confidence, nms)

    for i in indices:
        if classids[i] == 0:
            detected = True
            break

    return detected
