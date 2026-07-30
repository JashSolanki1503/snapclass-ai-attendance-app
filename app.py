# ISSUES 
# Supabase not grant the delete request 
# inside the student_screen toast color is completly white 




import streamlit as st 

from src.screens.home_screen import home_screen
from src.screens.student_screen import student_screen
from src.screens.teacher_screen import teacher_screen

from src.components.dialoge_auto_enroll import auto_enroll_dialog

def main():
    
    # initialize the state variables 
    if "login_type" not in st.session_state:
        st.session_state["login_type"] = None 

    match st.session_state["login_type"]:

        case "teacher":
            teacher_screen()

        case "student":
            student_screen()

        case None:
            home_screen()

    # when student try to enroll subject with teacher share link - implementation
    join_code = st.query_params.get("join-code")

    # if student enroll via teacher link 
    if join_code:

        # nevigate the student register screen and create the student account first 
        if st.session_state.login_type != "student":
            st.session_state.login_type = "student"
            st.rerun()
        
        # if once student succesfully created the account so that case we will pop up the login dialogue 
        if st.session_state.get('is_logged_in') and st.session_state['user_role'] == "student":
            auto_enroll_dialog(join_code)

main()