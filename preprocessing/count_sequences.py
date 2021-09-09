#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import warnings
from Bio import SeqIO
warnings.filterwarnings("ignore")


def count_sequences(finput):
    i = 0
    for seq_record in SeqIO.parse(io.StringIO(finput), "fasta"):
        name_seq = seq_record.name
        i += 1
    return i

    # print ("Number of sequences: %s" % (i))
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