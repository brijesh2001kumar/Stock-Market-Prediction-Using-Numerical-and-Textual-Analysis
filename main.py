# Deep learning libraries (Tensorflow Framework)
from tensorflow.keras.models import load_model
import joblib
import numpy as np

# Libraries required for deployment (Done using Streamlit)
import streamlit as st

#settimng up background image for app
st.markdown(
   f'''
   <style>
   .stApp {{
             background: url("https://img.freepik.com/premium-photo/abstract-communication-technology-network-concept_34629-641.jpg?w=1380");
             background-size: cover
         }}
   </style>
   ''',
   unsafe_allow_html=True)

#creating containers for different sections of app
header = st.container()
video = st.container()
input=st.form(key='form')
output=st.container()
model_intro = st.container()
model_details = st.container()
references = st.container()


with header:
    st.title('Stock-Market-Prediction-Using-Numerical-and-Textual-Analysis')
    st.markdown("""---""")
    # col1,col2=st.columns(2)

    st.write('In my project with the Spark Foundation, I used numerical and textual analysis to predict BSE Nifty stock prices. Leveraging libraries like TextBlob and VADER Sentiment, I downloaded and processed data, checked stationarity, and engineered features. This included rolling averages and date-based attributes. I also incorporated news headlines from Tribune, extracting subjectivity and polarity. Merging this with stock data, I built a predictive model using Random Forest Regressor, offering insights into stock price trends.')
    st.image('image.png')
    st.markdown("""---""")
    
with video:

    st.subheader('Video Walkthrough of Project')
    video = open('video_walkthrough.mp4','rb')
    st.video(video)

with model_details:
    st.subheader('Brief Description')
    st.write('**Data Collection:**\n\n This phase involved downloading historical BSE Nifty stock market data and news headlines from Tribune. These datasets were essential for both numerical and textual analysis.\n\n **Numerical Analysis:** \n\nTo ensure the reliability of the stock data, we checked for stationarity, a crucial concept in time series analysis. Additionally, we engineered new numerical features such as rolling averages and incorporated temporal attributes like day of the week, month, and day to enhance our analysis.')
    st.write('**Textual Analysis:**\n\ne explored the textual content of news headlines from Tribune. Using libraries like TextBlob and VADER Sentiment, we calculated subjectivity and polarity scores, providing insights into the sentiment and tone of the news.')
    st.write('**Data Integeration:**\n\nTo create a comprehensive dataset for modeling, we merged the processed stock price data with the enriched news headlines data, allowing us to combine numerical and textual features.')
    st.write('**Model Building:**\n\nFor stock price prediction, we employed a Random Forest Regressor. This machine learning algorithm used our combined dataset to make predictions about future stock prices based on historical data and textual sentiment analysis.')


