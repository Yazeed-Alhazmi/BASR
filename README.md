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
  
```python
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
<b>YOLOv11m</b> achieved the highest mAP@0.5, mAP@0.5:0.95, and F1 Score, making it the best model for deployment despite slightly higher inference time.<br>

BASR model results:

<div style="display: flex; gap: 20px; justify-content: flex-start;">
  <div align="center">
    <img src="https://github.com/user-attachments/assets/352af93b-4af6-401e-978d-f86ccaf149d4" alt="Training results" width="600"/>
    <p>Results during training</p>
  </div>
  <div align="center">
    <img src="https://github.com/user-attachments/assets/269a2542-ad6a-4573-9bf6-70f62158f7dc" alt="Confusion matrix" width="600"/>
    <p>Confusion matrix</p>
  </div>
     <div align="center">
    <img src="https://github.com/user-attachments/assets/201556d7-ae52-4104-aa36-e80af412978e" alt="Field test" width="600"/>
    <p>Field test</p>
  </div>
</div>

<h2>Download the Trained Model</h2>

You can download the trained model using one of the following methods:

- **Direct download** [link](https://drive.google.com/file/d/1iqVWjKo9MUc5R6eutrZXSccOUCC9IAav/view?usp=share_link)  

- **Using this command in Colab or your terminal**:

```bash
!gdown 1iqVWjKo9MUc5R6eutrZXSccOUCC9IAav
```


<h2>Try BASR</h2>

To set up and run the full BASR system, you will need the following components:

#### 1. Drone Setup
- Use a drone equipped with a 1080p+ camera.
- Configure the drone to stream live video to an RTMP server.

#### RTMP Server Setup
- Install a local RTMP server to receive the live video feed.
- We recommend using this [RTMP server](https://github.com/sallar/mac-local-rtmp-server).
- After installing and starting the server, your RTMP address will typically be:  
  `rtmp://localhost/live/key`

#### 3. Model and Detection System
- Download the trained YOLOv8 model following the instructions in the [Downloading the Trained Model](#-downloading-the-trained-model) section.
- Clone this repository and install the required dependencies:
