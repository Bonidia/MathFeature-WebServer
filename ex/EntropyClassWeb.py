#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys
import warnings
warnings.filterwarnings("ignore")
import numpy as np
import pandas as pd
import argparse
import math 
import streamlit as st
import os
import io
import time
import plotly.express as px
import plotly.graph_objects as go
import base64
import webbrowser
from stqdm import stqdm
from Bio import SeqIO
from st_aggrid import AgGrid, GridOptionsBuilder
from itertools import product


#############################################################################  


def header(ksize):
    file = open(foutput, 'a')
    file.write("nameseq,")
    for i in range(1, ksize+1):
        file.write("k" + str(i) + ",")
    file.write("label")
    file.write("\n")
    return


def chunks(seq, win, step):
    seqlen = len(seq)
    for i in range(0,seqlen,step):
        j = seqlen if i+win>seqlen else i+win
        yield seq[i:j]
        if j==seqlen: break
    return        
    

def chunks_two(seq, win):
    seqlen = len(seq)
    for i in range(seqlen):
        j = seqlen if i+win>seqlen else i+win
        yield seq[i:j]
        if j==seqlen: break
    return

            
def file_record():
    file = open(foutput, 'a')
    file.write("%s," % (name_seq))
    for data in information_entropy:
        file.write("%s," % (str(data)))
    file.write(label_dataset)
    file.write("\n")
    # print ("Recorded Sequence!!!")
    return
    

def entropy_equation():
    header(ksize)
    global name_seq, information_entropy
    for seq_record in SeqIO.parse(io.StringIO(finput), "fasta"):
        seq = seq_record.seq
        seq = seq.upper()
        name_seq = seq_record.name
        information_entropy = []
        for k in range(1, ksize+1):
            probabilities = []
            kmer = {}
            total_windows = (len(seq) - k) + 1 # (L - k + 1)
            for subseq in chunks_two(seq, k):
                if subseq in kmer:
                    # print(subseq)
                    kmer[subseq] = kmer[subseq] + 1
                else:
                    kmer[subseq] = 1
            for key, value in kmer.items():
                # print(key)
                # print(value)
                probabilities.append(value/total_windows)
            if e == "Shannon" or e == "shannon":
                entropy_equation = [(p * math.log(p, 2)) for p in probabilities]
                entropy = -(sum(entropy_equation))
                information_entropy.append(entropy)
            else:
                q = 2
                entropy_equation = [(p ** q) for p in probabilities]
                entropy =  (1/(q - 1)) * (1 - sum(entropy_equation))
                information_entropy.append(entropy)
        file_record()
    return

        
#############################################################################    

def file_selector(folder_path='.'):
    filenames = os.listdir(folder_path)
    selected_filename = st.sidebar.selectbox('Select a file', filenames)
    return os.path.join(folder_path, selected_filename)


def read_csv(foutput):
    dataset = pd.read_csv(foutput)
    return dataset


#############################################################################

def app():

    st.set_page_config(page_title="MathFeature", layout="wide", page_icon="img/mathfeature.png")

    st.markdown(""" <style>
    MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style> """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1,1,1])
    with col1:
    	st.write("")
    with col2:
    	st.image("../img/mathfeature-bk.png")
    with col3:
    	st.write("")

    # st.image("img/mathfeature-bk.png")
    st.title("MathFeature Package")
    st.markdown("Feature Extraction Package for Biological Sequences Based on Mathematical Descriptors")

    # st.image("img/mathfeature-bk.png", use_column_width=True)

    st.title("Descriptor: Entropy")
    st.markdown("Author: Robson Parmezan Bonidia")

#############################################################################  
    
    global finput, ksize, foutput, label_dataset, e
    foutput = ''
    with st.form(key='form'):
    	finput = st.file_uploader('Choose your .fasta file', type=["fasta", "fa", "faa"])
    	ksize = st.number_input('Range of k-mer, e.g., 1-mer (1) or 2-mer (1, 2)', min_value=1, step=1)
    	foutput = st.text_input('Output File - Name, e.g., dataset.csv, features.csv')
    	label_dataset = st.text_input('Dataset Label, e.g., lncRNA, mRNA, sncRNA')
    	e = st.selectbox('Entropy', ['Shannon', 'Tsallis (q = 2.0)'])
    	# option_three = st.sidebar.selectbox('Options:', ('Data Summary', 'Age', 'Job', 'Duration',...))
    	# option_four = st.sidebar.selectbox('Options:', ('Data Summary', 'Age', 'Job', 'Duration',...))
    	stepw = 1
    	submit = st.form_submit_button(label='Submit')


    if submit and finput and ksize and foutput and label_dataset:
        try:
            byte_str = finput.read()
            finput = byte_str.decode('UTF-8')
            my_bar = st.progress(20)
            st.success("Extracting Features!!!")
            entropy_equation()
            st.success("Recorded Sequences!!!")
            my_bar.progress(100)
            # download = st.button(label='Download CSV file')
            try:
                df = pd.read_csv(foutput)
                gb = GridOptionsBuilder.from_dataframe(df)
                gb.configure_pagination()
                gb.configure_side_bar()
                gb.configure_default_column(groupable=True, value=True, 
                	enableRowGroup=True, aggFunc="sum", editable=True)
                gridOptions = gb.build()
                AgGrid(df, gridOptions=gridOptions, enable_enterprise_modules=True)
            except:
                st.error('An error occurred while reading csv file.')
        except:
            st.error('Some error happened! Please fill out so required fields!')
            st.error('Report any problem to our repository!') 
    else:
        st.warning("Please fill out so required fields")


    try:
        df = pd.read_csv(foutput)
        st.title("Plotting Box Plot Chart - Choose a column ")
        with st.form(key='form_two'):
            column = st.selectbox('', df.columns[1:len(df.columns)-1])
            submit_chart = st.form_submit_button(label='Submit')
        if submit_chart:    
            try:         
                chart = go.Figure(data=[go.Box(y=df[column],
                    boxpoints='all',
                    jitter=0.3,
                    pointpos=-1.8)])
                chart.update_layout(
                    margin=dict(l=40, r=40, t=40, b=40))
                    # chart.update_xaxes(title_text='test')
                st.success("Generated Charts!!!")
                st.plotly_chart(chart, use_container_width=True)
                gb = GridOptionsBuilder.from_dataframe(df)
                gb.configure_pagination()
                gb.configure_side_bar()
                gb.configure_default_column(groupable=True, value=True, 
                	enableRowGroup=True, aggFunc="sum", editable=True)
                gridOptions = gb.build()
                AgGrid(df, gridOptions=gridOptions, enable_enterprise_modules=True)
            except:
                st.error('Plotting Box Plot Chart - Error')  
    except:
        st.error('Report any problem to our repository!')  


    try:
        df = pd.read_csv(foutput)
        st.title('Download - Dataset')
        download = st.button(label='Download CSV file')
        if download:
            st.success('Download successful!')
            try:
                csv = df.to_csv(index=False)
                b64 = base64.b64encode(csv.encode()).decode()
                webbrowser.open('data:file/csv;base64,'+b64)
                # link = f'<a href="data:file/csv;base64,{b64}" download="dataset.csv">Download csv file</a>'
                # st.markdown(link, unsafe_allow_html=True)
            except:
                st.error('Download error!')  
    except:
        st.success('Author: Robson Parmezan Bonidia') 

#streamlit run your_script.py --server.maxUploadSize=1028
app()
#############################################################################