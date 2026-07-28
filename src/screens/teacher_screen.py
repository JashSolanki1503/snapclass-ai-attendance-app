import streamlit as st 

from src.components.header import header_dashboard
from src.components.footer import footer_dashboard
from src.components.dialoge_create_subject import create_subject_dialog
from src.components.dialoge_share_subject import share_subject_dialog
from src.components.dialoge_add_photo import add_photos_dialog
from src.components.dialoge_attendance_result import attendance_result_dialog
from src.components.dialoge_voice_attendance import voice_attendance_dialog
from src.components.subject_card import subject_card

from src.pipelines.face_recognition import predict_attendance

from src.ui.base_layout import style_background_dashboard_teacher, style_base_layout
from src.database.db import check_teacher_exists, teacher_login, create_teacher, get_teacher_subjects
from src.database.config import supabase

import pandas as pd 
import numpy as np
from datetime import datetime


def teacher_screen():
    
    style_base_layout()
    style_background_dashboard_teacher()
    
    if 'teacher_data' in st.session_state:
        teacher_dashboard()
    elif 'teacher_login_type' not in st.session_state or st.session_state["teacher_login_type"] == "login":
        teacher_screen_login()
    else:
        teacher_screen_register()


# if teacher authenticate sucessfully so that case go to dashboard
def teacher_dashboard():
    
    teacher_data = st.session_state['teacher_data']

    # Header part 
    c1, c2 = st.columns(2, vertical_alignment="center", gap="xxlarge")
    with c1:
        header_dashboard()
    with c2:
        st.subheader(f"Welcome, {teacher_data['name']}")
        if st.button("Logout", type = "secondary", shortcut="control+backspace", width="stretch"):
            st.session_state['is_logged_in'] = False
            del st.session_state['teacher_data']
            st.rerun()
    
    st.space()
    
    # We track the teacher's current tab 
    if "current_teacher_tab" not in st.session_state:
        st.session_state.current_teacher_tab = "take_attendence"
    
    # Creating the tabs 
    tab1, tab2, tab3 = st.columns(3)
    
    with tab1:
        type1 = "primary" if st.session_state.current_teacher_tab == "take_attendence" else "tertiary"
        if st.button("Take Attendence", type=type1, width="stretch", icon=":material/ar_on_you:"):
            st.session_state.current_teacher_tab = "take_attendence"
            st.rerun()
    
    with tab2:
        type2 = "primary" if st.session_state.current_teacher_tab == "manage_subjects" else "tertiary"
        if st.button("Manage Subjects", type=type2, width="stretch", icon=":material/book_ribbon:"):
            st.session_state.current_teacher_tab = "manage_subjects"
            st.rerun()

    with tab3:
        type3 = "primary" if st.session_state.current_teacher_tab == "attendance_records" else "tertiary"
        if st.button("Attendece Records", type=type3, width="stretch", icon=":material/cards_stack:"):
            st.session_state.current_teacher_tab = "attendance_records"
            st.rerun()

    st.divider()
    
    # Depending upon choosen tab we are display tab content 
    if st.session_state.current_teacher_tab == "take_attendence":
        teacher_tab_take_attendence()
    elif st.session_state.current_teacher_tab == "manage_subjects":
        teacher_tab_manage_subjects()
    else:
        teacher_tab_attendece_records()

    footer_dashboard()


# Teacher dashboard tabs implementation 
def teacher_tab_take_attendence():
    
    teacher_id = st.session_state.teacher_data['teacher_id']

    if "attendence_images" not in st.session_state:
        st.session_state.attendence_images = []

    # Get the teacher subjects
    subjects = get_teacher_subjects(teacher_id)

    if not subjects:
        st.warning("You haven't created any subjects yet! Please create one to begin!")
        return 
    
    # Make the subject name and its code related dictionary 
    subject_option = {f"{s['name']} - {s['subject_code']}": s['subject_id'] for s in subjects}

    st.header("Take AI Attendance")

    tab1, tab2 = st.columns([3, 1], vertical_alignment="bottom")

    with tab1:
        selected_subject_label = st.selectbox("Select Subject", options = list(subject_option.keys())) 

    with tab2:
        if st.button("Add Photos", type="primary", icon=":material/photo_prints:", width="stretch"):
            add_photos_dialog()

    # Extract the student enter subject's id 
    selected_subject_id = subject_option[selected_subject_label]  

    st.divider()

    # ---------------------------------------------------------------------------------------
    # EXPERIMENTAL PART 
    # ---------------------------------------------------------------------------------------
    # if teacher capture any attendance images 
    if st.session_state.attendence_images:

        # display all those images in 4 x 4 Grid format
        st.header("Added Photos")

        cols = st.columns(4)

        for idx, image in enumerate(st.session_state.attendence_images):
            with cols[idx % 4]:
                st.image(image, width="stretch", caption=f"Photo {idx+1}")


        # Create three buttons 
        btn1, btn2 = st.columns(2)
        has_photos = bool(st.session_state.attendence_images)

        # clear all photos button
        with btn1:
            if st.button("Clear all Photos", width="stretch", type= "tertiary", icon=":material/delete:", disabled=not has_photos):
                st.session_state.attendence_images = []
                st.rerun()

        # run face analysis button 
        with btn2: 
            if st.button("Run Face Analysis", width="stretch", type="secondary", icon=":material/analytics:", disabled=not has_photos): 
                with st.spinner("Deep scanning classroom photos..."):

                    detected_students = {}

                    # Predict attendance by uploaded images of the class 
                    for idx, image in enumerate(st.session_state.attendence_images):

                        # convert image into the numpy array 
                        image_np = np.array(image.convert('RGB'))

                        # Predict the student attendance from the image 
                        detected, _, _ = predict_attendance(image_np)

                        if detected:
                            for sid in detected.keys():
                                student_id = int(sid)
                                detected_students.setdefault(student_id, []).append(f"Photo {idx+1}")

                    # Get the subject enroll students 
                    response = supabase.table("subject_students").select("*, students(*)").eq("subject_id", selected_subject_id).execute()
                    enroll_subject_students = response.data
                    
                    if not enroll_subject_students:
                        st.warning("No students enroll in this course.")
                        return 
                    else:

                        students_data, attendace_log = [], []

                        # Extract the current timestamp 
                        # Here datetime.now() give us the row datetime obejct which is harder to identify so that's why we use strftime() for better formating 
                        # and inside "%Y-%m-%dT%H:%M:%S" T just a seperator and as example "2026-07-25T16:28:30"
                        current_timestamp = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")

                        for node in enroll_subject_students:
                            student = node['students']

                            sources = detected_students.get(int(student['student_id']), [])
                            is_present = len(sources) > 0

                            # used to display the data in form of pandas dataframe
                            students_data.append({
                                "Name": student['name'],
                                "ID": student['student_id'],
                                "Source": ", ".join(sources) if is_present else "-",
                                "Status": "✅ Present" if is_present else "❌ Absent"
                            })

                            # used to insert inside the database 
                            attendace_log.append({
                                "timestamp": current_timestamp,
                                "subject_id": selected_subject_id,
                                "student_id": student['student_id'],
                                "is_present": is_present 
                            })

                        attendance_result_dialog(pd.DataFrame(students_data), attendace_log)

        # with btn3:
        #     if st.button("Use Voice Attendance", type="primary", icon=":material/mic:", width="stretch"):
        #         voice_attendance_dialog()

    else:
        st.info("Please Capture first images of Class.")


    if st.button("Use Voice Attendance", type="primary", icon=":material/mic:", width="stretch"):
        voice_attendance_dialog(selected_subject_id)
            



def teacher_tab_manage_subjects():
    
    # Fetch the teacher_id form the database 
    teacher_id = st.session_state.teacher_data['teacher_id']

    tab1, tab2 = st.columns(2)
    with tab1:
        st.header("Manage Subjects")

    with tab2:

        # When user select this button so that case create subject dialogue form will be appear 
        if st.button("Create New Subjects", width="stretch"):
            create_subject_dialog(teacher_id)

    # LIST ALL SUBJECTS 
    subjects = get_teacher_subjects(teacher_id)
    if subjects:

        # Create the state to store each subject's total_student and Classes to easily render by subject card component
        # State is just a storage unit nothing else 
        for sub in subjects:
            stats = [
                ("👥", "Students", sub['total_students']),
                ("📝", "Classes", sub['total_classes'])
            ]

            # Now here for each subjects we create the share link button 
            # if multiple buttons exist so that case we have to give unique ids to each buttons
            def share_btn():
                if st.button(f"Share Code: {sub['name']}", key=f"share_{sub['subject_code']}", icon=":material/share:"):

                    # QR - Code share feature function 
                    share_subject_dialog(sub['name'], sub['subject_code'])

                st.space()


            subject_card(
                name = sub['name'],
                code = sub['subject_code'],
                section = sub['section'],
                stats = stats,
                footer_callback = share_btn
            )

        
    else:
        st.info("No Subjects Found. Create One Above.")


def teacher_tab_attendece_records():
    st.header("Attendence Records")


# Helper function for the teacher_screen_login
def login_teacher(username, password):

    # Some essential checks 
    if not username or not password:
        return False
    
    # Check teacher inside the database
    teacher = teacher_login(username, password)

    if teacher:

        # Store some data inside the session_state
        st.session_state['user_role'] = "teacher"
        st.session_state['teacher_data'] = teacher
        st.session_state['is_logged_in'] = True

        return True
    
    return False

def teacher_screen_login():
    
    # Header part 
    c1, c2 = st.columns(2, vertical_alignment="center", gap="xxlarge")
    with c1:
        header_dashboard()
    with c2:
        if st.button("Go back to Home", shortcut="control+backspace"):
            st.session_state["login_type"] = None
            st.rerun()
    
    st.header("Login using password", text_alignment="center")

    # add some spaces 
    st.space()
    st.space()

    teacher_username = st.text_input("Enter username", placeholder="@jashsolanki")
    teacher_pass = st.text_input("Enter password", placeholder="Enter password", type="password")

    st.divider()

    # add buttons
    btn1, btn2 = st.columns(2)
    with btn1:
        if st.button("Login", shortcut="control+enter", icon=":material/passkey:", width="stretch"):
            
            if login_teacher(teacher_username, teacher_pass):
                st.toast("Welcome back!", icon="👋")  

                # pause for 2sec for the smooth demonstation 
                import time 
                time.sleep(1)

                st.rerun()

            else:
                st.error("Invalid username or password!")
                

    with btn2:
        if st.button("Register Instead", type="primary", icon=":material/passkey:", width="stretch"):
            st.session_state["teacher_login_type"] = "register"
            st.rerun()
            

    footer_dashboard()


# Helper Function for the registration 
def register_teacher(teacher_username, teacher_name, teacher_password, teacher_pass_confirm):
    
    # Check some registration requirnments
    if not teacher_username or not teacher_name or not teacher_password:
        return False, "All Fields are required!"
    
    # Check if this username already taken or already exist 
    if check_teacher_exists(teacher_username):
        return False, "Username already taken!"
    
    if teacher_password != teacher_pass_confirm:
        return False, "Password dosen't match!"
    
    # register the teacher 
    try:
        create_teacher(teacher_username, teacher_password, teacher_name)
        return True, "Sucessfully Created! Login Now"
    except Exception as e:
        return False, "Unexpected Error!"

def teacher_screen_register():
    
    # Header part 
    c1, c2 = st.columns(2, vertical_alignment="center", gap="xxlarge")
    with c1:
        header_dashboard()
    with c2:
        if st.button("Go back to Home", shortcut="control+backspace"):
            st.session_state['login_type'] = None
            st.rerun()

    st.header("Register your teacher profile", text_alignment="center")

    # add some spaces 
    st.space()
    st.space()

    # create some input fields
    teacher_username = st.text_input("Enter username", placeholder="@jashsolanki")
    teacher_name = st.text_input("Enter name", placeholder="Jash Solanki")
    teacher_pass = st.text_input("Enter password", placeholder="Enter your password", type="password")
    teacher_pass_confirm = st.text_input("Confirm password", placeholder="Confirm your password", type="password")

    st.divider()

    # add buttons
    btn1, btn2 = st.columns(2)
    with btn1:
        if st.button("Register now", type="primary", icon=":material/passkey:", width="stretch"):

            # try to register the teacher
            success, message = register_teacher(teacher_username, teacher_name, teacher_pass, teacher_pass_confirm)

            if success:
                st.success(message)
                
                # Take pause to demonstrate smooth performance
                import time 
                time.sleep(2)

                st.session_state["teacher_login_type"] = "login"
                st.rerun()
            else:
                st.error(message)

    with btn2:
        if st.button("Login Instead", shortcut="control+enter", icon=":material/passkey:", width="stretch"):
            st.session_state["teacher_login_type"] = "login"
            st.rerun()

    footer_dashboard()