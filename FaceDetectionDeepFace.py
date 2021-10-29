from deepface import DeepFace

models = ["VGG-Face", "Facenet", "Facenet512", "OpenFace", "DeepFace", "DeepID", "ArcFace", "Dlib"]
backends = ['opencv', 'ssd', 'dlib', 'mtcnn', 'retinaface']
metrics = ["cosine", "euclidean", "euclidean_l2"]


def face_detection_df(frame):
    try:
        bbox = DeepFace.detectFace(frame, detector_backend="retinaface")
        return bbox
    except:
        return None

