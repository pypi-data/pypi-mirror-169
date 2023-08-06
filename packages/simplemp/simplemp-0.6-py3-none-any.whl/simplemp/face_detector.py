import cv2
import numpy as np
import mediapipe as mp

mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils

__all__ = ["FaceDetector"]


class FaceDetector:
    def __init__(self):
        self.face = None
        self.__load_model()

    def __load_model(self):
        self.face = mp_face_detection.FaceDetection(
            model_selection=0, min_detection_confidence=0.5
        )

    def detect(self, frame, draw=True):
        if self.face is None:
            print("No Model Loaded!")

        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.face.process(image)

        keypoints = []
        bbox = []

        # print("***** results.detections :", results.detections)

        if results.detections:
            for detection in results.detections:

                bb = detection.location_data.relative_bounding_box
                bbox.append((bb.xmin, bb.ymin, bb.width, bb.height))

                facepoints = []
                for point in detection.location_data.relative_keypoints:
                    facepoints.append((point.x, point.y))

                keypoints.append(facepoints)

                if draw:
                    mp_drawing.draw_detection(frame, detection)

        frame = cv2.flip(frame, 1)
        # 인식한 얼굴의 개수만큼 bbox와 keypoints에 따로 저장해서 리턴
        # bbox만 사용하던지, keypoints만 사용하던지
        return frame, bbox, keypoints

    def __del__(self):
        self.__close()

    def __close(self):
        if self.face is not None:
            self.face.close()
