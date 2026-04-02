import streamlit as st
import pandas as pd


st.title("Sales Dashboard")
st.subheader("Simple sales summary with category filter")


data = {
    "Product": ["Laptop", "Mouse", "Keyboard", "Monitor", "Printer"],
    "Category": ["Electronics", "Accessories", "Accessories", "Electronics", "Office"],
    "Sales": [50000, 1500, 3000, 12000, 8000]
}

df = pd.DataFrame(data)

# -------------------------------
# Sidebar Filter
# -------------------------------
st.sidebar.title("Filters")
selected_category = st.sidebar.selectbox(
    "Select Category",
    df["Category"].unique()
)


filtered_df = df[df["Category"] == selected_category]

st.write(f"Showing data for category: {selected_category}")
st.dataframe(filtered_df)


st.line_chart(filtered_df["Sales"])