import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# App title
st.title("Comprehensive Data Visualization and Analysis App")

# File uploader
uploaded_file = st.file_uploader("Choose a CSV or Excel file", type=["csv", "xlsx"])

# Check if a file is uploaded
if uploaded_file is not None:
    try:
        # Read the file based on its type
        if uploaded_file.name.endswith('.csv'):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)

        # Display data preview
        st.write("**Data Preview:**")
        st.write(df.head())

        # Display basic data summary
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

        # Display DataFrame shape
        st.write("**DataFrame Shape:**")
        st.write(f"Rows: {df.shape[0]}")
        st.write(f"Columns: {df.shape[1]}")

        # Sidebar for plot settings
        st.write("**Data Visualization:**")
        st.sidebar.title("Plot Settings")

        # Select columns for x and y axes
        x_column = st.sidebar.selectbox("Select X-axis column", df.columns)
        y_column = st.sidebar.selectbox("Select Y-axis column", df.columns)

        # Select plot type
        plot_type = st.sidebar.selectbox("Select Plot Type", [
            "Scatter Plot", "Line Plot", "Bar Plot", "Histogram", "Box Plot", "Relational Plot"
        ])

        # Plot the selected chart
        plt.figure(figsize=(10, 6))

        if plot_type == "Scatter Plot":
            sns.scatterplot(data=df, x=x_column, y=y_column)
        elif plot_type == "Line Plot":
            sns.lineplot(data=df, x=x_column, y=y_column)
        elif plot_type == "Bar Plot":
            sns.barplot(data=df, x=x_column, y=y_column)
        elif plot_type == "Histogram":
            sns.histplot(data=df[x_column], kde=True)
        elif plot_type == "Box Plot":
            sns.boxplot(data=df, x=x_column, y=y_column)
        elif plot_type == "Relational Plot":
            sns.relplot(data=df, x=x_column, y=y_column, height=6, aspect=1.5)

        st.pyplot(plt)

    except Exception as e:
        st.error(f"An error occurred while processing the file: {e}")
else:
    st.write("Please upload a file to proceed.")
