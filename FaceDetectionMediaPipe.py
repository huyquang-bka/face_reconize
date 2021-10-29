import mediapipe as mp

mpFaceDetection = mp.solutions.face_detection
mpDraw = mp.solutions.drawing_utils
faceDetection = mpFaceDetection.FaceDetection()


def face_detection_mp(frame, W, H):
    bbox_list = []
    results = faceDetection.process(frame)
    if results.detections:
        for detection in results.detections:
            print(detection.location_data.relative_bounding_box)
            bbox = detection.location_data.relative_bounding_box
            x = int(bbox.xmin * W)
            y = int(bbox.ymin * H)
            w = int(bbox.width * W)
            h = int(bbox.height * H)
            bbox_list.append([x, y, w, h])
    return bbox_list
