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
from count_bases import *


#############################################################################

def app():
    st.title("Descriptor: Sequences and Bases/Nucleotide Count")
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
            st.success("Extracting Features!!!")
            length, seq = count_sequences(finput)
            st.success("Finished!!!")
            my_bar.progress(100)

            st.write("Min Length: %s" % (min(length)))
            st.write("Max Length: %s" % (max(length)))
            st.write("Mean Length: %s" % ((sum(length)/len(length))))
            st.write("Number of Sequences: %s" % seq)

            # download = st.button(label='Download CSV file')
        except:
            st.error('Some error happened! Please fill out so required fields!')
    else:
        st.warning("Please fill out so required fields")

# streamlit run your_script.py --server.maxUploadSize=1028
#############################################################################
