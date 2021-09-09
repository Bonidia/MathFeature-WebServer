import argparse
import random
import warnings
import os
import io
from datetime import timedelta, datetime
from Bio import SeqIO
warnings.filterwarnings("ignore")


def sampling(finput, parameter):

    var = (datetime.now() + timedelta(hours=9)).strftime('%H%M%S')
    foutput = 'tmp/file-' + var + '.fasta'
    if os.path.exists(foutput):
        os.remove(foutput)

    arq = open(foutput, 'a')
    nameseq = {}
    for seq_record in SeqIO.parse(io.StringIO(finput), "fasta"):
        name = seq_record.name
        seq = seq_record.seq
        nameseq[name] = seq
    for key, value in random.sample(nameseq.items(), parameter):
        arq.write(">" + key)
        arq.write("\n")
        arq.write(str(value))
        arq.write("\n")
    return foutput


#############################################################################    
if __name__ == "__main__":
    print("\n")
    print("###################################################################################")
    print("######################## Feature Extraction: Sampling  ############################")
    print("##############  Arguments: python3.5 -i input -o output -p samples   ##############")
    print("##########               Author: Robson Parmezan Bonidia                ###########")
    print("###################################################################################")
    print("\n")
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', help='Fasta format file, E.g., test.fasta')
    parser.add_argument('-o', '--output', help='Fasta format file, E.g., sampling.fasta')
    parser.add_argument('-p', '--parameter', help='Amount of Samples, e.g., 1000, 2000 ...')
    args = parser.parse_args()
    finput = str(args.input)
    foutput = str(args.output)
    parameter = int(args.parameter)
    sampling(finput,foutput,parameter)
#############################################################################