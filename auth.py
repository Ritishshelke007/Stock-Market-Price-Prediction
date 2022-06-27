#modules
from matplotlib import image
import pyrebase
import streamlit as st
from datetime import datetime
from PIL import Image
import webbrowser
from streamlit_lottie import st_lottie
import requests
from streamlit_option_menu import option_menu

st.set_page_config(
        page_title="ByTheDip!",
        page_icon="chart_with_upwards_trend",
        layout="wide",
    )


#configuration key 
firebaseConfig = {
  'apiKey': "AIzaSyAsrgdsJKN8ffVcUXz0brFoc2-uKJvHB3g",
 'authDomain': "authentication-88adb.firebaseapp.com",
 ' projectId': "authentication-88adb",
'databaseURL': "https://authentication-88adb-default-rtdb.europe-west1.firebasedatabase.app/",
  'storageBucket': "authentication-88adb.appspot.com",
  'messagingSenderId': "308554439342",
  'appId': "1:308554439342:web:0d3bf8ae1d7b3b1b12ab3f",
 ' measurementId': "G-XGB4TDFYGY"
}

# st.header("Welocme to Search and Predict")
# image = Image.open('Stock-Market-in-india.jpg')


#firebase authentication
firebase = pyrebase.initialize_app(firebaseConfig)
auth= firebase.auth()



# Database

db= firebase.database()
storage= firebase.storage()
# st.sidebar.title("Stock price Prediction")


#authentication
# choice= st.sidebar.selectbox('login/Signup',['Login','Sign up'])
# email = st.sidebar.text_input('please enter your email address')
# password= st.sidebar.text_input('please enter your password',type="password")


#new code starts 
def load_image(image_file):
    img = Image.open(image_file)
    return img

col1 , col2 = st.columns([2,1])

with col1:
    st.header("Welcome to ByTheDip!")
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


    if select_log =='Sign up':
      # handle = st.sidebar.text_input('Please input your app handle name', value= 'Default')
      # submit= st.sidebar.button('Create account')

      #new code starts for sign up
      name = st.text_input('Full Name')
      email = st.text_input('Email')
      password2 = st.text_input('Enter password',type="password")

      dob = st.date_input('Date Of Birth',value=None)
      image_file = st.file_uploader("Upload Profile", type=["png","jpg","jpeg"])

      if image_file is not None:
          st.image(load_image(image_file),width=250)
      else:
          pass

      submit = st.button('Sign Up')
      

      if submit:
        user = auth.create_user_with_email_and_password(email,password2)
        st.success('Your account is created ')
        st.balloons()
    

        # Sign in

        user= auth.sign_in_with_email_and_password(email,password2)
        db.child(user['localId']).child("Handle").set(name)
        db.child(user['localId']).child("ID").set(user['localId'])

        
        st.title('Welcome '+ name)
        st.info('Login via login drop down select')

    if select_log == 'Login':
        with open('style.css') as f:
            st.markdown(f'<style>{f.read()}<style>',unsafe_allow_html=True)
        #st.markdown("<p style='text-align: left; color: white;'>Enter Email Address</p>", unsafe_allow_html=True)
        email = st.text_input('Enter Email Address')
        password= st.text_input('Enter password',type="password")
        submit = st.button('Log In')
      # login= st.sidebar.button('Login')

        if submit:
          user= auth.sign_in_with_email_and_password(email,password)
          webbrowser.open("http://localhost:8502/")
        #   st.success('Logged in')
        #   st.markdown('<a href="https://stock-predict-app.herokuapp.com/" target="_self">Click to continue</a>', unsafe_allow_html=True)
          st.balloons()

