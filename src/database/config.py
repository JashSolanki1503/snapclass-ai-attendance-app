import streamlit as st

from supabase import Client, create_client

supabase: Client = create_client(
    st.secrets["SUPABASE_URL"], # give url of the database
    st.secrets["SUPABASE_KEY"] # give main access key of the database 
)