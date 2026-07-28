import streamlit as st

from src.database.config import supabase
from src.database.db import enroll_student_to_subject

import time 


# When student try to enroll a subject with teacher given link so that case we pop up this dialog
@st.dialog("Create New Subject")
def auto_enroll_dialog(subject_code):
    student_id = st.session_state.student_data["student_id"]

    # Check 1 : if subject is not exist 
    response = supabase.table("subjects").select("subject_id, name").eq("subject_code", subject_code).execute()
    if not response.data:
        st.error("This subject is not exist!")

        if st.button("Close"):
            st.query_params.clear()
            st.rerun()

        return 

    # Check 2 : if student is already register inside the subject 
    subject = response.data[0]
    check = supabase.table("subject_students").select("*").eq("subject_id", subject['subject_id']).eq("student_id", student_id).execute()
    if check.data:
        st.info("You are already enrolled!")
        
        if st.button("Got it!"):
            st.query_params.clear()
            st.rerun()

        return

    # Actual dialog data implementation 
    st.markdown(f"Would you like to enroll in **{subject['name']}**?")

    tab1, tab2 = st.columns(2)
    with tab1:
        if st.button("No thanks"):
            st.query_params.clear()
            st.rerun()

    with tab2:
        if st.button("Yes enroll now!", type="primary", width="stretch"):
            enroll_student_to_subject(student_id, subject['subject_id'])
            st.success("Joined Succesfully!")
            st.query_params.clear()
            time.sleep(2)
            st.rerun()