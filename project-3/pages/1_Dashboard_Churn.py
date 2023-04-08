import streamlit as st
import plotly.express as px
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.image as im
st.title("Dashboard - Churn")
st.header("Customer Churn Prediction in Telecom Industry")
telco_data = pd.read_csv('resources/data/WA_Fn-UseC_-Telco-Customer-Churn.csv')
st.dataframe(telco_data)
img = im.imread("resources/images/Web capture_26-2-2023_223210_localhost.jpeg")
churn = st.selectbox("Select yes or no: ", telco_data['Churn'].unique())
#col1, col2,col3 = st.columns(3)
fig_1 = px.histogram(telco_data[telco_data["Churn"] == churn], x = "gender")
st.plotly_chart(fig_1)
fig_2 = px.density_heatmap(telco_data[telco_data["Churn"] == churn], x = "gender")
st.plotly_chart(fig_2)
st.subheader("Let's see histogram of churn depending on gender")
fig_3 = px.histogram(telco_data, x = "gender", color = "Churn",  marginal = "box", color_discrete_sequence=["red","grey"])
st.plotly_chart(fig_3)
st.subheader("Co-relation after cleaning the dataset")
st.image(img)