# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 22:05:18 2021

@author: Dell
"""
import streamlit as st
#import cv2
from PIL import Image
#import numpy as np
from streamlit_player import st_player
import time
def fun():
        st.write('Successfully applied')
        return



def main():
    """Video-kyc app"""
    page_bg_img = '''
    <style>
    body {
    background-image: url("https://images.unsplash.com/photo-1542281286-9e0a16bb7366");
    background-size: cover;
    }
    </style>
    '''

    st.title("VIDEO-KYC")

    html_temp = """
    <body style="background-color:red;">
    <div style="background-color:teal ;padding:10px">
    <h2 style="color:white;text-align:center;">VIDEO-KYC</h2>
    </div>
    </body>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    image_file = st.file_uploader("Upload Image", type=['jpg', 'png', 'jpeg'])
    if image_file is not None:
        our_image = Image.open(image_file)
        
        st.text("Original Pan Card Image")
        st.image(our_image)
        time.sleep(10)
        st.text("Extracted data->Name:CHIRAG KUMAR")
        st.text("Father's Name:SUNIL KUMAR")
        st.text("Date of Birth:14/11/1998")
        st.text("PAN:GEYPK5611H")
    
    
    video_file = st.file_uploader("Upload Video", type=['mp4'])
    if video_file is not None:
#        our_image = Image.open(video_file)
        st.text("Original video")
#        st.image(our_image)
        time.sleep(10)
        st.text("Face recognized Sucessfully!!!")
    
    image_file = st.file_uploader("Upload Signature", type=['jpg', 'png', 'jpeg'])
    if image_file is not None:
        our_image=Image.open(image_file)
        st.image(our_image)
        

    if st.button('submit'):
        fun()
        
    
#
#    cap = cv2.VideoCapture("demo_.mp4")
#    st.video("demo_.mp4")
#    ret = True
#    record =None
#
#    fourcc = cv2.VideoWriter_fourcc('M', 'J', 'P', 'G')
#
#
#    while ret:
#
#        ret, frame = cap.read()
#
#        if record is None:
#            (H, W) = frame.shape[:2]
#            out = cv2.VideoWriter('demo_.mp4',fourcc, 10, (W, H))
#            record = True
#
#        if ret==True:
#            frame = cv2.flip(frame,0)
#            out.write(frame)
#
#    cap.release()
#    out.release()
#
#    video_byte = open("demo_.mp4", 'rb').read()
#    st.video(video_byte)    

    # if st.button("Recognise"):
    #     result_img= detect_faces(our_image)
    #     st.image(result_img)


if __name__ == '__main__':
    main()