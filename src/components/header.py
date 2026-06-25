import streamlit as st 


def header_home():

    logo_url = "https://i.ibb.co/YTYGn5qV/logo.png"

    st.markdown(f"""
      <div style='display:flex; flex-direction:column; align-items:center; justify-content:center; margin-bottom:30px; margin-top:30px'>
          <img src={logo_url} alt="logo of the app" style='height:100px;' />    
          <h1 style='text-align:center; color: #E0E3FF'>SNAP<br/>CLASS</h1>
      </div>

    """, unsafe_allow_html=True)



def header_dashboard():
    logo_url = "https://i.ibb.co/YTYGn5qV/logo.png"

    st.markdown(f"""
      <div style='display:flex; align-items:center; gap:10px; justify-content:center; margin-top:30px'>
          <img src={logo_url} alt="logo of the app" style='height:85px;' />    
          <h2 class='snap-heading'>SNAP<br/>CLASS</h2>
      </div>

      <style>
      h2.snap-heading {{
          color: #5865F2 !important;
      }}
      </style>
    """, unsafe_allow_html=True)
