from ultralytics import YOLO
import time
import os
import streamlit as st

class BASR_Model:

    def __init__(self, rtmp_url, detection_time, folder_name=None):
        self.rtmp_url = rtmp_url
        self.detection_time = detection_time
        
        os.makedirs(folder_name)
        self.file_name = f"{folder_name}/frame_"

        self.model = YOLO("/Users/yaz/Downloads/yolov8n.pt")
        
        
    def stream_predictions(self): # the function that start detection and save the detections

        results = self.model.predict(source=self.rtmp_url, stream=True)

        start_time = time.time() # save start time to detects only the required time by the user

        for frame_num, frame_results in enumerate(results):
            if len(frame_results.boxes) > 0:
                conf = float(frame_results.boxes.conf[0]) # take the conf of the frame (to add it to the frame name)
                frame_results.save(filename=self.file_name+f"{frame_num}_{conf:.2f}.jpg")
            if time.time() - start_time > self.detection_time: # If the required time has passed, stop detection
                break