import streamlit as st
import pyautogui
import pandas as pd
from assets.email_functions import *
from assets.data_functions import *
from assets.components import *

def buildEmailPage(data):
    first= data.iloc[0]

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        bdc = component_select_bdc()
    with col2:
        subject_option = component_select_subject()
    with col3:
        body_option = component_select_body()
    
    component_show_subject_option(subject_option, first, bdc)
    component_show_body_option(body_option, first, bdc)

    col1, col2, col3, col4 = st.columns(4)
    if body_option: 
        lines = col1.selectbox("Send until line:", range(1, len(data) + 1))
    
        col2.write('')
        col2.write('')

        if col2.button("Send Emails", type="primary"):
            goToOutlook()
            for index, row in data.iterrows():
                if index <= (lines+1):
                    if subject := getSubject(row, subject_option, bdc):
                        if body := getBody(row, body_option, bdc):
                            sendEmail(row, subject, body)
                else: break
