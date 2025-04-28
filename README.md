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

<h2>Training Stage</h2>
After preparing the dataset, we experimented with training multiple YOLO models to determine the best-performing one for our application.

- <b>Trained Models:</b> YOLOv8n, YOLOv8m, YOLOv11n, YOLOv11m<br>
- <b>Optimizer:</b> AdamW<br>
- <b>Epochs:</b> 100<br>
- <b>Batch Size:</b> 16<br>
- <b>Framework:</b> <a href="https://docs.ultralytics.com">Ultralytics</a><br>
- <b>Environment:</b> <a href="https://colab.research.google.com">Google Colab</a><br>

<h2>Validation and Results</h2>

Each model was evaluated based on:<br>
- <b>Mean Average Precision:</b> mAP@0.5 and mAP@0.5:0.95<br>
- <b>F1 Score</b><br>
- <b>Inference speed</b> (Image/ms)<br>



| Model    | mAP@0.5 | mAP@0.5:0.95 | F1 Score | Inference Time (ms/image) |
|:---------|:-------:|:------------:|:--------:|:-------------------------:|
| YOLOv8n  |  0.641  |     0.279    |   0.66   |           1.7             |
| YOLOv8m  |  0.664  |     0.327    |   0.69   |           9.8             |
| YOLOv11n |  0.612  |     0.267    |   0.65   |           1.8             |
| YOLOv11m |  0.682  |     0.338    |   0.70   |          10.7    

<br>
<b>Selected BASR model:</b><br>
   - <b>YOLOv11m</b> achieved the highest mAP@0.5, mAP@0.5:0.95, and F1 Score, making it the best model for deployment despite slightly higher inference time.

