import cv2
import streamlit as st
import time

st.title("Motion Detection")
start = st.button("Start Camera")
time_now = time.strftime("%H:%M:%S")
if start:
    streamlit_image = st.image([])
    camera = cv2.VideoCapture(0)
    
    while True:
        time_now = time.strftime("%H:%M:%S")
        day_of_week = time.strftime("%A")
        check, frame = camera.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        cv2.putText(img=frame, text=day_of_week, org=(50, 50),
                    fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=2, color=(255, 255, 255),
                    thickness=2, lineType=cv2.LINE_AA)
        cv2.putText(img=frame, text=time_now, org=(50, 90),
                    fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=2, color=(10, 100, 200),
                    thickness=2, lineType=cv2.LINE_AA)
        
        streamlit_image.image(frame)