#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import warnings
import os
import io
from Bio import SeqIO
warnings.filterwarnings("ignore")


def count_sequences(finput):
    i = 0
    length = []
    for seq_record in SeqIO.parse(io.StringIO(finput), "fasta"):
        length.append(len(seq_record.seq))
        i += 1
    return length, i


    # print("Min: %s" % (min(length)))
    # print("Max: %s" % (max(length)))
    # print("Mean: %s" % ((sum(length)/len(length))))
    # print("Sequences: %s" % i)
    # print("Finished")


#############################################################################    
if __name__ == "__main__":
    print("\n")
    print("###################################################################################")
    print("#################### Feature Extraction: Sequences Counting #######################")
    print("########################   Arguments: python3.5 -i input  #########################")
    print("##########               Author: Robson Parmezan Bonidia                ###########")
    print("###################################################################################")
    print("\n")
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', help='Fasta format file, E.g., test.fasta')
    args = parser.parse_args()
    finput = str(args.input)
    count_sequences(finput)
#############################################################################