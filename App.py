import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Set up the app title and image
st.title("Comprehensive Data Visualization and Analysis App")
st.image("https://diggrowth.com/wp-content/uploads/2024/02/AI-Data-Visualization-Tool_-Improve-Your-Insights-1.png")

# File uploader for multiple file types
uploaded_file = st.file_uploader("Upload a Data File (CSV, Excel, JSON)", type=["csv", "xlsx", "json"])

if uploaded_file is not None:
    try:
        # Load the data based on file type
        if uploaded_file.name.endswith('.csv'):
            df = pd.read_csv(uploaded_file)
        elif uploaded_file.name.endswith('.xlsx'):
            df = pd.read_excel(uploaded_file)
        elif uploaded_file.name.endswith('.json'):
            df = pd.read_json(uploaded_file)
        else:
            st.error("Unsupported file format. Please upload a CSV, Excel, or JSON file.")
            df = None
    except Exception as e:
        st.error(f"Error reading the file: {e}")
        df = None

    if df is not None and not df.empty:
        # Display a preview of the data
        st.subheader("**Data Overview:**")
        st.write("Here is a preview of the first few rows of your dataset:")
        st.write(df.head())

        # Provide a summary of the data
        st.subheader("**Statistical Summary of the Dataset:**")
        st.write("This section provides a statistical summary of the numerical columns:")
        st.write(df.describe())

        # Detailed column analysis
        st.subheader("**Detailed Column Information:**")
        st.write("Search for a specific column to get detailed information such as length, missing values, and basic statistics:")
        search_column = st.text_input("Enter column name for detailed analysis")

        if search_column:
            if search_column in df.columns:
                st.write(f"Length of column '{search_column}': {len(df[search_column])}")
                st.write(f"Number of missing values in '{search_column}': {df[search_column].isnull().sum()}")
                st.write(f"Number of unique values in '{search_column}': {df[search_column].nunique()}")
                st.write(f"Mean value of '{search_column}': {np.mean(df[search_column].dropna())}")
                st.write(f"Standard deviation of '{search_column}': {np.std(df[search_column].dropna())}")
            else:
                st.write("Column not found in the dataset.")
        
        # Display the shape of the DataFrame
        st.subheader("**Dataset Dimensions:**")
        st.write(f"Total number of rows: {df.shape[0]}")
        st.write(f"Total number of columns: {df.shape[1]}")

        # Visualization settings
        st.subheader("**Data Visualization Options:**")
        st.sidebar.title("Plot Configuration")

        # Select columns for plotting
        x_column = st.sidebar.selectbox("Choose X-axis Column", df.columns)
        y_column = st.sidebar.selectbox("Choose Y-axis Column", df.columns)

        # Choose plot type
        plot_type = st.sidebar.selectbox("Select Plot Type", 
                                         ["Scatter Plot", "Line Plot", "Bar Plot", "Histogram", "Box Plot", "Relational Plot"])

        # Plotting based on the selected type
        plt.figure(figsize=(10, 6))
        if plot_type == "Scatter Plot":
            sns.scatterplot(data=df, x=x_column, y=y_column)
            st.pyplot(plt)

        elif plot_type == "Line Plot":
            sns.lineplot(data=df, x=x_column, y=y_column)
            st.pyplot(plt)

        elif plot_type == "Bar Plot":
            sns.barplot(data=df, x=x_column, y=y_column)
            st.pyplot(plt)

        elif plot_type == "Histogram":
            sns.histplot(data=df[x_column], kde=True)
            st.pyplot(plt)

        elif plot_type == "Box Plot":
            sns.boxplot(data=df, x=x_column, y=y_column)
            st.pyplot(plt)

        elif plot_type == "Relational Plot":
            sns.relplot(data=df, x=x_column, y=y_column, height=6, aspect=1.5)
            st.pyplot(plt.gcf())  # Display the relational plot
    else:
        st.write("The uploaded file is either empty or could not be processed.")
