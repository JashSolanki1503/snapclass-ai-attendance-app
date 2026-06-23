import streamlit as st 

def teacher_screen():
    st.header("Hello I am a Teacher Screen")

    if st.button("Go to the Home Scrren"):

        st.session_state["login_type"] = None

        st.rerun()