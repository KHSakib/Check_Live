import streamlit as st
import pandas as pd

# Title of the app
st.title("Dataset Uploader")

# File uploader widget
uploaded_file = st.file_uploader("Choose a CSV or Excel file", type=["csv", "xlsx"])

if uploaded_file is not None:
    # Check if the uploaded file is CSV or Excel
    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

    # Display the dataframe
    st.write("Here is your dataset:")
    st.dataframe(df)

    # Display basic statistics
    st.write("Basic Statistics:")
    st.write(df.describe())
