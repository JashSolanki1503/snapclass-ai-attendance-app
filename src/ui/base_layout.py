import streamlit as st 



def style_background_home():

    st.markdown("""
  
        <style>

            .stApp {
                background: #5865F2 !important;   
            }  

            /* Change the default style of the st.columns as Columns */
            .stApp div[data-testid="stColumn"] {
                background-color: #E0E3FF !important;
                padding: 2.5rem !important;
                border-radius: 5rem !important;
            }  

        </style>

     """, unsafe_allow_html=True)
    


def style_background_dashboard_teacher():

    st.markdown("""
  
        <style>

        .stApp {
            background: #E0E3FF !important;   
        } 

        /* Change the subheader font color white to black */
        h3 {
            color: black !important;
        }      

        </style>

     """, unsafe_allow_html=True)
    

def style_background_dashboard_student():

    st.markdown("""
  
        <style>

        .stApp {
            background: #E0E3FF !important;   
        } 

        /* Change the subheader font color white to black */
        h3 {
            color: black !important;
        }   
                
        /* Audio traker */
        /* Content/text color black */
        [data-testid="stAudioInput"] p {
            color: #000000 !important;
        }

        /* Change the background color of the audio taker */      
        .st-emotion-cache-1uzegzg {
            background-color: white !important;  
        }
        .st-emotion-cache-oj06lr {
            color: black !important;
            background-color: white !important;   
        }
        /* when we want to see recording so that case also apply same background is white and text color is balck */
        .st-emotion-cache-nm0s83 { 
            color: black !important;
            background-color: white !important;    
        }
                
        /* Target the live wave capture canvas and invert/shift its hue to render Red instead of White */
        div[data-testid="stAudioInputRecordButton"] canvas {
            filter: invert(18%) sepia(96%) saturate(6726%) hue-rotate(356deg) brightness(91%) contrast(119%) !important;
        }   
    
        /* target the spinner */
        /* Change its content color to the black */
        div[data-testid="stSpinner"] > div {
            color: black !important;
        }
        
        /* Change loading symbol color defaultly white to the dark blue */
        /* border-color expect TOP RIGHT BOTTOM LEFT side color */ 
        .st-emotion-cache-1vycjxg {
            border-color: #00008B #00008B #00008B transparent !important;
        }    
                 
        </style>

     """, unsafe_allow_html=True)
    


# for the base style which can apply every pages of the app
def style_base_layout():

    st.markdown("""
  
        <style>
                
        /* importing the heading fonts */
        @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis:YEAR@1985&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@100..900&display=swap');        

        /* Hide Top Toolbar of the Streamlit */
        #MainMenu, header, footer {
            visibility: hidden !important;    
        }

        /* Adjust the top spacing of the main header */ 
        /* Note : Here rem => default font size which browser have which mostly 8px */      
        .block-container {
            padding-top: 1.5rem;        
        }
                
        /* here we apply Climate-Crisis font style to h1 & h2 tags */
        h1 {
            font-family: 'Climate Crisis', sans-serif !important;
            font-size: 3.5rem !important;
            line-height: 1.1 !important;
            margin-bottom: 0rem !important;      
        }

        /* streamlit header bydefault use h2 */      
        h2 {
            font-family: 'Climate Crisis', sans-serif !important;
            font-size: 2rem !important;
            line-height: 0.9 !important;
            letter-spacing: 2px !important;
            margin-bottom: 0rem !important; 
            color: black !important;     
        }
                
        h3, h4, p {
            font-family: 'Outfit', sans-sarif !important;
        }
        
        /* button styling additing */          
        button {
            border-radius: 1.5rem !important;
            background: #5865F2 !important;
            color: white !important;
            padding: 10px, 20px !important;
            border: none !important;
            transition: transform 0.25s ease-in-out !important;   
        }
                
        button[kind="secondary"] {
            border-radius: 1.5rem !important;
            background: #EB459E !important;
            color: white !important;
            padding: 10px, 20px !important;
            border: none !important;
            transition: transform 0.25s ease-in-out !important;   
        }
                
        button[kind="tertiary"] {
            border-radius: 1.5rem !important;
            background: black !important;
            color: white !important;
            padding: 10px, 20px !important;
            border: none !important;
            transition: transform 0.25s ease-in-out !important;   
        }
                
        button:hover {
            transform: scale(1.05)   
        }
                
        /* Input box styling changing */
        .stTextInput input {
            background-color: #f5f5f5  !important;
        }
                
        div[data-baseweb="input"] {
            background-color: white !important;
            border: none !important;
            box-shadow: none !important;
        }
                
        .st-b7 {
            background-color: rgb(250, 250, 250); 
        }

        .stTextInput input::placeholder {
            color: gray !important;
            opacity: 1 !important;
        }    
                
        .stTextInput label {
            color: #000000 !important;
        }
                
        hr {
            border-color: gray !important;
        }
                
        /* Typed text → gray */
        .stTextInput input {
            color: #444444 !important;
        }

        /* Red border on focus */
        div[data-baseweb="input"]:focus-within {
            outline: 2px solid #FF0000 !important;
            border: none !important;
            box-shadow: none !important;
        }

        /* Remove inner input border */
        .stTextInput input:focus {
            border: none !important;
            outline: none !important;
            box-shadow: none !important;
        }

        /* Remove eye button left border */
        div[data-baseweb="input"] button {
            border: none !important;
            border-left: none !important;
            outline: none !important;
            box-shadow: none !important;
        }  
        
        /* Overwrite only the camera_input content */
        [data-testid="stCameraInput"] [data-testid="stWidgetLabel"] p {
            color: #000000 !important;
        } 

        /* Change the dialog background-color and content color */
        /* Dialog background → white */
        [data-testid="stDialog"] > div > div {
            background-color: #ffffff !important;
        }

        /* Dialog title "Create New Subject" → black */
        /* Button text inside dialog → white */
        [data-testid="stDialog"] button p {
            color: #ffffff !important;
        }

        /* All other text inside dialog → black */
        [data-testid="stDialog"] p {
            color: #000000 !important;
        }
                

        /* Change the color of st.code black into the white */
        [data-testid="stCode"] pre {
            background-color: #f5f5f5 !important;
            color: #333333 !important;
        }
                
        /* Change the st.selectbox some property */ 
        /* Chage the selectbox content Label color white to black */
        .stSelectbox label {
            color: #000000 !important;
        }
                
        /* Selected option text inside box → black */
        /* TODO: replace with proper selector, auto-generated class used as last resort */
        /* This targets selected option text in st.selectbox */
        .st-dn {
            color: #000000 !important;
        }


        /* Change the st.file_uplaoder background and content color */
        /* File uploader background → light gray */
        # [data-testid="stFileUploader"] section {
        #     background-color: #f5f5f5 !important;
        # }

        # /* File uploader text → black */
        # [data-testid="stFileUploader"] section span {
        #     color: #000000 !important;
        # }      

        </style>

     """, unsafe_allow_html=True)