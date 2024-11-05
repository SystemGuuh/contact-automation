import streamlit as st
import pyautogui
import pandas as pd
from assets.email_functions import *
from assets.data_functions import *

def buildEmailPage(data):
    email_option = st.selectbox(
            "What e-mail you want to send?",
            ("1", "2", "3", "4"),
            index=None,
            placeholder="Select e-mail type...",
            )
    
    first= data.iloc[0]

    if email_option == '1':
        subject = st.text_input("Subject:", getInitialSubject(first['Nome']))
        body = st.text_area("Email body:",getInitialBody(first['Nome'],first['Data1'],first['Data2']), height=500)


    elif email_option == '2':
        subject = getDefaultSubject(first['Nome'])
        body = getDefaultBody(first['Nome'],first['Data1'],first['Data2'])
        with st.expander(subject):
            st.write(body)

    elif email_option == '3':
        subject = getFinalSubject(first['Nome'])
        body = getFinalBody(first['Nome'],first['Data1'],first['Data2'])
        with st.expander(subject):
            st.write(body)

    elif email_option == '4':
        subject = getExpiredSubject(first['Nome'])
        body = getExpiredBody(first['Nome'])
        with st.expander(subject):
            st.write(body)

    col1, col2, col3, col4 = st.columns(4)
    if email_option: 
        lines = col1.selectbox("Send to:", range(1, len(data) + 1))
    
        col2.write('')
        col2.write('')
        if col2.button("Send Emails", type="primary"):
            goToOutlook()
            for index, row in data.iterrows():
                if index <= 80:
                    sendEmail(row)
                else: break
