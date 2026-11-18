# import streamlit as st 



# def style_background_home():

#     st.markdown("""
  
#         <style>

#             .stApp {
#                 background: #5865F2 !important;   
#             }  

#             /* Change the default style of the st.columns as Columns */
#             .stApp div[data-testid="stColumn"] {
#                 background-color: #E0E3FF !important;
#                 padding: 2.5rem !important;
#                 border-radius: 5rem !important;
#             }  

#         </style>

#      """, unsafe_allow_html=True)
    


# def style_background_dashboard_teacher():

#     st.markdown("""
  
#         <style>

#         .stApp {
#             background: #E0E3FF !important;   
#         } 

#         /* Change the subheader font color white to black */
#         h3 {
#             color: black !important;
#         } 

#         /* target the spinner */
#         /* Change its content color to the black */
#         div[data-testid="stSpinner"] > div {
#             color: black !important;
#         }
        
#         /* Change loading symbol color defaultly white to the dark blue */
#         /* border-color expect TOP RIGHT BOTTOM LEFT side color */ 
#         .st-emotion-cache-1vycjxg {
#             border-color: #00008B #00008B #00008B transparent !important;
#         }         
        

#         /* Audio traker */
#         /* Content/text color black */
#         [data-testid="stAudioInput"] p {
#             color: #000000 !important;
#         }

#         # /* Change the background color of the audio taker */      
#         # .st-emotion-cache-1uzegzg {
#         #     background-color: white !important;  
#         # }
#         # .st-emotion-cache-oj06lr {
#         #     color: black !important;
#         #     background-color: white !important;   
#         # }

#         # /* st.image property changing */
#         # /* change the caption content color white to black */
#         # [data-testid="stImageCaption"] {
#         #     color: #000000 !important;
#         # }
#         </style>

#      """, unsafe_allow_html=True)
    

# def style_background_dashboard_student():

#     st.markdown("""
  
#         <style>

#         .stApp {
#             background: #E0E3FF !important;   
#         } 

#         /* Change the subheader font color white to black */
#         h3 {
#             color: black !important;
#         } 

#         /* Toast background */
#         # [data-testid="stToast"] {
#         #     background-color: #000000 !important;
#         # }
  
                
#         /* Audio traker */
#         /* Content/text color black */
#         [data-testid="stAudioInput"] p {
#             color: #000000 !important;
#         }

#         /* Change the background color of the audio taker */      
#         .st-emotion-cache-1uzegzg {
#             background-color: white !important;  
#         }
#         .st-emotion-cache-oj06lr {
#             color: black !important;
#             background-color: white !important;   
#         }
#         /* when we want to see recording so that case also apply same background is white and text color is balck */
#         .st-emotion-cache-nm0s83 { 
#             color: black !important;
#             background-color: white !important;    
#         }
                
#         /* Target the live wave capture canvas and invert/shift its hue to render Red instead of White */
#         div[data-testid="stAudioInputRecordButton"] canvas {
#             filter: invert(18%) sepia(96%) saturate(6726%) hue-rotate(356deg) brightness(91%) contrast(119%) !important;
#         }   
    
#         /* target the spinner */
#         /* Change its content color to the black */
#         div[data-testid="stSpinner"] > div {
#             color: black !important;
#         }
        
#         /* Change loading symbol color defaultly white to the dark blue */
#         /* border-color expect TOP RIGHT BOTTOM LEFT side color */ 
#         .st-emotion-cache-1vycjxg {
#             border-color: #00008B #00008B #00008B transparent !important;
#         }    
                 
#         </style>

#      """, unsafe_allow_html=True)
    


# # for the base style which can apply every pages of the app
# def style_base_layout():

#     st.markdown("""
  
#         <style>
                
#         /* importing the heading fonts */
#         @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis:YEAR@1985&display=swap');
#         @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@100..900&display=swap');        

#         /* Hide Top Toolbar of the Streamlit */
#         #MainMenu, header, footer {
#             visibility: hidden !important;    
#         }

#         /* Adjust the top spacing of the main header */ 
#         /* Note : Here rem => default font size which browser have which mostly 8px */      
#         .block-container {
#             padding-top: 1.5rem;        
#         }
                
#         /* here we apply Climate-Crisis font style to h1 & h2 tags */
#         h1 {
#             font-family: 'Climate Crisis', sans-serif !important;
#             font-size: 3.5rem !important;
#             line-height: 1.1 !important;
#             margin-bottom: 0rem !important;      
#         }

#         /* streamlit header bydefault use h2 */      
#         h2 {
#             font-family: 'Climate Crisis', sans-serif !important;
#             font-size: 2rem !important;
#             line-height: 0.9 !important;
#             letter-spacing: 2px !important;
#             margin-bottom: 0rem !important; 
#             color: black !important;     
#         }
                
#         h3, h4, p {
#             font-family: 'Outfit', sans-sarif !important;
#         }
        
#         /* button styling additing */          
#         button {
#             border-radius: 1.5rem !important;
#             background: #5865F2 !important;
#             color: white !important;
#             padding: 10px, 20px !important;
#             border: none !important;
#             transition: transform 0.25s ease-in-out !important;   
#         }
                
#         button[kind="secondary"] {
#             border-radius: 1.5rem !important;
#             background: #EB459E !important;
#             color: white !important;
#             padding: 10px, 20px !important;
#             border: none !important;
#             transition: transform 0.25s ease-in-out !important;   
#         }
                
#         button[kind="tertiary"] {
#             border-radius: 1.5rem !important;
#             background: black !important;
#             color: white !important;
#             padding: 10px, 20px !important;
#             border: none !important;
#             transition: transform 0.25s ease-in-out !important;   
#         }
                
#         button:hover {
#             transform: scale(1.05)   
#         }
                
#         /* Input box styling changing */
#         .stTextInput input {
#             background-color: #f5f5f5  !important;
#         }
                
#         div[data-baseweb="input"] {
#             background-color: white !important;
#             border: none !important;
#             box-shadow: none !important;
#         }
                
#         .st-b7 {
#             background-color: rgb(250, 250, 250); 
#         }

#         .stTextInput input::placeholder {
#             color: gray !important;
#             opacity: 1 !important;
#         }    
                
#         .stTextInput label {
#             color: #000000 !important;
#         }
                
#         hr {
#             border-color: gray !important;
#         }
                
#         /* Typed text → gray */
#         .stTextInput input {
#             color: #444444 !important;
#         }

#         /* Red border on focus */
#         div[data-baseweb="input"]:focus-within {
#             outline: 2px solid #FF0000 !important;
#             border: none !important;
#             box-shadow: none !important;
#         }

#         /* Remove inner input border */
#         .stTextInput input:focus {
#             border: none !important;
#             outline: none !important;
#             box-shadow: none !important;
#         }

#         /* Remove eye button left border */
#         div[data-baseweb="input"] button {
#             border: none !important;
#             border-left: none !important;
#             outline: none !important;
#             box-shadow: none !important;
#         }  
        
#         /* Overwrite only the camera_input content */
#         [data-testid="stCameraInput"] [data-testid="stWidgetLabel"] p {
#             color: #000000 !important;
#         } 

#         /* Change the dialog background-color and content color */
#         /* Dialog background → white */
#         [data-testid="stDialog"] > div > div {
#             background-color: #ffffff !important;
#         }

#         /* Dialog title "Create New Subject" → black */
#         /* Button text inside dialog → white */
#         [data-testid="stDialog"] button p {
#             color: #ffffff !important;
#         }

#         /* All other text inside dialog → black */
#         [data-testid="stDialog"] p {
#             color: #000000 !important;
#         }
                

#         /* Change the color of st.code black into the white */
#         [data-testid="stCode"] pre {
#             background-color: #f5f5f5 !important;
#             color: #333333 !important;
#         }
                
#         /* Change the st.selectbox some property */ 
#         /* Chage the selectbox content Label color white to black */
#         .stSelectbox label {
#             color: #000000 !important;
#         }

#         # /* Apply select box right most icon white color to black */
#         # .st-c5 {
#         #     fill: rgb(19, 23, 32);
#         # }
                
#         /* Selected option text inside box → black */
#         /* TODO: replace with proper selector, auto-generated class used as last resort */
#         /* This targets selected option text in st.selectbox */
#         .st-dn {
#             color: #000000 !important;
#         }


#         /* Change the st.file_uplaoder background and content color */
#         /* File uploader background → light gray */
#         # [data-testid="stFileUploader"] section {
#         #     background-color: #f5f5f5 !important;
#         # }

#         # /* File uploader text → black */
#         # [data-testid="stFileUploader"] section span {
#         #     color: #000000 !important;
#         # }  

#         /* Consistant the all warning buttons like st.warning st.info etc content color */
#         /* st.error → darker red */
#         [data-testid="stAlert"][kind="error"] {
#             background-color: #f5c6cb !important;
#             border-color: #c0392b !important;
#         }    

#         /* st.warning → darker yellow */
#         [data-testid="stAlert"][kind="warning"] {
#             background-color: #ffeaa0 !important;
#             border-color: #d68910 !important;
#         }

#         /* st.success → darker green */
#         [data-testid="stAlert"][kind="success"] {
#             background-color: #a9dfbf !important;
#             border-color: #1e8449 !important;
#         }

#         /* st.info → darker blue */
#         [data-testid="stAlert"][kind="info"] {
#             background-color: #aed6f1 !important;
#             border-color: #1a5276 !important;
#         }

#         /* Fix content color back to default for all alerts — removes black bug */
#         [data-testid="stAlert"] p {
#             color: inherit !important;
#         }


#         </style>

#      """, unsafe_allow_html=True)




# ===================================================================================================================
# ===================================================================================================================

import streamlit as st

# ---------------------------------------------------------------------------
# NEW PALETTE (change a color here by find-and-replace in this file)
#   Ink (text, borders, shadows) : #1B1B3A
#   Cream (dashboard background) : #FFF4E0
#   Soft white (cards, dialogs)  : #FFFBF2
#   Deep teal (primary)          : #0F766E
#   Coral (secondary)            : #E8553A
# ---------------------------------------------------------------------------


def style_background_home():

    st.markdown("""

        <style>

            .stApp {
                background: #0F766E !important;
            }

            /* Student / Teacher cards on the home screen */
            .stApp div[data-testid="stColumn"] {
                background-color: #FFF4E0 !important;
                padding: 2.5rem !important;
                border: 3px solid #1B1B3A !important;
                border-radius: 2rem !important;
                box-shadow: 8px 8px 0 #1B1B3A !important;
            }

        </style>

     """, unsafe_allow_html=True)


def style_background_dashboard_teacher():

    st.markdown("""

        <style>

        .stApp {
            background: #FFF4E0 !important;
        }

        h3 {
            color: #1B1B3A !important;
        }

        /* Spinner text */
        div[data-testid="stSpinner"] > div {
            color: #1B1B3A !important;
        }

        /* Spinner circle color (auto-generated class, same one you used before) */
        .st-emotion-cache-1vycjxg {
            border-color: #0F766E #0F766E #0F766E transparent !important;
        }

        /* Audio recorder text */
        [data-testid="stAudioInput"] p {
            color: #1B1B3A !important;
        }

        </style>

     """, unsafe_allow_html=True)


def style_background_dashboard_student():

    st.markdown("""

        <style>

        .stApp {
            background: #FFF4E0 !important;
        }

        h3 {
            color: #1B1B3A !important;
        }

        /* Audio recorder text */
        [data-testid="stAudioInput"] p {
            color: #1B1B3A !important;
        }

        /* Audio recorder background (auto-generated classes, same ones you used before) */
        .st-emotion-cache-1uzegzg {
            background-color: #FFFBF2 !important;
        }
        .st-emotion-cache-oj06lr {
            color: #1B1B3A !important;
            background-color: #FFFBF2 !important;
        }
        .st-emotion-cache-nm0s83 {
            color: #1B1B3A !important;
            background-color: #FFFBF2 !important;
        }

        /* Recording wave: shift the color to red */
        div[data-testid="stAudioInputRecordButton"] canvas {
            filter: invert(18%) sepia(96%) saturate(6726%) hue-rotate(356deg) brightness(91%) contrast(119%) !important;
        }

        /* Spinner text */
        div[data-testid="stSpinner"] > div {
            color: #1B1B3A !important;
        }

        /* Spinner circle color */
        .st-emotion-cache-1vycjxg {
            border-color: #0F766E #0F766E #0F766E transparent !important;
        }

        </style>

     """, unsafe_allow_html=True)


# Base style applied on every page of the app
def style_base_layout():

    st.markdown("""

        <style>

        /* New fonts: Syne for headings, DM Sans for body text */
        @import url('https://fonts.googleapis.com/css2?family=Syne:wght@600;800&family=DM+Sans:wght@400;500;700&display=swap');

        /* Hide Streamlit's default top toolbar and footer */
        #MainMenu, header, footer {
            visibility: hidden !important;
        }

        .block-container {
            padding-top: 1.5rem;
        }

        /* Body font (p, labels, inputs only, so icon fonts are not affected) */
        .stApp, p, label, input, textarea {
            font-family: 'DM Sans', sans-serif;
        }

        h1 {
            font-family: 'Syne', sans-serif !important;
            font-weight: 800 !important;
            font-size: 3.2rem !important;
            line-height: 1.1 !important;
            margin-bottom: 0rem !important;
            letter-spacing: -1px !important;
        }

        h2 {
            font-family: 'Syne', sans-serif !important;
            font-weight: 800 !important;
            font-size: 1.9rem !important;
            line-height: 1 !important;
            letter-spacing: 0.5px !important;
            margin-bottom: 0rem !important;
            color: #1B1B3A !important;
        }

        h3, h4 {
            font-family: 'Syne', sans-serif !important;
            font-weight: 600 !important;
        }

        p {
            font-family: 'DM Sans', sans-serif !important;
        }

        /* ---------- BUTTONS ---------- */
        /* Primary (default) = deep teal */
        button {
            border-radius: 0.9rem !important;
            background: #0F766E !important;
            color: white !important;
            padding: 10px 20px !important;
            border: 2px solid #1B1B3A !important;
            box-shadow: 3px 3px 0 #1B1B3A !important;
            font-weight: 700 !important;
            transition: transform 0.15s ease-in-out, box-shadow 0.15s ease-in-out !important;
        }

        /* Secondary = coral */
        button[kind="secondary"] {
            border-radius: 0.9rem !important;
            background: #E8553A !important;
            color: white !important;
            padding: 10px 20px !important;
            border: 2px solid #1B1B3A !important;
            box-shadow: 3px 3px 0 #1B1B3A !important;
        }

        /* Tertiary = ink navy */
        button[kind="tertiary"] {
            border-radius: 0.9rem !important;
            background: #1B1B3A !important;
            color: white !important;
            padding: 10px 20px !important;
            border: 2px solid #1B1B3A !important;
            box-shadow: 3px 3px 0 #E8553A !important;
        }

        /* Hover: the button "lifts" up and its shadow grows */
        button:hover {
            transform: translate(-2px, -2px) !important;
            box-shadow: 5px 5px 0 #1B1B3A !important;
        }

        /* ---------- TEXT INPUTS ---------- */
        .stTextInput input {
            background-color: #FFFBF2 !important;
            color: #1B1B3A !important;
        }

        div[data-baseweb="input"] {
            background-color: #FFFBF2 !important;
            border: 2px solid #1B1B3A !important;
            border-radius: 0.9rem !important;
            box-shadow: none !important;
        }

        .stTextInput input::placeholder {
            color: #7A7A95 !important;
            opacity: 1 !important;
        }

        .stTextInput label {
            color: #1B1B3A !important;
            font-weight: 700 !important;
        }

        hr {
            border-color: rgba(27, 27, 58, 0.35) !important;
        }

        /* Coral outline when the input is focused */
        div[data-baseweb="input"]:focus-within {
            outline: 3px solid #E8553A !important;
            box-shadow: none !important;
        }

        .stTextInput input:focus {
            border: none !important;
            outline: none !important;
            box-shadow: none !important;
        }

        /* Password "eye" button: no border or shadow */
        div[data-baseweb="input"] button {
            border: none !important;
            border-left: none !important;
            outline: none !important;
            box-shadow: none !important;
        }

        /* Camera input label */
        [data-testid="stCameraInput"] [data-testid="stWidgetLabel"] p {
            color: #1B1B3A !important;
        }

        /* ---------- DIALOGS ---------- */
        [data-testid="stDialog"] > div > div {
            background-color: #FFFBF2 !important;
            border: 3px solid #1B1B3A !important;
            border-radius: 1.5rem !important;
        }

        /* Button text inside dialog stays white */
        [data-testid="stDialog"] button p {
            color: #ffffff !important;
        }

        /* All other text inside dialog */
        [data-testid="stDialog"] p {
            color: #1B1B3A !important;
        }

        /* ---------- CODE BLOCK ---------- */
        [data-testid="stCode"] pre {
            background-color: #FFFBF2 !important;
            color: #1B1B3A !important;
            border: 2px solid #1B1B3A !important;
        }

        /* ---------- SELECTBOX ---------- */
        .stSelectbox label {
            color: #1B1B3A !important;
            font-weight: 700 !important;
        }

        /* Selected option text (auto-generated class, same one you used before) */
        .st-dn {
            color: #1B1B3A !important;
        }

        /* ---------- ALERTS ---------- */
        [data-testid="stAlert"][kind="error"] {
            background-color: #FFD6CC !important;
            border-color: #E8553A !important;
        }

        [data-testid="stAlert"][kind="warning"] {
            background-color: #FFE8A3 !important;
            border-color: #C98A00 !important;
        }

        [data-testid="stAlert"][kind="success"] {
            background-color: #BFEAD9 !important;
            border-color: #0F766E !important;
        }

        [data-testid="stAlert"][kind="info"] {
            background-color: #CFE6F5 !important;
            border-color: #1B4F72 !important;
        }

        /* Keep alert text in its default color */
        [data-testid="stAlert"] p {
            color: inherit !important;
        }

        </style>

     """, unsafe_allow_html=True)