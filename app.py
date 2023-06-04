import streamlit as st
import joblib
import pandas as pd 
from streamlit_option_menu import option_menu
from PIL import Image
import seaborn as sns
import base64
import pickle
import numpy as np


with st.sidebar:
    selected=option_menu(
    menu_title="Main Menu",
        options=['Home','Wine Prediction'],
        icons=['house','book'],
        styles={
            "container":{"background-color":"#ebb667"},
            "nav-link":{
                "font-size":"21px",
                "--hover-color":"#f2ecb0",
                "color":"#FFFFFF "
            },
            "nav-link-selected":{
                "background-color":"#d65c56"
            },
            "icon":{
                "font-size":"20px"
            },
        },
    )

if selected == 'Home':
    st.markdown("""
    <style>
    .big-font1{
    font-size:50px !important;
    color:#900C3F;
    text-align:center;
    font-weight:bold;
    
    }
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown('<p class="big-font1"> WELCOME TO THE WINE QUALITY PREDICTION SYSTEM </p>',unsafe_allow_html=True)
    file_=open("wine3.png","rb")
    contents=file_.read()
    data_url=base64.b64encode(contents).decode("utf-8")
    file_.close()
    
    st.markdown(' <p class="paragraph"> This system predict the quality of wine on the basis of given features. We use the wine quality dataset available on Internet for free. This dataset has the fundamental features which are responsible for affecting the quality of the wine. By the use of several Machine learning models, we will predict the quality of the wine.  </p>',
    unsafe_allow_html=True)

    st.markdown(
        f'<img src="data:image/gif;base64,{data_url}" width="750" length="500" image-align="center"  alt="wine3">',
        unsafe_allow_html=True, )
    

    

if selected=='Wine Prediction':

    st.markdown("""
    <style>
        .big-font1{
            font-size:50px !important;
            color:red;
            text-align:center;
            font-weight:bold;
    </style>
    """,unsafe_allow_html=True)
    loaded_model=pickle.load(open('wine_quality.sav','rb'))

    def quality_prediction(input_data):
    

        # changing the input_data to numpy array
        input_data_as_numpy_array = np.asarray(input_data)

        # reshape the array as we are predicting for one instance
        input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

        prediction = loaded_model.predict(input_data_reshaped)
        print(prediction)

        if (prediction[0] == 3):
            return 'Quality of Wine is Poor'
        elif (prediction[0]==4):
            return 'Quality of Wine is Average'
        elif (prediction[0]==5):
            return 'Quality of Wine is Good'
        elif (prediction[0]==6):
            return 'Quality of Wine is Fine'
        elif (prediction[0]==7):
            return 'Quality of Wine is Superb'
        else:
            return 'Quality of Wine is Excellent'
    def main(): 


        st.markdown("<h1 style='text-align: center; color: #C70039 ;'>WINE QUALITY PREDICTION SYSTEM</h1>", unsafe_allow_html=True)
        #getting the input data from the user
        co1,col2,col3,col4=st.columns(4)


        with co1:
            fixed_acidity=st.number_input('Enter Fixed Acidity Value',format='%f')
            volatile_acidity=st.number_input('Enter Volatile Acidity Value',format='%f')
            citric_acid=st.number_input('Enter Citric Acid Value',format='%f')

        with col2:
            residual_sugar=st.number_input('Enter Residual Sugar Value',format='%f')
            chlorides=st.number_input('Enter Chlorides Value',format='%f')
            free_sulfur_dioxide=st.number_input('Enter Free Sulphur Dioxide Value',format='%f')


        with col3:
            total_sulfur_dioxide=st.number_input('Enter Total Sulphur Dioxide Value',format='%f')
            density=st.number_input('Enter Density Value',format='%f')
            ph=st.number_input('Enter pH Value',format='%f')

        with col4:
            sulphates=st.number_input('Enter Sulphate Value',format='%f')
            alcohol=st.number_input('Enter Alcohol Value',format='%f')
        #code for the prediction 
        diagnosis=''
        #creating a button for prediction 
        if st.button('Wine Quality Prediction Result'):
            diagnosis = quality_prediction([fixed_acidity,volatile_acidity,citric_acid,residual_sugar,chlorides,free_sulfur_dioxide,total_sulfur_dioxide,density,ph,sulphates,alcohol])
            st.success(diagnosis)
        

    
    if __name__ =='__main__':
        main()










