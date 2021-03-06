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
from Bio import SeqIO
from st_aggrid import AgGrid, GridOptionsBuilder
import sys
path = os.path.dirname(os.path.abspath(__file__))
path = path.split('pages')[0]
sys.path.append(path + 'methods/')
from ExtractionTechniques import *


#############################################################################

def charts(foutput):
    st.title("Plotting Box Plot Chart - Choose a column ")
    try:
        df = pd.read_csv(foutput)
        column = st.selectbox('', df.columns[1:len(df.columns) - 1])
        if column:
            chart = go.Figure(data=[go.Box(y=df[column],
                                           boxpoints='all',
                                           jitter=0.3,
                                           pointpos=-1.8)])
            chart.update_layout(
                margin=dict(l=40, r=40, t=40, b=40))
            # chart.update_xaxes(title_text='test')
            st.success("Generated Charts!!!")
            st.plotly_chart(chart, use_container_width=True)
            # gb = GridOptionsBuilder.from_dataframe(df)
            # gb.configure_pagination()
            # gb.configure_side_bar()
            # gb.configure_default_column(groupable=True,value=True,
            #                             enableRowGroup=True,aggFunc="sum",editable=True)
            # grid_options = gb.build()
            # AgGrid(df,gridOptions=grid_options,enable_enterprise_modules=True)
    except:
        st.error('Plotting Box Plot Chart - Error')


def app():
    st.title("Descriptor: Customized k-mer (Protein)")
    st.markdown("Author: Robson Parmezan Bonidia")

    if 'foutput' not in st.session_state:
        st.session_state.foutput = ''
    #############################################################################
    with st.form(key='form'):
        finput = st.file_uploader('Choose your .fasta file', type=["fasta", "fa", "faa"])
        window = st.number_input('Sliding Window (e.g., 10, 20, 30, 40):', min_value=1, step=1)
        step = st.number_input('Window Step (e.g., 3, 4):', min_value=1, step=1)
        ksize = st.number_input('k-mer Frequency in Window (e.g., 1, 2, 3, 4):', min_value=1, step=1)
        label_dataset = st.text_input('Dataset Label, e.g., lncRNA, mRNA, sncRNA')
        caracteres = ['A', 'C', 'D', 'E', 'F',
                      'G', 'H', 'I', 'K', 'L',
                      'M', 'N', 'P', 'Q', 'R',
                      'S', 'T', 'V', 'W', 'Y']
        submit = st.form_submit_button(label='Submit')

    if submit:
        try:
            byte_str = finput.read()
            finput = byte_str.decode('UTF-8')
            my_bar = st.progress(20)
            st.success("Extracting Features!!!")

            foutput = seqKGAP(finput, caracteres, label_dataset, window, ksize, step)
            if st.session_state.foutput != foutput or st.session_state.foutput != '':
                st.session_state.foutput = foutput

            st.success("Recorded Sequences!!!")
            my_bar.progress(100)
            # download = st.button(label='Download CSV file')
        except:
            st.error('Some error happened! Please fill out so required fields!')
    else:
        st.warning("Please fill out so required fields")


    # if st.session_state.foutput != '' and ksize <= 5:
    #     try:
    #         df = pd.read_csv(st.session_state.foutput)
    #         gb = GridOptionsBuilder.from_dataframe(df)
    #         gb.configure_pagination()
    #         gb.configure_side_bar()
    #         gb.configure_default_column(groupable=True,value=True,
    #                                     enableRowGroup=True, aggFunc="sum", editable=False)
    #         grid_options = gb.build()
    #         AgGrid(df, gridOptions=grid_options, enable_enterprise_modules=True)
    #     except:
    #         st.error('An error occurred while reading csv file!')
    #
    #
    # if st.session_state.foutput != '' and ksize <= 5:
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
            download = st.button(label='Download CSV file')
            file_size = (os.path.getsize(st.session_state.foutput) / 1024) / 1024
            if download:
                try:
                    if file_size < 40:
                        df = pd.read_csv(st.session_state.foutput)
                        csv = df.to_csv(index=False)
                        b64 = base64.b64encode(csv.encode()).decode()
                        # webbrowser.open('data:file/csv;base64,' + b64)
                        link = f'<a href="data:file/csv;base64,{b64}" ' \
                               f'download="dataset.csv">Download CSV file</a>'
                        st.markdown(link, unsafe_allow_html=True)
                        st.success('Download successful!')
                    else:
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
