import streamlit as st
from assets.email_functions import *

def component_select_bdc():
    return st.selectbox(
            "Who are you?",
            ("Gustavo Almeida", "Lidiane Faria", "Melissa Cruz", "Nenhum"),
            index=None,
            placeholder="Select subject type...",
            )
    
def component_select_subject():
    return st.selectbox(
            "What e-mail Subject you want to send?",
            ("Primeiro Contato", "Segundo Contato", "Contato Final", "Expirado"),
            index=None,
            placeholder="Select subject type...",
            )

def component_select_body():
    return st.selectbox(
            "What e-mail Body you want to send?",
            ("Primeiro Contato", "Segundo Contato", "Contato Final", "Expirado"),
            index=None,
            placeholder="Select e-mail type...",
            )

def component_show_subject_option(subject_option, first, bdc):
    container = st.container(border=True)
    with container:
        if subject_option == "Primeiro Contato":
            st.write(getInitialSubject(first['Nome'], bdc))
        elif subject_option == "Segundo Contato":
            st.write(getDefaultSubject(first['Nome'], bdc))
        elif subject_option == "Contato Final":
            st.write(getFinalSubject(first['Nome'], bdc))
        elif subject_option == "Expirado":
            st.write(getExpiredSubject(first['Nome'], bdc))
        else:
            return
        
def component_show_body_option(email_option, first, bdc):
    container = st.container(border=True)
    with container:
        if email_option == "Primeiro Contato":
            st.write(getInitialBody(first['Nome'],first['Data1'],first['Data2'], bdc))
        elif email_option == "Segundo Contato":
            st.write(getDefaultBody(first['Nome'],first['Data1'],first['Data2'], bdc))
        elif email_option == "Contato Final":
            st.write(getFinalBody(first['Nome'],first['Data1'],first['Data2'], bdc))
        elif email_option == "Expirado":
            st.write(getExpiredBody(first['Nome'], bdc))
        else:
            return
