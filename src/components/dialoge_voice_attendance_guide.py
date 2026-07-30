import streamlit as st
from PIL import Image 


@st.dialog("🎤 Voice Attendance Guide")
def voice_attendance_guide():

    # Guide content 
    st.write("""
    Voice Attendance is an optional attendance method.

    The system identifies students using their registered voice profiles.

    Before continuing, please note:

    • Only students who have completed Voice Enrollment can be recognized.

    • Students who have registered only their face profile but not their voice profile cannot be identified using Voice Attendance.

    • For the most accurate attendance, ask students to speak clearly in a quiet classroom.

    If many students have not enrolled their voice, we recommend using Camera Attendance instead.
    """)

    # button that indicate teacher is agreed 
    if st.button("Got it", type="primary", width="stretch"):
        st.session_state.voice_attendance_guide_seen = False
        st.rerun()