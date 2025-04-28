<h1>BASR: Broad Assistance Search and Rescue</h1>

This project implements a drone-based AI system to assist in search and rescue (SAR) missions, specifically focused on locating lost individuals in desert environments.

By combining a drone equipped with a high-resolution camera and an object detection model (YOLOv11m), BASR enhances traditional rescue missions with real-time detection

<h2>System Overview</h2>
- <b>Drone:</b><br>
   - Captures real-time 1080p 30FPS aerial video using a high-resolution camera.<br>
   - Streams the live video feed to the ground system via an RTMP protocol.<br>
   
- <b>Ground System:</b><br>
  - <b>RTMP Server:</b> Acts as the bridge between the drone and the detection system.<br>
  - <b>Detection Model:</b> A YOLOv11m model processes incoming frames in real time.<br>
  - <b>Website (Streamlit Interface):</b> Allows the rescue team to interact with the system, Displays detected individuals, manages the RTMP stream connection, and shows the top detected frames.<br>


