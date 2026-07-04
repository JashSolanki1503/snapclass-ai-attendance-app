import streamlit as st 

from src.ui.base_layout import style_base_layout, style_background_dashboard
from src.components.header import header_dashboard
from src.components.footer import footer_dashboard

# open the image in python interface
from PIL import Image
import numpy as np

from src.pipelines.face_recognition import predict_attendance, get_face_embeddings, train_classifier
from src.pipelines.voice_recognition import get_voice_embedding

from src.database.db import get_all_students, create_student
import time  


def student_dashboard():
    st.header("THIS IS THE DASHBAORD")


def student_screen():
    
    style_base_layout()
    style_background_dashboard()

    # student dashboard navigation 
    if "student_data" in st.session_state:
        student_dashboard()
        return 
    

    # Header part 
    c1, c2 = st.columns(2, vertical_alignment="center", gap="xxlarge")
    with c1:
        header_dashboard()
    with c2:
        if st.button("Go back to Home", shortcut="control+backspace"):
            st.session_state["login_type"] = None
            st.rerun()
    
    st.header("Login using FaceID", text_alignment="center")
    
    st.space()
    st.space()

    photo_source = st.camera_input("Position your face in the center")
    show_registration = False

    if photo_source:
        
        # load detected image in form of numpy array 
        image = np.array(Image.open(photo_source))

        # Display a loading spinner while AI processes the image.
        with st.spinner("AI is scanning..."):
            
            # to identify if student has already register or not 
            # if student is already registed so that case we get not empty detected dictionary 
            # other wise we get empty dictionary 
            # if student validly capture photo so that all case we get faces 
            detected, all_ids, faces = predict_attendance(image)

            if faces == 0:
                st.warning("Face not found!")
            elif faces > 1:
                st.warning("Multiple faces found!")
            else:
                
                # if student is alraedy registerd so we redirect to dashboard
                if detected:

                    # extract the student id from the detected student dict 
                    student_id = list(detected.keys())[0]

                    # find detected student all data from database
                    all_students = get_all_students()

                    if all_students:
                        student = next((s for s in all_students if s['student_id'] == student_id), None)
                        
                        if student:

                            # Store student information in the session for dashboard navigation. 
                            st.session_state.is_logged_in = True
                            st.session_state.user_role = 'student'
                            st.session_state.student_data = student

                            st.toast(f"Welcome Back {student['name']}")
                            time.sleep(1)

                            # to go to dashboard 
                            st.rerun()

                else:
                    st.info("Face not recognized! You might be a new student!")
                    show_registration = True

    # if student is not exist inside the database
    if show_registration:

        with st.container(border=True):
        
            st.header("Register new Profile")

            new_name = st.text_input("Enter your name", placeholder="E.g. Jash Solanki")

            st.subheader("Optional: Voice Enrollment")
            st.info("Enroll your for voice only attendence")

            # student audio capturing 
            audio_data = None
            
            try:
                audio_data = st.audio_input("Record a short phrase like I am present, My name is Jash.")
            except Exception:
                st.error("Audio Data failed!")

            # insert all student data inside the database 
            if st.button("Create Account", type="primary"):
                
                # check if student enter name or not 
                if new_name:
                    with st.spinner("Creating profile..."):
                        
                        # load detected image in form of numpy array 
                        image = np.array(Image.open(photo_source))

                        # convert raw image into the embedding 
                        face_embedding = get_face_embeddings(image)

                        if face_embedding:

                            face_embedding = face_embedding[0].tolist()

                            # convert raw voice into the embedding 
                            voice_embedding = None
                            if audio_data:
                                voice_embedding = get_voice_embedding(audio_data.read())

                            # insert data in database
                            response_data = create_student(
                                new_name, 
                                face_embedding = face_embedding, 
                                voice_embedding = voice_embedding
                            )

                            if response_data:
                                
                                # Retrain the face classifier so future logins can recognize the newly registered student.
                                train_classifier()

                                # insert some data inside the session_state
                                st.session_state.is_logged_in = True
                                st.session_state.user_role = 'student'
                                st.session_state.student_data = response_data[0]

                                st.toast(f"Profile Created! Hi {new_name}!")
                                time.sleep(1)
                                st.rerun()
                        else:
                            st.error("Couldn't capture yout facial feature for registration!")

                else:
                    st.warning("Please enter your name!")  

    footer_dashboard()