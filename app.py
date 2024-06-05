import streamlit as st
import pandas as pd
from io import BytesIO

# Function to clean the Excel file
def clean_excel(file):
    df = pd.read_excel(file)
    # Example cleaning: remove rows with any null values
    df_cleaned = df.dropna()
    return df_cleaned

# Hide Streamlit branding
hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Title of the app
st.markdown("""
    <h1 style='text-align: center;'>Excel File Cleaner</h1>
    """, unsafe_allow_html=True)

# File upload functionality
uploaded_file = st.file_uploader("Upload an Excel file", type=["xlsx", "xls"])

if uploaded_file is not None:
    file_name = uploaded_file.name
    st.write(f"File name: {file_name}")
    st.write("<p style='color:green;'>Upload successful</p>", unsafe_allow_html=True)

    # Clean button
    if st.button("Clean"):
        cleaned_df = clean_excel(uploaded_file)
        
        # Convert cleaned DataFrame to a binary Excel file
        output = BytesIO()
        with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
            cleaned_df.to_excel(writer, index=False, sheet_name='Sheet1')
        output.seek(0)
        
        # Provide download link for the cleaned file
        st.download_button(
            label="Download Cleaned File",
            data=output,
            file_name="cleaned_" + file_name,
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
        
        st.write("<p style='color:green;'>Cleaning complete</p>", unsafe_allow_html=True)
