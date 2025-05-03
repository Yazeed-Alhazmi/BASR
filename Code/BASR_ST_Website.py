import streamlit as st
from ultralytics import YOLO
from PIL import Image
import time
import os
from BASR_M import BASR_Model


st.set_page_config(page_title="BASR", page_icon="", layout="centered")
st.markdown("<h1 style='text-align: center; color: #778da9;'>BASR</h1>", unsafe_allow_html=True)
st.markdown("<h5 style='text-align: center; color: #415a77; margin-top: -25px; margin-bottom: 60px;'>Broad Assistant Search and Rescue</h5>", unsafe_allow_html=True)

st.logo("taibah_logo.png", size='large', link='https://www.taibahu.edu.sa')
st.html("""
        <style>
            [alt=Logo] {
            height: 6rem;
            }
        </style>
    """)

# Let user enter the RTMP URl
rtmp_url = st.text_input("Enter RTMP stream URL:", placeholder="rtmp://127.0.0.1/live/r1zQx9mCJl")
detection_time = st.number_input("Set detection duration (in seconds):", min_value=5, max_value=10000, value=10, step=5)
folder_name = st.text_input("Enter Folder Name:", placeholder="SAR_Mission_001")

# Button to start prediction
if st.button("Start Detection"):
    
    if not rtmp_url:
        st.warning("Please enter RTMP stream URL to continue")
        st.stop() 

    st.info("Starting stream...")

    try:
        model = BASR_Model(rtmp_url, detection_time, folder_name)
        start_time = time.time() # To display a message when detection is done
        results = model.stream_predictions()

    except FileExistsError:
        st.warning("Folder already exists. Please choose a different folder name")
        st.stop()
    except ConnectionError:
        st.warning("Please enter a valid RTMP URL")
        st.stop()
    
    if time.time() - start_time > detection_time:
        st.success("Detection finished")

    image_files = [f for f in os.listdir(folder_name)]
    top_accuracy_images = sorted(image_files, reverse=True, key=lambda x: float(x.split("_")[-1].replace(".jpg", "")))[:9]


    rows = [st.columns(3) for _ in range(3)]  # 3x3 grid

    for idx, img_file in enumerate(top_accuracy_images):
        row = rows[idx // 3]
        col = row[idx % 3]
        with col:
            img_path = os.path.join(folder_name, img_file)
            st.image(Image.open(img_path), caption=img_file, use_container_width=True)










