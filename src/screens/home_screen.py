import streamlit as st
from src.components.header import header_home

def home_screen():
    st.header("Hello i am a HEADER SECTION")
    
    header_home()

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Go to the Teacher section", key = "teacher"):

            st.session_state["login_type"] = "Teacher"
            st.rerun()

    with col2:
        if st.button("Go to the Student section"):

            st.session_state["login_type"] = "Student"
            st.rerun()