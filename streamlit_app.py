import streamlit as st
import pandas as pd
from assets.email_page import buildEmailPage
from assets.data_functions import checkColumns


st.set_page_config(page_title="Autonomous Bot",page_icon="🏎️", layout="wide")
st.title("Autonomous Email, Whatsapp, Linkdinln sender")

st.divider()

st.write('Upload data containing columns: Nome|Email|Data1|Data2')
colum1, colum2= st.columns([1, 2])
uploaded_file = colum1.file_uploader("Choose a XLSX file", type=["xlsx"], accept_multiple_files=False)

st.divider()
if uploaded_file is not None:
    df =  pd.read_excel(uploaded_file)

    required_columns = ['Nome', 'Email', 'Data1', 'Data2']
    if missing_columns := checkColumns(df, required_columns):
        colum2.error(f'Error: missing columns: {missing_columns}')
        df = None

    if df is not None:
            
        tab1, tab2, tab3 = st.tabs(["Email", "Whatsapp", "Linkdinln"])
        with tab1:
            buildEmailPage(df)

        with tab2:
            whatsapp_option = st.selectbox(
            "What whatsapp mensage you want to send?",
            ("1", "2", "3", "4"),
            index=None,
            placeholder="Select mensage type...",
            )

        with tab3:
            linkdinln_option = st.selectbox(
            "What linkdinln mensage you want to send?",
            ("1", "2", "3", "4"),
            index=None,
            placeholder="Select mensage type...",
            )

