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
    


def style_background_dashboard():

    st.markdown("""
  
        <style>

            .stApp {
                background: #E0E3FF !important;   
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
            background-color: white !important;
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
        </style>

     """, unsafe_allow_html=True)