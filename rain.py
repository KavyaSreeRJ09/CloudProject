import numpy as np
import pandas as pd
from xgboost import XGBClassifier
import pickle
import streamlit as st

model=pickle.load(open('xgb.pkl', 'rb'))

st.title("Rainfall Prediction App")
location =st.sidebar.slider("Location",1,26,1)
minTemp=st.sidebar.slider("minTemp", -5.0, 20.0, step=1.0) 
maxTemp=st.sidebar.slider("maxTemp", 0.0, 40.0, step=1.0) 
rainfall=st.sidebar.slider("Rainfall",0.0,5.0,step=0.1)
evaporation=st.sidebar.slider("evaporation", 0.0, 15.0, step=1.0) 
sunshine=st.sidebar.slider("sunshine", 0.0, 15.0, step=1.0) 

windGustDir=st.sidebar.slider("windGustDir", 0.0, 15.0, step=1.0)
windGustSpeed=st.sidebar.slider("windGustSpeed", 20.0, 80.0, step=1.0) 
winddDir9am=st.sidebar.slider("windGustDir9am", 0.0, 20.0, step=1.0)
winddDir3pm=st.sidebar.slider("windGustDir3pm", 0.0, 15.0, step=1.0) 
windSpeed9am=st.sidebar.slider("Wind Speed 9am", 0.0, 30.0, step=1.0) 
windSpeed3pm=st.sidebar.slider("Wind Speed 3pm", 0.0, 40.0, step=1.0) 

humidity9am=st.sidebar.slider("humidity 9 am", 0.0, 100.0, step=1.0) 
humidity3pm=st.sidebar.slider("humidity 3pm", 0.0, 100.0, step=1.0)

pressure9am=st.sidebar.slider("pressure 9am", 1000.0, 1020.0, step=1.0)  
pressure3pm=st.sidebar.slider("pressure 3pm", 1000.0, 1020.0, step=1.0)  
cloud9am=st.sidebar.slider("cloud 9am", 0.0, 10.0, step=1.0) 
cloud3pm=st.sidebar.slider("cloud 3pm", 0.0, 10.0, step=1.0) 
temp9am=st.sidebar.slider("temp 9am", 0.0, 30.0, step=1.0) 
temp3pm=st.sidebar.slider("temp 3pm", 0.0, 40.0, step=1.0) 
rainToday=st.sidebar.slider("rainToday", 0.0, 1.0, step=1.0) 
month=st.sidebar.selectbox("month",['',1,2,3,4,5,6,7,8,9,10,11,12])
date=st.sidebar.slider("Day",1,31,1)

df2=pd.DataFrame(data=[[location, minTemp, maxTemp, rainfall, evaporation, sunshine, windGustDir, windGustSpeed, winddDir9am, winddDir3pm, windSpeed9am, windSpeed3pm,humidity9am,humidity3pm, pressure9am,pressure3pm, cloud9am,cloud3pm,temp9am,temp3pm, rainToday, month, date]],columns=['Location', 'MinTemp', 'MaxTemp', 'Rainfall', 'Evaporation', 'Sunshine',
       'WindGustDir', 'WindGustSpeed', 'WindDir9am', 'WindDir3pm',
       'WindSpeed9am', 'WindSpeed3pm', 'Humidity9am', 'Humidity3pm',
       'Pressure9am', 'Pressure3pm', 'Cloud9am', 'Cloud3pm', 'Temp9am',
       'Temp3pm', 'RainToday', 'Date_month', 'Date_day'])

if st.button("Predict"):
    prediction=model.predict(df2)
    if prediction==0 :
        st.success("Not Raining")
    else:
        st.error("Raining")

