#modules
from matplotlib import image
import pyrebase
import streamlit as st
from datetime import datetime
from PIL import Image


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

st.header("Welocme to Search and Predict")
image = Image.open('Stock-Market-in-india.jpg')


#firebase authentication
firebase = pyrebase.initialize_app(firebaseConfig)
auth= firebase.auth()



# Database

db= firebase.database()
storage= firebase.storage()
st.sidebar.title("Stock price Prediction")


#authentication
choice= st.sidebar.selectbox('login/Signup',['Login','Sign up'])
email = st.sidebar.text_input('please enter your email address')
password= st.sidebar.text_input('please enter your password',type="password")

if choice =='Sign up':
  handle = st.sidebar.text_input('Please input your app handle name', value= 'Default')
  submit= st.sidebar.button('Create account')
  

  if submit:
    user = auth.create_user_with_email_and_password(email,password)
    st.success('Your account is created ')
    st.balloons()
 

    # Sign in

    user= auth.sign_in_with_email_and_password(email,password)
    db.child(user['localId']).child("Handle").set(handle)
    db.child(user['localId']).child("ID").set(user['localId'])

    
    st.title('Welcome '+ handle)
    st.info('Login via login drop down select')

if choice == 'Login':
  login= st.sidebar.button('Login')
  if login:
    user= auth.sign_in_with_email_and_password(email,password)
    
    st.success('Logged in')
    st.balloons()