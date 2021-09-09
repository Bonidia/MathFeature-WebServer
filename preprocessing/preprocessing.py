#!/usr/bin/env python
# -*- coding: utf-8 -*-

import warnings
import re
import argparse
import os
import io
from datetime import timedelta, datetime
from Bio import SeqIO
warnings.filterwarnings("ignore")


def preprocessing(finput):

    var = (datetime.now() + timedelta(hours=9)).strftime('%H%M%S')
    foutput = 'tmp/file-' + var + '.fasta'
    if os.path.exists(foutput):
        os.remove(foutput)

    alphabet = ("B|D|E|F|H|I|J|K|L|M|N|O|P|Q|R|S|V|W|X|Y|Z")
    file = open(foutput, 'a')
    for seq_record in SeqIO.parse(io.StringIO(finput), "fasta"):
        name_seq = seq_record.name
        seq = seq_record.seq
        if re.search(alphabet, str(seq)) is not None:
            print(name_seq)
            # print("Removed Sequence")
        else:
            file.write(">%s" % (str(name_seq)))
            file.write("\n")
            file.write(str(seq))
            file.write("\n")
            # print(name_seq)
            # print("Included Sequence")
    return foutput


#############################################################################    
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', help='Fasta format file, E.g., dataset.fasta')
    parser.add_argument('-o', '--output', help='Fasta format file, E.g., preprocessing.fasta')
    args = parser.parse_args()
    finput = str(args.input)
    foutput = str(args.output)
    preprocessing(finput,foutput)
#############################################################################]