import cv2
import numpy as np

video_path = "recorded.MOV"
cap = cv2.VideoCapture(video_path)

decoded_texts = set()
frame_number = 0
detector = cv2.QRCodeDetector()

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame_number += 1
    height, width, _ = frame.shape

    crop_size = min(width, height) // 3
    x_offset = width - crop_size
    y_offset = height - crop_size
    crop_frame = frame[y_offset:height, x_offset:width]

    gray = cv2.cvtColor(crop_frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.equalizeHist(gray)

    for scale in [2, 3, 4]:
        resized = cv2.resize(gray, None, fx=scale, fy=scale, interpolation=cv2.INTER_CUBIC)
        data, bbox, _ = detector.detectAndDecode(resized)
        if data and data not in decoded_texts:
            print(f"Frame {frame_number}, Scale {scale}: {data}")
            decoded_texts.add(data)
            cap.release()  
            print("Decoding finished. Found messages:", decoded_texts)
            exit()  

print("Decoding finished. Found messages:", decoded_texts)
