import streamlit as st
from screener.storage import load_from_db

st.set_page_config(page_title="Stock Screener", layout="wide")
st.title("📊 Custom Python Stock Screener")

try:
    df = load_from_db()
    st.write(f"✅ {len(df)} stocks matched your filters")
    st.dataframe(df)
except Exception as e:
    st.error(f"Failed to load data: {e}")
