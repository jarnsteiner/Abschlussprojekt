import streamlit as st

def show():
    st.title("Registration")
    #st.divider()
    st.subheader("Neues Konto erstellen")

    firstname = st.text_input("Vorname", key="reg_firstname")
    lastname = st.text_input("Nachname", key="reg_lastname")
    username = st.text_input("Benutzername", key="reg_username")
    password1 = st.text_input("Passwort", type="password", key= "reg_password1")
    password2 = st.text_input("Passwort wiederholen", type="password", key= "reg_password2")
    
    col = st.columns(2)

    with col[0]:
        if st.button("Registrieren", use_container_width=True) and check_person(firstname, lastname, username, password1, password2) == True:
            print("Erfolgreich registriert")

            #überprüft person
            
    
    
    with col[1]:
        if st.button("zum Login zurück", use_container_width=True):
            st.session_state.page = "login"
            st.rerun()

def check_person(firstname, lastname, username, password1, password2):
    if firstname.strip() == "":
        st.error("Bitte Vornamen eingeben")
        return False
    if lastname.strip() == "":
        st.error("Bitte Nachnamen eingeben")
        return False
    if username.strip() == "":
        st.error("Bitte Benutzername eingeben")
        return False
    if password1 != password2:
        st.error("Passwort stimmt nicht überein")
        return False
    return True
    
