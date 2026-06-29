import streamlit as st
from src.person import Person
from src.ekg_data import EKGdata
from src.read_data import load_person_data, get_name_to_id

st.set_page_config(
    page_title="Schlafanalyse",
    page_icon="🌙",
    layout="wide"
)
#set Pages
overview = st.Page("pages/overview.py", title="Übersicht", icon="🏠")
analysis = st.Page("pages/analysis.py", title="Schlafanalyse", icon="📊")
account = st.Page("pages/account.py", title="Schlafphasen", icon="📊")

pg = st.navigation([overview, analysis, account])


