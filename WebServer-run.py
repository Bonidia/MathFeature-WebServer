#!/usr/bin/env python
# -*- coding: utf-8 -*-

import warnings
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
import multiprocessing
from Bio import SeqIO
from itertools import product
import sys

#############################################################################
path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(path + '/class/')
sys.path.append(path + '/pages/')
from multiapp import MultiPage
from link import link_button
############################################################################# 

import EntropyClassWeb
import TsallisEntropyWeb
import ComplexNetworksClassWeb
import ComplexNetworksClassV2Web
import KmerDNAWeb
import KgapWeb
import FickettScoreWeb
import CodingWeb
import PseKNCWeb
import AAIndexWeb
import NACWeb
import DNCWeb
import TNCWeb
import CKmerDNAWeb
import CKmerProteinWeb
import KmerProteinWeb
import AACWeb
import DPCWeb
import TPCWeb
import FourierDNAWeb
import ANFDWeb
import ANFDFourierWeb
import ChaosClassicalWeb
import ChaosFreqWeb
import ChaosSignalWeb
import MappingDNAWeb
import ANFProteinWeb
import IntegerProteinWeb
import EIIPProteinWeb
import KmerMapProteinWeb
import ANFProteinFourierWeb
import IntegerProteinFourierWeb
import EIIPProteinFourierWeb
import KmerMapProteinFourierWeb
import PreSamplingWeb
import PreprocessingWeb
import PreCountWeb
import PreRedundWeb
import PreConcatWeb

#############################################################################
warnings.filterwarnings("ignore")
#############################################################################

st.set_page_config(page_title="MathFeature", layout="wide", page_icon="img/mathfeature.png")

st.markdown(""" <style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style> """, unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 1, 1])
with col1:
    st.write("")
with col2:
    st.image("img/mathfeature-bk.png")
with col3:
    st.write("")

# st.image("img/mathfeature-bk.png")
st.title("MathFeature Package")
st.markdown("Feature Extraction Package for Biological Sequences Based on Mathematical Descriptors")

# st.image("img/mathfeature-bk.png", use_column_width=True)
st.sidebar.title("MathFeature Package")
st.sidebar.markdown("Author: Robson Parmezan Bonidia")

#############################################################################

main = MultiPage()

pages = {'Classical Chaos Game Representation': ChaosClassicalWeb,
         'Frequency Chaos Game Representation': ChaosFreqWeb,
         'Chaos Game Signal (with Fourier)': ChaosSignalWeb,
         'Binary': MappingDNAWeb,
         'Z-curve': MappingDNAWeb,
         'Real': MappingDNAWeb,
         'Integer': MappingDNAWeb,
         'EIIP': MappingDNAWeb,
         'Complex Number': MappingDNAWeb,
         'Atomic Number': MappingDNAWeb,
         'Shannon': EntropyClassWeb,
         'Tsallis': TsallisEntropyWeb,
         'Binary + Fourier': FourierDNAWeb,
         'Z-curve + Fourier': FourierDNAWeb,
         'Real + Fourier': FourierDNAWeb,
         'Integer + Fourier': FourierDNAWeb,
         'EIIP + Fourier': FourierDNAWeb,
         'Complex Number + Fourier': FourierDNAWeb,
         'Atomic Number + Fourier': FourierDNAWeb,
         'Accumulated nucleotide frequency': ANFDWeb,
         'Accumulated nucleotide frequency + Fourier': ANFDFourierWeb,
         'Complex Networks (with threshold)': ComplexNetworksClassWeb,
         'Complex Networks (without threshold)': ComplexNetworksClassV2Web,
         'Basic k-mer (DNA/RNA)': KmerDNAWeb,
         'Customized k-mer (DNA/RNA)': CKmerDNAWeb,
         'Xmer k-Spaced Ymer composition frequency': KgapWeb,
         'Fickett score': FickettScoreWeb,
         'ORF Features or Coding Features': CodingWeb,
         # 'PseKNC': PseKNCWeb,
         'AAindex Table': AAIndexWeb,
         'Nucleic acid composition': NACWeb,
         'Dinucleotide composition': DNCWeb,
         'Trinucleotide composition': TNCWeb,
         'Amino Acid composition': AACWeb,
         'Dipeptide composition': DPCWeb,
         'Tripeptide composition': TPCWeb,
         'Basic k-mer (Protein)': KmerProteinWeb,
         'Customized k-mer (Protein)': CKmerProteinWeb,
         'Integer (Protein)': IntegerProteinWeb,
         'EIIP (Protein)': EIIPProteinWeb,
         'Accumulated amino acid frequency (Protein)': ANFProteinWeb,
         'Kmer Frequency Mapping (Protein)': KmerMapProteinWeb,
         'Integer + Fourier (Protein)': IntegerProteinFourierWeb,
         'EIIP + Fourier (Protein)': EIIPProteinFourierWeb,
         'Accumulated amino acid frequency + Fourier (Protein)': ANFProteinFourierWeb,
         'Kmer Frequency Mapping + Fourier (Protein)': KmerMapProteinFourierWeb,
         'Preprocessing (DNA/RNA)': PreprocessingWeb,
         'Sampling': PreSamplingWeb,
         'Sequences and Bases/Nucleotide Count': PreCountWeb,
         'To remove repeated sequences in a file': PreRedundWeb,
         'Concatenate datasets/descriptors': PreConcatWeb
         }


sub_descr = ''
try:
    with st.sidebar:
        group = st.selectbox('Descriptor Group', ['', 'Preprocessing', 'Mathematical', 'Conventional'])

        if group == 'Preprocessing':

            sub_descr = st.selectbox('Techniques', ['Concatenate datasets/descriptors',
                                                    'Preprocessing (DNA/RNA)',
                                                    'Sampling',
                                                    'Sequences and Bases/Nucleotide Count',
                                                    'To remove repeated sequences in a file'])

        elif group == 'Mathematical':
            descr = st.selectbox('Mathematical Group', ['Numerical Mapping',
                                                        'Fourier Transform',
                                                        'Chaos Game',
                                                        'Entropy',
                                                        'Graphs'])

            if descr == 'Numerical Mapping':
                descr_two = st.selectbox('Sequence', ['DNA/RNA', 'Protein'])

                if descr_two == 'DNA/RNA':
                    sub_descr = st.selectbox('Descriptor', ['Binary', 'Z-curve', 'Real',
                                                            'Integer', 'EIIP', 'Complex Number',
                                                            'Atomic Number',
                                                            'Accumulated nucleotide frequency'])
                else:
                    sub_descr = st.selectbox('Descriptor', ['Integer (Protein)',
                                                            'EIIP (Protein)',
                                                            'Accumulated amino acid frequency (Protein)',
                                                            'Kmer Frequency Mapping (Protein)'])

            elif descr == 'Fourier Transform':
                descr_two = st.selectbox('Sequence', ['DNA/RNA', 'Protein'])

                if descr_two == 'DNA/RNA':
                    sub_descr = st.selectbox('Descriptor', ['Binary + Fourier',
                                                            'Z-curve + Fourier',
                                                            'Real + Fourier',
                                                            'Integer + Fourier',
                                                            'EIIP + Fourier',
                                                            'Complex Number + Fourier',
                                                            'Atomic Number + Fourier',
                                                            'Accumulated nucleotide frequency + Fourier'])
                else:
                    sub_descr = st.selectbox('Descriptor', ['Integer + Fourier (Protein)',
                                                            'EIIP + Fourier (Protein)',
                                                            'Accumulated amino acid frequency + Fourier (Protein)',
                                                            'Kmer Frequency Mapping + Fourier (Protein)'])

            elif descr == 'Chaos Game':
                sub_descr = st.selectbox('Descriptor', ['Classical Chaos Game Representation',
                                                       'Chaos Game Signal (with Fourier)',
                                                       'Frequency Chaos Game Representation'])

            elif descr == 'Entropy':
                sub_descr = st.selectbox('Descriptor', ['Shannon', 'Tsallis'])

            elif descr == 'Graphs':
                sub_descr = st.selectbox('Descriptor', ['Complex Networks (with threshold)',
                                                        'Complex Networks (without threshold)'])

        elif group == 'Conventional':

            descr_two = st.selectbox('Sequence', ['DNA/RNA', 'Protein'])

            if descr_two == 'DNA/RNA':
                sub_descr = st.selectbox('Conventional Descriptors', ['Basic k-mer (DNA/RNA)',
                                                                      'Customized k-mer (DNA/RNA)',
                                                                      'Nucleic acid composition',
                                                                      'Dinucleotide composition',
                                                                      'Trinucleotide composition',
                                                                      # 'PseKNC',
                                                                      'Xmer k-Spaced Ymer composition frequency',
                                                                      'ORF Features or Coding Features',
                                                                      'Fickett score'])
            else:
                sub_descr = st.selectbox('Conventional Descriptors', ['Basic k-mer (Protein)',
                                                                      'Customized k-mer (Protein)',
                                                                      'Amino Acid composition',
                                                                      'Dipeptide composition',
                                                                      'Tripeptide composition',
                                                                      'Xmer k-Spaced Ymer composition frequency',
                                                                      'AAindex Table'])

    # submit = st.button(label='Open')
except:
    st.warning("Please fill out so required fields")


if __name__ == '__main__':
    try:
        start_time = time.time()
        main.add_page(group, pages[sub_descr].app)
        p = multiprocessing.Process(target=main.run())
        p.start()

        # main.add_page(group, pages[sub_descr].app)
        # main.run()
        # print('Computation time %s senconds' % (time.time() - start_time))
    except:
        st.warning("Please fill out so required fields")
        st.success('Author: Robson Parmezan Bonidia')
        st.error('Report any problem to our repository!')
        doc = 'https://bonidia.github.io/MathFeature/'
        link_button('See our Documentation!', doc)
        url = 'https://github.com/Bonidia/MathFeature'
        link_button('Visit our Repository!', url)
        cs = 'https://github.com/Bonidia/MathFeature/tree/master/Case%20Studies'
        link_button('See Input Files - Case Studies!', cs)
        # https://github.com/Bonidia/MathFeature/issues

#############################################################################
