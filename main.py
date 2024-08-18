import pyqrcode
import streamlit as st
s1 = "upi://pay?pa=hamala.anbu@okicici&am="
s2 = st.text_input("Enter the Amount")
s3 = "&cu=INR"
s = s1+s2+s3
if st.button("Generate"):
    url = pyqrcode.create(s)  
    url.png('myqr.png', scale = 10) 
    st.image("myqr.png", caption="Generated QR")
