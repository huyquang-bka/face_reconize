import cv2
from FaceDetectionDeepFace import *

video_path = "FaceVideoData/Quang.mp4"
name = video_path.split("/")[1].split(".")[0].lower()
cap = cv2.VideoCapture(video_path)
length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
count = 0
while True:
    ret, frame = cap.read()
    bbox = face_detection_df(frame)
    if bbox is not None:
        count += 1
        x, y, w, h = bbox
        face = frame[y:y + h, x:x + w]
        cv2.imwrite(f"FaceDataImage/{name}/{count}.jpg", face)
        cv2.imshow("Face", face)
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1)
    if key == ord("q"):
        break
