import streamlit as st
from src.database.db import insert_attendance_logs 


# st.dialog are the simple forms that can appear anywhere and inside this over case if user click the button so that case dialog appear
def show_attendance_results(df, attendance_logs):
    st.write("Please review attendance before confirming.")

    # Show the student present in form of the pandas dataframe 
    st.dataframe(df, hide_index=True, width="stretch")

    # add two buttons 
    btn1, btn2 = st.columns(2)
    with btn1:
        if st.button("Discard", type="secondary", width="stretch"):
            st.session_state.attendence_images = []
            st.session_state.voice_attendance_results = None 
            st.session_state.is_audio_exist = False
            st.rerun()
            

    with btn2:
        if st.button("Confirm & Save", type="primary", width="stretch"):
            try:
                insert_attendance_logs(attendance_logs)
                st.toast("Attendance taken.")
                st.session_state.attendence_images = []
                st.session_state.voice_attendance_results = None
                st.session_state.is_audio_exist = False
                st.rerun()

            except Exception as e:
                st.error("Sync failed!")

@st.dialog("Attendance Reports")
def attendance_result_dialog(df, attendance_logs):
    show_attendance_results(df, attendance_logs)
