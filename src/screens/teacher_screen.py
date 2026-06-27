import streamlit as st 

from src.components.header import header_dashboard
from src.ui.base_layout import style_background_dashboard, style_base_layout
from src.components.footer import footer_dashboard


def teacher_screen():
    
    style_base_layout()
    style_background_dashboard()
    
    if 'teacher_login_type' not in st.session_state or st.session_state["teacher_login_type"] == "login":
        teacher_screen_login()
    else:
        teacher_screen_register()


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
            st.session_state["teacher_login_type"] = "login"
            st.rerun()

    with btn2:
        if st.button("Register Instead", type="primary", icon=":material/passkey:", width="stretch"):
            st.session_state["teacher_login_type"] = "register"
            st.rerun()
            

    footer_dashboard()


def teacher_screen_register():
    
    # Header part 
    c1, c2 = st.columns(2, vertical_alignment="center", gap="xxlarge")
    with c1:
        header_dashboard()
    with c2:
        if st.button("Go back to Home", shortcut="control+backspace"):
            st.session_state["login_type"] = None
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
            st.session_state["teacher_login_type"] = "register"
            st.rerun()
    with btn2:
        if st.button("Login Instead", shortcut="control+enter", icon=":material/passkey:", width="stretch"):
            st.session_state["teacher_login_type"] = "login"
            st.rerun()

    footer_dashboard()



