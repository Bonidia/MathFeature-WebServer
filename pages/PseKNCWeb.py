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
sys.path.append(path + 'methods/')
from PseKNC import *


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
    st.title("Descriptor: Pseudo K-tuple nucleotide composition")
    st.markdown("Author: Robson Parmezan Bonidia")

    if 'foutput' not in st.session_state:
        st.session_state.foutput = ''
    #############################################################################
    with st.form(key='form'):
        finput = st.file_uploader('Choose your .fasta file', type=["fasta", "fa", "faa"])
        type_seq = st.selectbox('Type of sequence', ['DNA', 'RNA'])
        type_t = st.selectbox('PseKNC Type', ['Type 1 PseKNC', 'Type 2 PseKNC'])
        type_k = st.selectbox('Kind of oligonucleotide', ['Dinucleotide', 'Trinucleotide'])
        j = st.number_input('Set the value of lambda parameter '
                            'in the PseKNC algorithm.'
                            'Must be smaller than the '
                            'length of any query sequence, e.g., 1', min_value=1, step=1)
        w = st.number_input('Set the value of weight parameter in '
                            'the PseKNC algorithm. '
                            'It can be a value between (0, 1]', min_value=0.1, step=0.1, max_value=1.0)
        s = st.number_input('Calculate only the '
                            'frequency of each oligonucleotide in the input sequence. '
                            'Unless otherwise specified, e.g., 2', min_value=2, step=1, max_value=3)
        label_dataset = st.text_input('Dataset Label, e.g., lncRNA, mRNA, sncRNA')
        submit = st.form_submit_button(label='Submit')

    if submit:
        try:
            byte_str = finput.read()
            finput = byte_str.decode('UTF-8')
            my_bar = st.progress(20)
            st.success('Extracting Features!!!')

            if type_seq == 'DNA':
                allowed_chars = ['A', 'C', 'G', 'T']
                seq = 1
            else:
                allowed_chars = ['A', 'C', 'G', 'U']
                seq = 2

            if type_t == 'Type 1 PseKNC':
                t = 1
            else:
                t = 2

            if type_k == 'Dinucleotide':
                k = 2
            else:
                k = 3

            x = ''
            xp = ''
            if seq == 1 and k == 2:
                x = path + 'files/propNames-DNA-k2.txt'
                xp = path + 'files/propValues-DNA-k2.txt'
            elif seq == 1 and k == 3:
                x = path + 'files/propNames-DNA-k3.txt'
                xp = path + 'files/propValues-DNA-k3.txt'
            elif seq == 2 and k == 2:
                x = path + 'files/propNames-RNA-k2.txt'
                xp = path + 'files/propValues-RNA-k2.txt'

            foutput = parameters(xp, x, t, k, j, w, s, finput, label_dataset, seq, allowed_chars)
            if st.session_state.foutput != foutput or st.session_state.foutput != '':
                st.session_state.foutput = foutput
            st.success('Recorded Sequences!!!')
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
    #         gb.configure_default_column(groupable=True,value=True,
    #                                     enableRowGroup=True,aggFunc="sum",editable=True)
    #         grid_options = gb.build()
    #         AgGrid(df,gridOptions=grid_options,enable_enterprise_modules=True)
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
