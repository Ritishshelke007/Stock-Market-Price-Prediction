from turtle import speed
import streamlit as st
from PIL import Image
from streamlit_option_menu import option_menu
import json
import requests
from streamlit_lottie import st_lottie

#set page in wide mode
st. set_page_config(layout="wide")


def load_image(image_file):
    img = Image.open(image_file)
    return img

col1 , col2 = st.columns([2,1])

with col1:
    st.header("Welcome to BuyTheDip!")
    st.caption("Predict the Future!")

    def load_lottiefile(filepath: str):
        with open(filepath, "r") as f:
            return json.load(f)

    def load_lottieurl(url : str):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()

    lottie_hello = load_lottieurl("https://assets7.lottiefiles.com/packages/lf20_wh4gk3bb.json")

    st_lottie(
        lottie_hello,
        speed=1,
        reverse=False,
        loop=True,
        quality="low",
        height=400,
        width=500,

    )



with col2:
    select_log = option_menu(
            menu_title = None,
            options=["Login", "Sign up"],
            icons=['box-arrow-in-left','plus-square'],
            orientation="horizontal",
        )


    if select_log == "Login":
        with open('style.css') as f:
            st.markdown(f'<style>{f.read()}<style>',unsafe_allow_html=True)
        #st.markdown("<p style='text-align: left; color: white;'>Enter Email Address</p>", unsafe_allow_html=True)
        email = st.text_input('Enter Email Address')
        password= st.text_input('Enter password',type="password")
        submit = st.button('Log In')

    if select_log =="Sign up":
        name = st.text_input('Full Name')
        email = st.text_input('Email')
        password2 = st.text_input('Enter password',type="password")

        dob = st.date_input('Date Of Birth',value=None)
        image_file = st.file_uploader("Upload Profile", type=["png","jpg","jpeg"])

        if image_file is not None:
            st.image(load_image(image_file),width=250)
        else:
            pass

        st.button('Sign Up')
		





