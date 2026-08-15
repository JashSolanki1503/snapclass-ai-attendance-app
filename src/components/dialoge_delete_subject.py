import streamlit as st
import time 

from src.database.db import delete_subject


@st.dialog("⚠️ Remove Subject?")
def delete_subject_dialog(subject_id, subject_name):

    st.write("This will permanently delete this subject, all student enrollments for this subject, and all attendance records associated with it. This action cannot be undone.")

    btn1, btn2 = st.columns(2)
    with btn1:
        if st.button("Cancel", icon=":material/close:", type="primary", width="stretch"):
            st.rerun()

    with btn2:
        if st.button("Remove Subject", icon=":material/delete_forever:", width="stretch"):
               
            response = delete_subject(subject_id)

            if response.data:
                time.sleep(1)
                st.toast(f"✅ Sucessfully Deleted {subject_name}")

                st.rerun()

            else:
                st.error("Some Unexpected error ! Try Again !")