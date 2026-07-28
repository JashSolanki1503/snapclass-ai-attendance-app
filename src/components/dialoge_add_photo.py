import streamlit as st
from PIL import Image 


# st.dialog are the simple forms that can appear anywhere and inside this over case if user click the button so that case dialog appear
@st.dialog("Capture or upload photos")
def add_photos_dialog():
    st.write("Add Classroom photos to scan for attendance")

    if "photo_tab" not in st.session_state:
        st.session_state.photo_tab = "camera"
    
    tab1, tab2 = st.columns(2)

    with tab1:
        button_type = "primary" if st.session_state.photo_tab == "camera" else "tertiary"
        if st.button("Camera", type=button_type, width="stretch", icon=":material/add_a_photo:"):
            st.session_state.photo_tab = "camera"
            
    with tab2:
        button_type = "primary" if st.session_state.photo_tab == "upload_photo" else "tertiary"
        if st.button("Upload photos", type=button_type, width="stretch", icon=":material/image_inset:"):
           st.session_state.photo_tab = "upload_photo"
    
    # depending upon the selected tab we are going to chosse action 
    if st.session_state.photo_tab == "camera":
        photo = st.camera_input("Take Snapshot", key="dialog_cam")

        if photo:
            # push this photo inside the sesstion_state
            st.session_state.attendence_images.append(Image.open(photo))

            st.toast("Photo Captured")
            st.rerun()


    if st.session_state.photo_tab == "upload_photo":
        st.space()
        
        uploaded_photos = st.file_uploader('choose image file', type=['jpg', 'png', 'jpeg'], accept_multiple_files=True, key="dialog_upload")

        if uploaded_photos:

            # if teacher upload the multiple photos
            for photo in uploaded_photos:
                st.session_state.attendence_images.append(Image.open(photo))

            # once all photos are loaded inside the session_state so that case we can rerun the app
            st.toast("Photo Uploaded Sucessfully!")
            st.rerun()

    st.divider()

    if st.button("Done", type="primary", width="stretch"):
        st.rerun()