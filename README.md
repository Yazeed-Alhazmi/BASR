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

- <b>Dataset:</b> drone images filtered to contain only the "person" class from [VisDrone](https://github.com/VisDrone/VisDrone-Dataset) dataset.<br>
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
version = project.version(1)
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
- <b>Inference speed</b> (ms/image)<br>



| Model    | mAP@0.5 | mAP@0.5:0.95 | F1 Score | Inference Time (ms/image) |
|:---------|:-------:|:------------:|:--------:|:-------------------------:|
| YOLOv8n  |  0.641  |     0.279    |   0.66   |           1.7             |
| YOLOv8m  |  0.664  |     0.327    |   0.69   |           9.8             |
| YOLOv11n |  0.612  |     0.267    |   0.65   |           1.8             |
| YOLOv11m |  0.682  |     0.338    |   0.71   |          10.7    

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

<h2>Download BASR Model</h2>

You can download the trained model using one of the following methods:

- **Direct download** [link](https://drive.google.com/file/d/1iqVWjKo9MUc5R6eutrZXSccOUCC9IAav/view?usp=share_link)  

- **Using this command in Colab or your terminal**:

```bash
!gdown 1iqVWjKo9MUc5R6eutrZXSccOUCC9IAav
```


<h2>Try BASR</h2>

<div style="display: flex; gap: 20px; justify-content: flex-start;">
  <div align="center">
    <img src="https://github.com/user-attachments/assets/d3660f72-b5a0-4673-80e6-4bfbb951008f" alt="BASR Full System" width="600"/>
    <p>BASR Full System</p>
  </div>
</div>

To set up and run the full BASR system, you will need the following components:

#### 1. Drone Setup
- Use a drone equipped with a 1080p+ camera.
- Configure the drone to stream live video to an RTMP server.

#### 2. RTMP Server Setup
- Install a local RTMP server to receive the live video feed.
- We recommend using this [RTMP server](https://github.com/sallar/mac-local-rtmp-server).
- After installing and starting the server, your RTMP address will typically be:  
  `rtmp://localhost/live/key`

#### 3. Model and Detection System
- Download BASR model following the instructions in the [Download BASR Model](#download-basr-model) section.
- Clone this repository and install the required dependencies:
```bash
git clone https://github.com/Yazeed-Alhazmi/BASR.git
cd BASR
pip install -r requirements.txt
```

- Start the detection system using Streamlit:
```bash
streamlit run BASR_ST_Website.py
```
- You will get this interface:
<div style="display: flex; gap: 20px; justify-content: flex-start;">
  <div align="center">
    <img src="https://github.com/user-attachments/assets/b868bd14-5a4f-4f29-aecf-9c1c4c5f0dbd" alt="BASR Interface" width="900"/>
    <p>BASR Interface</p>
  </div>
</div>

- Enter your RTMP URL, required detection time, and folder name (detected frames will be saved to this folder).

- After detection, you will see the top 9 detected frames in term of accuracy as we see here:
<div style="display: flex; gap: 20px; justify-content: flex-start;">
  <div align="center">
    <img src="https://github.com/user-attachments/assets/229977fe-6c5d-41bc-9cee-c3903cdb8564" alt="BASR Interface after detection" width="900"/>
    <p>BASR Interface After Detection</p>
  </div>
</div>


<h2>Try BASR without a drone</h2>

For testing the BASR system without a drone, you can provide an **image path** or a **folder path containing images** instead of an RTMP URL.

This allows you to simulate the system behavior and test the detection model easily without requiring a live video stream.

Simply enter the input source in your Streamlit app:
- A single image: `"/path/to/your/image.jpg"`
- A folder of images: `"/path/to/your/images_folder"`

The detection model will process the provided images just like it would

<div style="display: flex; gap: 20px; justify-content: flex-start;">
  <div align="center">
    <img src="https://github.com/user-attachments/assets/977abba6-9ca2-4b3f-8291-edf6b0ae089c" alt="BASR Interface after detection using an image folder" width="900"/>
    <p>BASR Interface After Detection Using A Folder of Images</p>
  </div>
</div>
