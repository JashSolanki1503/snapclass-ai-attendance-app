import streamlit as st
import io

# To generate the QR - Codes 
import segno 

@st.dialog("Share Class Link")
def share_subject_dialog(subject_name, subject_code):
    
    # Define the app domain
    app_domain = "https://snapclass-ai-attendance-app-4gw6keezdpnv5fkbsyva5m.streamlit.app"

    # we add this query-string parameter so that case when user login we easily nevigate it into the correct subject
    join_url = f"{app_domain}/?join-code={subject_code}"

    st.header("Scan to Join")
    
    # here segno.make("content") 
    # segno hide this content into the QR - Code and when we scan through browser so browser easily identify this join_url 
    qr = segno.make(join_url)

    # We create the buffer memory where we store this QR - Code image info
    # With the help of this buffer memory we can store this image inside the RAM
    out = io.BytesIO()

    # Save this QR - Code into this buffter memory
    qr.save(out, kind="png", scale=10, border=1)

    tab1, tab2 = st.columns(2)
    with tab1:
        st.markdown("### 🔗 Copy Link")
        st.code(join_url, language="text")
        st.code(subject_code, language="text")
        st.info("Copy this link to share on WhatsApp or Email")

    with tab2:
        st.markdown("### 📸 Scan to Join")
        st.image(out.getvalue(), caption=f"QRCODE for {subject_name}")



    