import streamlit as st
from src.database.db import create_subject


# st.dialog are the simple forms that can appear anywhere and inside this over case if user click the button so that case dialog appear
@st.dialog("Create New Subject")
def create_subject_dialog(teacher_id):
    st.write("Enter the details of new subject")

    sub_id = st.text_input("Subject Code", placeholder="CS101")
    sub_name = st.text_input("Subject Name", placeholder="Machine Learning Fundametals")
    sub_section = st.text_input("Section", placeholder="A")

    if st.button("Create Subject Now", type="primary", width="stretch"):

        # if user enter all fields inside the dialog
        if sub_id and sub_name and sub_section:

            try:
                create_subject(sub_id, sub_name, sub_section, teacher_id) 
                st.toast("Subject Created Succesfully!")
                st.rerun()
            except Exception as e:
                st.error(f"Error : {e}")

        else:
            st.warning("Please fill all the fields")