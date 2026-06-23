import streamlit as st 

def student_screen():
    st.header("Hello I am a Studnet Screen")

    if st.button("Go to the Home Scrren"):

        st.session_state["login_type"] = None

        st.rerun()