#!/usr/bin/env python
# -*- coding: utf-8 -*-

import warnings
import numpy as np
import pandas as pd
import streamlit as st
import os
import io
import time
import plotly.express as px
import plotly.graph_objects as go
import base64
import webbrowser
from link_button import link_button
from Bio import SeqIO
from st_aggrid import AgGrid, GridOptionsBuilder
import sys
path = os.path.dirname(os.path.abspath(__file__))
path = path.split('pages')[0]
sys.path.append(path + 'preprocessing/')
from remove_redundancy import *


#############################################################################

def app():
    st.title("Descriptor: To remove repeated sequences in a file")
    st.markdown("Author: Robson Parmezan Bonidia")

    if 'foutput' not in st.session_state:
        st.session_state.foutput = ''
    #############################################################################
    with st.form(key='form'):
        finput = st.file_uploader('Choose your .fasta file', type=["fasta", "fa", "faa"])
        submit = st.form_submit_button(label='Submit')

    if submit:
        try:
            byte_str = finput.read()
            finput = byte_str.decode('UTF-8')
            my_bar = st.progress(20)
            st.success("Preprocessing!!!")

            foutput = remove_equal_sequences(finput)
            if st.session_state.foutput != foutput or st.session_state.foutput != '':
                st.session_state.foutput = foutput

            st.success("Finished!!!")
            my_bar.progress(100)
            # download = st.button(label='Download CSV file')
        except:
            st.error('Some error happened! Please fill out so required fields!')
    else:
        st.warning("Please fill out so required fields")


    # if st.session_state.foutput != '':
    #     try:
    #         df = pd.read_csv(st.session_state.foutput)
    #         gb = GridOptionsBuilder.from_dataframe(df)
    #         gb.configure_pagination()
    #         gb.configure_side_bar()
    #         gb.configure_default_column(groupable=True, value=True,
    #                                     enableRowGroup=True, aggFunc="sum", editable=True)
    #         grid_options = gb.build()
    #         AgGrid(df, gridOptions=grid_options, enable_enterprise_modules=True)
    #     except:
    #         st.error('An error occurred while reading csv file!')
    #
    #
    # if st.session_state.foutput != '':
    #     try:
    #         # st.text(st.session_state.foutput)
    #         charts(st.session_state.foutput)
    #     except:
    #         st.error('Plotting Box Plot Chart - Error')
    #
    # else:
    #     st.error("Any problem, contact us!")


    if st.session_state.foutput != '':
        try:
            st.title('Download - Dataset')
            download = st.button(label='Download Fasta file')
            if download:
                try:
                    # st.text(st.session_state.foutput.split)
                    foutput_down = st.session_state.foutput.split('/')[-1]
                    # st.text(foutput_down)
                    webbrowser.open('ftp://mathfeature:%26l%23t%24L%5'
                                    'EEx9BWHYGpZR@localhost:2121/' + foutput_down)
                except:
                    st.error('Download error!')
        except:
            st.error('An error occurred while reading csv file!')
    else:
        st.success('Author: Robson Parmezan Bonidia')

# streamlit run your_script.py --server.maxUploadSize=1028
#############################################################################
