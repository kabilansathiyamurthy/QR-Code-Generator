import pyqrcode
import streamlit as st
a = st.number_input("Pen Count")
s2 = a*5
c = str(s2)
if st.button("Close the Bill"):
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.write('Sl.No')
    with col2:
        st.write('Description')
    with col3:
        st.write('Rate')
    with col4:
        st.write('QTY')
    with col5:
        st.write('Amount')
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.write('1')
    with col2:
        st.write('Pen')
    with col3:
        st.write('5.00')
    with col4:
        st.write(a)
    with col5:
        st.write(s2)
    s1 = "upi://pay?pa=saji.diya24@okaxis&am="
    s3 = "&cu=INR"
    s = s1+c+s3
    url=pyqrcode.create(s)
    url.png('myqr.png',scale=10)
    st.image("myqr.png",caption="generated QR")
