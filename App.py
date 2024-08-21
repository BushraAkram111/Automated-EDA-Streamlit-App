import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set title and name
st.title("Data Analysis and Visualization App")
st.sidebar.markdown("### **Shakeela Riaz**", unsafe_allow_html=False)

# Upload file
uploaded_file = st.file_uploader("Choose a CSV or Excel file", type=["csv", "xlsx"])

if uploaded_file is not None:
    try:
        # Check file type and load the data accordingly
        if uploaded_file.name.endswith('.csv'):
            df = pd.read_csv(uploaded_file)
        elif uploaded_file.name.endswith('.xlsx'):
            df = pd.read_excel(uploaded_file)
        else:
            st.error("Unsupported file format. Please upload a CSV or Excel file.")
            df = None
    except Exception as e:
        st.error(f"Error reading the file: {e}")
        df = None

    if df is not None and not df.empty:
        # Data preview
        st.write("**Data Preview:**")
        st.write(df.head())

        # Data summary
        st.write("**Data Summary:**")
        st.write(df.describe())

        # Column search and details
        st.write("**Column Information:**")
        search_column = st.text_input("Search column name")

        if search_column:
            if search_column in df.columns:
                st.write(f"Column length: {len(df[search_column])}")
                st.write(f"Missing values: {df[search_column].isnull().sum()}")
            else:
                st.write("Column not found.")
        
        # DataFrame shape
        st.write("**DataFrame Shape:**")
        st.write(f"Rows: {df.shape[0]}")
        st.write(f"Columns: {df.shape[1]}")

        # Visualization
        st.write("**Data Visualization:**")
        st.sidebar.title("Plot Settings")

        # Select column for x-axis
        x_column = st.sidebar.selectbox("Select X-axis column", df.columns)
        
        # Select column for y-axis
        y_column = st.sidebar.selectbox("Select Y-axis column", df.columns)

        plot_type = st.sidebar.selectbox("Select Plot Type", 
                                         ["Scatter Plot", "Line Plot", "Bar Plot", "Histogram", "Box Plot", "Relational Plot"])

        if plot_type == "Scatter Plot":
            plt.figure(figsize=(10, 6))
            sns.scatterplot(data=df, x=x_column, y=y_column)
            st.pyplot(plt)

        elif plot_type == "Line Plot":
            plt.figure(figsize=(10, 6))
            sns.lineplot(data=df, x=x_column, y=y_column)
            st.pyplot(plt)

        elif plot_type == "Bar Plot":
            plt.figure(figsize=(10, 6))
            sns.barplot(data=df, x=x_column, y=y_column)
            st.pyplot(plt)

        elif plot_type == "Histogram":
            plt.figure(figsize=(10, 6))
            sns.histplot(data=df[x_column], kde=True)
            st.pyplot(plt)

        elif plot_type == "Box Plot":
            plt.figure(figsize=(10, 6))
            sns.boxplot(data=df, x=x_column, y=y_column)
            st.pyplot(plt)

        elif plot_type == "Relational Plot":
            sns.relplot(data=df, x=x_column, y=y_column, height=6, aspect=1.5)
            st.pyplot(plt.gcf())  # Get the current figure and display it
    else:
        st.write("The uploaded file is empty or could not be processed.")
