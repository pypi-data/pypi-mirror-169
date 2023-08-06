import cv2
import numpy as np
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_pose = mp.solutions.pose


__all__ = ["PoseDetector"]


class PoseDetector:
    def __init__(self):
        self.pose = None
        self.__load_model()

    def __load_model(self):
        self.pose = mp_pose.Pose(
            min_detection_confidence=0.5, min_tracking_confidence=0.5
        )

    def detect(self, frame, draw=True):
        if self.pose is None:
            print("No Model Loaded!")

        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.pose.process(image)

        keypoints = []

        for lmk in results.pose_landmarks.landmark:
            keypoints.append((lmk.x, lmk.y, lmk.z, lmk.visibility))

        if draw:
            mp_drawing.draw_landmarks(
                frame,
                results.pose_landmarks,
                mp_pose.POSE_CONNECTIONS,
                landmark_drawing_spec=mp_drawing_styles.get_default_pose_landmarks_style(),
            )

        frame = cv2.flip(frame, 1)
        return frame, keypoints

    def __del__(self):
        self.__close()

    def __close(self):
        if self.pose is not None:
            self.pose.close()
