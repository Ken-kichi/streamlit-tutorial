import streamlit as st

def render_data_table(pd_display_data):
    st.subheader("📜 Record List")
    st.dataframe(pd_display_data)
