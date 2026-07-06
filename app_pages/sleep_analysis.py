import streamlit as st
import pandas as pd
from src.sleep_data import sleep_data

def show():
    st.set_page_config(
        page_title="Schlafanalyse",
        page_icon="💤",
        layout="wide"
    )
    
    st.title("Schlafanalyse")

    person = st.session_state.user

    
    st.write(person.get_full_name())
    st.write(person.smartwatch_data)
    data = person.smartwatch_data
    st.write(data[0]["result_link"])
    file = data[0]["result_link"]
    df = pd.read_csv(file)
    
    sleep001 = sleep_data(file)
    sleep001.load_data()
    data_filtered = sleep001.filter_data()
    print(data_filtered)
