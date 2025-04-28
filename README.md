<h1>BASR: Broad Assistance Search and Rescue</h1>

This project implements a drone-based AI system to assist in search and rescue (SAR) missions, specifically focused on locating lost individuals in desert environments.

By combining a drone equipped with a high-resolution camera and an object detection model (YOLOv11m), BASR enhances traditional rescue missions with real-time detection.

<h2>System Overview</h2>

- <b>Drone:</b><br>
   - Captures real-time 1080p 30FPS aerial video using a high-resolution camera.<br>
   - Streams the live video feed to the ground system via an RTMP protocol.<br>
   
- <b>Ground System:</b><br>
  - <b>RTMP Server:</b> Acts as the bridge between the drone and the detection system.<br>
  - <b>Detection Model:</b> A YOLOv11m model processes incoming frames in real time.<br>
  - <b>Website (Streamlit Interface):</b> Allows the rescue team to interact with the system, Displays detected individuals, manages the RTMP stream connection, and shows the top detected frames.<br>

<h2>Dataset Preparation Stage</h2>

- <b>Dataset:</b> drone images filtered to contain only the "person" class.<br>
- <b>Tool:</b> <a href="https://app.roboflow.com">Roboflow</a> was used for labeling, augmentation, and splitting into training/validation sets.<br>
- <b>Training dataset:</b> 5,351 training images + 436 validation images.<br>
- <b>test dataset:</b> 100 test images selected to cover all possible scenarios.<br>
   
- <b>Ground System:</b><br>
  - <b>RTMP Server:</b> Acts as the bridge between the drone and the detection system.<br>
  - <b>Detection Model:</b> A YOLOv11m model processes incoming frames in real time.<br>
  - <b>Website (Streamlit Interface):</b> Allows the rescue team to interact with the system, Displays detected individuals, manages the RTMP stream connection, and shows the top detected frames.<br>
  
  Due to their large size, you can download both datasets using the following code:
  
```
#Training dataset:
!pip install roboflow

from roboflow import Roboflow
rf = Roboflow(api_key="YOUR_API_KEY")
project = rf.workspace("basr").project("basr_v1")
version = project.version(1)
dataset = version.download("yolov11m") # Or any yolo version

#Test dataset:
!pip install roboflow

from roboflow import Roboflow
rf = Roboflow(api_key="YOUR_API_KEY")
project = rf.workspace("basr").project("basr_test")
version = project.version(12)
dataset = version.download("yolov11m") # Or any yolo version
```

