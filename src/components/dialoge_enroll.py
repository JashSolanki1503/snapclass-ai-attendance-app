import streamlit as st
from src.database.config import supabase
from src.database.db import enroll_student_to_subject
import time 


# st.dialog are the simple forms that can appear anywhere and inside this over case if user click the button so that case dialog appear
@st.dialog("Enroll in Subject")
def enroll_dialog():
    st.write("Enter the subject code provided by your teacher to enroll")
    join_code = st.text_input("Subject Code", placeholder="Eg. IT101")

    if st.button("Enroll now", type="primary", width="stretch"):

        # if student is not provide the code of the subject 
        if join_code:

            # check the provided code realted subject exist inside the database
            # same as : SELECT subject_id, name, subject_code FROM subjects WHERE subject_code = given_code;
            res = supabase.table("subjects").select("subject_id, name, subject_code").eq("subject_code", join_code).execute()

            if res.data:
                # fetch subject realted info 
                subject = res.data[0]

                student_id = st.session_state.student_data["student_id"]

                # Check this student already enroll inside this subject or not
                # same as : SELECT * FROM subject_students WHERE subject_id = given_id AND student_id = given_student_id;
                # inside the supabase query .eq().eq() means AND of the filter
                check = supabase.table("subject_students").select("*").eq("subject_id", subject['subject_id']).eq('student_id', student_id).execute()
                if check.data:
                    st.warning("You are already enrolled in this program")
                else:
                    enroll_student_to_subject(student_id, subject['subject_id'])
                    st.success("Succesfully enrolled!")
                    time.sleep(1)
                    st.rerun()

            else:
                st.error("Your provided code related subject is not exist!")

        else:
            st.warning("Please enter a subject code")
