import streamlit as st
import pandas as pd
import numpy as np
import base64
from pathlib import Path


st.set_page_config(
    page_title="Student Performance Analyzer",
    page_icon="📊",
    layout="wide"
)
st.snow()
st.title("📊 Student Performance Analyzer")
st.caption("Hands-on Streamlit for Data Science")

image_data = base64.b64encode(
    Path("bg1.png").read_bytes()
).decode()

st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{image_data}");
        background-size: cover;
        background-position: center;
    }}
    </style>
    """,
    unsafe_allow_html=True
)


# Sample data used when the user does not upload a CSV
sample_data = pd.DataFrame({
    "Student": ["Asha", "Bala", "Charan", "Divya", "Ezhil", "Farah", "Gokul", "Hari"],
    "Python": [82, 67, 91, 74, 88, 59, 78, 95],
    "SQL": [76, 72, 89, 81, 84, 61, 70, 92],
    "Statistics": [80, 65, 94, 78, 86, 55, 75, 90],
    "Attendance": [92, 84, 96, 88, 91, 72, 80, 98]
})

st.sidebar.header("1. Upload Data")
uploaded_file = st.sidebar.file_uploader(
    "Upload a CSV file",
    type=["csv"]
)

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    source = "Uploaded CSV"
else:
    df = sample_data.copy()
    source = "Built-in sample data"

st.sidebar.success(f"Data source: {source}")

st.header("Dataset Preview")
st.dataframe(df, width="stretch",
    height=700)

# Identify numeric columns
numeric_cols = df.select_dtypes(include=np.number).columns.tolist()

if numeric_cols:
    st.header("Quick Statistics")

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Rows", len(df))
    c2.metric("Columns", len(df.columns))
    c3.metric("Numeric Columns", len(numeric_cols))
    c4.metric("Missing Values", int(df.isna().sum().sum()))

    st.header("📈 Visual Analysis")

    selected_column = st.selectbox(
        "Choose a numeric column",
        numeric_cols
    )

    chart_df = df[[selected_column]].dropna().reset_index(drop=True)
    st.bar_chart(chart_df)

    st.subheader("Summary")
    st.write(df[numeric_cols].describe())

    st.header("🎯 Performance Insight")

    average = df[selected_column].mean()
    highest = df[selected_column].max()
    lowest = df[selected_column].min()

    a, b, c = st.columns(3)
    a.metric("Average", f"{average:.2f}")
    b.metric("Highest", f"{highest:.2f}")
    c.metric("Lowest", f"{lowest:.2f}")

    if average >= 75:
        st.success("Overall performance is strong based on the selected metric.")
    elif average >= 50:
        st.warning("There is room for improvement based on the selected metric.")
    else:
        st.error("The selected metric needs attention.")

else:
    st.info("No numeric columns found. Upload a dataset containing numeric values.")

st.divider()
st.caption("Built during the Streamlit for Data Science hands-on workshop")
