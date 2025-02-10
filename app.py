import streamlit as st
import pandas as pd
import plotly.express as px

# Title of the dashboard
st.title("LiDAR and Mesoscale Data Analysis Dashboard")

# File uploader
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    # Read the uploaded file
    df = pd.read_csv(uploaded_file)

    # Display the uploaded data
    st.write("Uploaded Data:")
    st.write(df.head())

    # Perform analysis (example: correlation matrix)
    st.write("Correlation Matrix:")
    correlation_matrix = df.corr()
    st.write(correlation_matrix)

    # Create a scatter plot (example)
    st.write("Scatter Plot:")
    fig = px.scatter(df, x=df.columns[0], y=df.columns[1], title="LiDAR Height vs Mesoscale Data")
    st.plotly_chart(fig)

    # Additional analysis (example: histogram)
    st.write("Histogram:")
    fig_hist = px.histogram(df, x=df.columns[0], title="Distribution of LiDAR Height")
    st.plotly_chart(fig_hist)
else:
    st.write("Please upload a CSV file to get started.")
