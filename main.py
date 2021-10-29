import cv2
# from FaceDetectionMediaPipe import *
from FaceDetectionDeepFace import *
import time

video_path = "akshay_mov.mp4"
cap = cv2.VideoCapture(video_path)
print(cap.get(cv2.CAP_PROP_FPS))
while True:
    s = time.time()
    ret, frame = cap.read()
    face = face_detection_df(frame)
    cv2.imshow("Frame", frame)
    if face is not None:
        print(face.shape)
        face = cv2.cvtColor(face, cv2.COLOR_RGB2BGR)
        cv2.imshow("Face", face)
    key = cv2.waitKey(int(1000 / 24 - (time.time() - s)))
    print(1 // (time.time() - s))
    if key == ord("q"):
        break
