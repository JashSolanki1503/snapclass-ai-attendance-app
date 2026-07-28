import streamlit as st
from src.pipelines.voice_recognition import process_bulk_audio
from src.components.dialoge_attendance_result import show_attendance_results
from src.database.config import supabase
from datetime import datetime 
import pandas as pd

# st.dialog are the simple forms that can appear anywhere and inside this over case if user click the button so that case dialog appear
@st.dialog("Voice Attendance")
def voice_attendance_dialog(selected_subject_id):
    st.write("Record audio of students saying I am present. Then AI will recognize the students.")

    audio_input = st.audio_input("Record classroom audio")

    if st.button("Analyze Audio", type="primary", width="stretch"):

        with st.spinner("Processing Audio data..."):

            try:
                response = supabase.table("subject_students").select("*, students(*)").eq("subject_id", selected_subject_id).execute()
                enroll_subject_students = response.data

                # if not student enroll this subeject 
                if not enroll_subject_students:
                    st.warning("No students enrolled in this course")
                    return 
                
                # Find the students who register their voice inside the database
                candidates_dict = {
                  s['students']['student_id'] : s['students']['voice_embedding']
                  for s in enroll_subject_students if s['students'].get('voice_embedding')
                }

                if not candidates_dict:
                    st.error("No enrolled students have voice profiles registerd")
                    return 

                # Extract the raw binary audio bytes 
                audio_bytes = audio_input.read()

                # Detect the students 
                detected_scores = process_bulk_audio(audio_bytes, candidates_dict)

                students_data, attendace_log = [], []
                
                # Extract the current timestamp 
                current_timestamp = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")

                for node in enroll_subject_students:
                    student = node['students']

                    score = detected_scores.get(student['student_id'], 0.0)
                    is_present = bool(score > 0)

                    # used to display the data in form of pandas dataframe
                    students_data.append({
                        "Name": student['name'],
                        "ID": student['student_id'],
                        "Matching Score": score if is_present else "-",
                        "Status": "✅ Present" if is_present else "❌ Absent"
                    })

                    # used to insert inside the database 
                    attendace_log.append({
                        "timestamp": current_timestamp,
                        "subject_id": selected_subject_id,
                        "student_id": student['student_id'],
                        "is_present": bool(is_present)
                    })

                # insert this students_data and attendace_log inside the session_state
                st.session_state.voice_attendance_results = (
                    pd.DataFrame(students_data),
                    attendace_log
                )
            
            except Exception as e:
                st.error(f"Unexpected error : {e}!")
                return 

    if st.session_state.get("voice_attendance_results"):
        st.divider()
        df_results, logs = st.session_state.voice_attendance_results
        show_attendance_results(df_results, logs)