#!/usr/bin/env python
# -*- coding: utf-8 -*-


import argparse
import numpy as np
from Bio import SeqIO
from scipy.fftpack import fft
import warnings
import statistics
import os
import io
from datetime import timedelta, datetime
warnings.filterwarnings('ignore')


#############################################################################
#############################################################################

def sequence_length(finput):
    length = 0
    for seq_record in SeqIO.parse(io.StringIO(finput), "fasta"):
        seq = seq_record.seq
        if len(seq) > length:
            length = len(seq)
    return length


def file_record(foutput, name_seq, mapping, label_dataset):
    dataset = open(foutput, 'a')
    dataset.write('%s,' % (str(name_seq)))
    for map in mapping:
        dataset.write('%s,' % map)
        # dataset.write('{0:.4f},'.format(metric))
    dataset.write(label_dataset)
    dataset.write('\n')
    # print('Recorded Sequence: %s' % (name_seq))
    return


def chunksTwo(seq, win):
    seqlen = len(seq)
    for i in range(seqlen):
        j = seqlen if i+win>seqlen else i+win
        yield seq[i:j]
        if j==seqlen: break
    return


def accumulated_amino_frequency(finput, label_dataset, padd):

    var = (datetime.now() + timedelta(hours=9)).strftime('%H%M%S')
    foutput = 'tmp/file-' + var + '.csv'
    if os.path.exists(foutput):
        os.remove(foutput)

    max_length = sequence_length(finput)
    for seq_record in SeqIO.parse(io.StringIO(finput), 'fasta'):
        seq = seq_record.seq
        seq = seq.upper()
        name_seq = seq_record.name
        mapping = []
        protein = {'A': 0, 'C': 0, 'D': 0, 'E': 0,
                   'F': 0, 'G': 0, 'H': 0, 'I': 0,
                   'K': 0, 'L': 0, 'M': 0, 'N': 0,
                   'P': 0, 'Q': 0, 'R': 0, 'S': 0,
                   'T': 0, 'V': 0, 'W': 0, 'Y': 0}
        for i in range(len(seq)):
            if seq[i] in protein:
                protein[seq[i]] += 1
                mapping.append(protein[seq[i]] / (i + 1))
        if padd == 'Yes':
            padding = (max_length - len(mapping))
            mapping = np.pad(mapping, (0, padding), 'constant')
        file_record(foutput, name_seq, mapping, label_dataset)
    return foutput


def kmer_frequency_protein(finput, label_dataset, padd, k):

    var = (datetime.now() + timedelta(hours=9)).strftime('%H%M%S')
    foutput = 'tmp/file-' + var + '.csv'
    if os.path.exists(foutput):
        os.remove(foutput)

    max_length = sequence_length(finput)
    for seq_record in SeqIO.parse(io.StringIO(finput), 'fasta'):
        seq = seq_record.seq
        seq = seq.upper()
        name_seq = seq_record.name
        mapping = []
        kmer = {}
        totalWindows = (len(seq) - k) + 1  # (L - k + 1)
        for subseq in chunksTwo(seq, k):
            # print(subseq)
            if subseq in kmer:
                kmer[subseq] = kmer[subseq] + 1
            else:
                kmer[subseq] = 1
        for subseq in chunksTwo(seq, k):
            # print(kmer[subseq])
            # print(kmer[subseq]/totalWindows)
            mapping.append(kmer[subseq] / totalWindows)
        if padd == 'Yes':
            padding = ((max_length - k + 1) - len(mapping))
            mapping = np.pad(mapping, (0, padding), 'constant')
        file_record(foutput, name_seq, mapping, label_dataset)
    return foutput


def integer_mapping_protein(finput, label_dataset, padd):

    var = (datetime.now() + timedelta(hours=9)).strftime('%H%M%S')
    foutput = 'tmp/file-' + var + '.csv'
    if os.path.exists(foutput):
        os.remove(foutput)

    max_length = sequence_length(finput)
    for seq_record in SeqIO.parse(io.StringIO(finput), 'fasta'):
        seq = seq_record.seq
        seq = seq.upper()
        name_seq = seq_record.name
        mapping = []
        protein = {'A': 1, 'C': 5, 'D': 4, 'E': 7,
                   'F': 14, 'G': 8, 'H': 9, 'I': 10,
                   'K': 12, 'L': 11, 'M': 13, 'N': 3,
                   'P': 15, 'Q': 6, 'R': 2, 'S': 16,
                   'T': 17, 'V': 20, 'W': 18, 'Y': 19}
        for i in range(len(seq)):
            if seq[i] in protein:
                mapping.append(protein[seq[i]])
        if padd == 'Yes':
            padding = (max_length - len(mapping))
            mapping = np.pad(mapping, (0, padding), 'constant')
        file_record(foutput, name_seq, mapping, label_dataset)
    return foutput


def eiip_mapping_protein(finput, label_dataset, padd):

    var = (datetime.now() + timedelta(hours=9)).strftime('%H%M%S')
    foutput = 'tmp/file-' + var + '.csv'
    if os.path.exists(foutput):
        os.remove(foutput)

    max_length = sequence_length(finput)
    for seq_record in SeqIO.parse(io.StringIO(finput), 'fasta'):
        seq = seq_record.seq
        seq = seq.upper()
        name_seq = seq_record.name
        mapping = []
        protein = {'A': 0.3710, 'C': 0.08292, 'D': 0.12630, 'E': 0.00580,
                   'F': 0.09460, 'G': 0.0049, 'H': 0.02415, 'I': 0.0000,
                   'K': 0.37100, 'L': 0.0000, 'M': 0.08226, 'N': 0.00359,
                   'P': 0.01979, 'Q': 0.07606, 'R': 0.95930, 'S': 0.08292,
                   'T': 0.09408, 'V': 0.00569, 'W': 0.05481, 'Y': 0.05159}
        for i in range(len(seq)):
            if seq[i] in protein:
                mapping.append(protein[seq[i]])
        if padd == 'Yes':
            padding = (max_length - len(mapping))
            mapping = np.pad(mapping, (0, padding), 'constant')
        file_record(foutput, name_seq, mapping, label_dataset)
    return foutput


#############################################################################
#############################################################################


def header_fourier(foutput):
    dataset = open(foutput, 'a')
    dataset.write('nameseq,average,median,maximum,minimum,peak,'
                  + 'none_levated_peak,sample_standard_deviation,population_standard_deviation,'
                  + 'percentile15,percentile25,percentile50,percentile75,amplitude,'
                  + 'variance,interquartile_range,semi_interquartile_range,'
                  + 'coefficient_of_variation,skewness,kurtosis,label')
    dataset.write('\n')
    return


def file_record_fourier(foutput, features, name_seq, label_dataset):
    dataset = open(foutput, 'a')
    dataset.write('%s,' % (str(name_seq)))
    for metric in features:
        dataset.write('%s,' % metric)
        # dataset.write('{0:.4f},'.format(metric))
    dataset.write(label_dataset)
    dataset.write('\n')
    # print('Recorded Sequence: %s' % name_seq)
    return


def feature_extraction(features, spectrum, spectrumTwo):
    average = sum(spectrum)/len(spectrum)
    features.append(average)
    ###################################
    median = np.median(spectrum)
    features.append(median)
    ###################################
    maximum = np.max(spectrum)
    features.append(maximum)
    ###################################
    minimum = np.min(spectrum)
    features.append(minimum)
    ###################################
    peak = (len(spectrum)/3)/average
    features.append(peak)
    ###################################
    peak_two = (len(spectrumTwo)/3)/(np.mean(spectrumTwo))
    features.append(peak_two)
    ###################################
    standard_deviation = np.std(spectrum)  # standard deviation
    features.append(standard_deviation)
    ###################################
    standard_deviation_pop = statistics.stdev(spectrum)  # population sample standard deviation
    features.append(standard_deviation_pop)
    ###################################
    percentile15 = np.percentile(spectrum, 15)
    features.append(percentile15)
    ###################################
    percentile25 = np.percentile(spectrum, 25)
    features.append(percentile25)
    ###################################
    percentile50 = np.percentile(spectrum, 50)
    features.append(percentile50)
    ###################################
    percentile75 = np.percentile(spectrum, 75)
    features.append(percentile75)
    ###################################
    amplitude = maximum - minimum
    features.append(amplitude)
    ###################################
    # mode = statistics.mode(spectrum)
    ###################################
    variance = statistics.variance(spectrum)
    features.append(variance)
    ###################################
    interquartile_range = np.percentile(spectrum, 75) - np.percentile(spectrum, 25)
    features.append(interquartile_range)
    ###################################
    semi_interquartile_range = (np.percentile(spectrum, 75) - np.percentile(spectrum, 25))/2 
    features.append(semi_interquartile_range)
    ###################################
    coefficient_of_variation = standard_deviation/average
    features.append(coefficient_of_variation)
    ###################################
    skewness = (3 * (average - median))/standard_deviation
    features.append(skewness)   
    ###################################
    kurtosis = (np.percentile(spectrum, 75) - np.percentile(spectrum, 25)) / (2 * (np.percentile(spectrum, 90) - np.percentile(spectrum, 10))) 
    features.append(kurtosis)
    ###################################
    return


def accumulated_amino_frequency_fourier(finput, label_dataset):

    var = (datetime.now() + timedelta(hours=9)).strftime('%H%M%S')
    foutput = 'tmp/file-' + var + '.csv'
    if os.path.exists(foutput):
        os.remove(foutput)

    header_fourier(foutput)
    for seq_record in SeqIO.parse(io.StringIO(finput), "fasta"):
        seq = seq_record.seq
        seq = seq.upper()
        name_seq = seq_record.name
        features = []
        spectrum = []
        spectrumTwo = []
        mapping = []
        protein = {'A': 0, 'C': 0, 'D': 0, 'E': 0,
                   'F': 0, 'G': 0, 'H': 0, 'I': 0,
                   'K': 0, 'L': 0, 'M': 0, 'N': 0,
                   'P': 0, 'Q': 0, 'R': 0, 'S': 0,
                   'T': 0, 'V': 0, 'W': 0, 'Y': 0}
        for i in range(len(seq)):
            if seq[i] in protein:
                protein[seq[i]] += 1
                mapping.append(protein[seq[i]] / (i + 1))
        Fmap = fft(mapping)
        for i in range(len(mapping)):
            specTotal = (abs(Fmap[i]) ** 2)
            specTwo = (abs(Fmap[i]))
            spectrum.append(specTotal)
            spectrumTwo.append(specTwo)
        feature_extraction(features, spectrum, spectrumTwo)
        file_record_fourier(foutput, features, name_seq, label_dataset)
    return foutput


def kmer_frequency_protein_fourier(finput, label_dataset, k):

    var = (datetime.now() + timedelta(hours=9)).strftime('%H%M%S')
    foutput = 'tmp/file-' + var + '.csv'
    if os.path.exists(foutput):
        os.remove(foutput)

    header_fourier(foutput)
    for seq_record in SeqIO.parse(io.StringIO(finput), "fasta"):
        seq = seq_record.seq
        seq = seq.upper()
        name_seq = seq_record.name
        features = []
        spectrum = []
        spectrumTwo = []
        mapping = []
        kmer = {}
        totalWindows = (len(seq) - k) + 1  # (L - k + 1)
        for subseq in chunksTwo(seq, k):
            # print(subseq)
            if subseq in kmer:
                kmer[subseq] = kmer[subseq] + 1
            else:
                kmer[subseq] = 1
        for subseq in chunksTwo(seq, k):
            # print(kmer[subseq])
            # print(kmer[subseq]/totalWindows)
            mapping.append(kmer[subseq] / totalWindows)
        Fmap = fft(mapping)
        for i in range(len(mapping)):
            specTotal = (abs(Fmap[i]) ** 2)
            specTwo = (abs(Fmap[i]))
            spectrum.append(specTotal)
            spectrumTwo.append(specTwo)
        feature_extraction(features, spectrum, spectrumTwo)
        file_record_fourier(foutput, features, name_seq, label_dataset)
    return foutput


def integer_mapping_protein_fourier(finput, label_dataset):

    var = (datetime.now() + timedelta(hours=9)).strftime('%H%M%S')
    foutput = 'tmp/file-' + var + '.csv'
    if os.path.exists(foutput):
        os.remove(foutput)

    header_fourier(foutput)
    for seq_record in SeqIO.parse(io.StringIO(finput), "fasta"):
        seq = seq_record.seq
        seq = seq.upper()
        name_seq = seq_record.name
        features = []
        spectrum = []
        spectrumTwo = []
        mapping = []
        protein = {'A': 1, 'C': 5, 'D': 4, 'E': 7,
                   'F': 14, 'G': 8, 'H': 9, 'I': 10,
                   'K': 12, 'L': 11, 'M': 13, 'N': 3,
                   'P': 15, 'Q': 6, 'R': 2, 'S': 16,
                   'T': 17, 'V': 20, 'W': 18, 'Y': 19}
        for i in range(len(seq)):
            if seq[i] in protein:
                mapping.append(protein[seq[i]])
        Fmap = fft(mapping)
        for i in range(len(mapping)):
            specTotal = (abs(Fmap[i]) ** 2)
            specTwo = (abs(Fmap[i]))
            spectrum.append(specTotal)
            spectrumTwo.append(specTwo)
        feature_extraction(features, spectrum, spectrumTwo)
        file_record_fourier(foutput, features, name_seq, label_dataset)
    return foutput


def eiip_mapping_protein_fourier(finput, label_dataset):

    var = (datetime.now() + timedelta(hours=9)).strftime('%H%M%S')
    foutput = 'tmp/file-' + var + '.csv'
    if os.path.exists(foutput):
        os.remove(foutput)

    header_fourier(foutput)
    for seq_record in SeqIO.parse(io.StringIO(finput), "fasta"):
        seq = seq_record.seq
        seq = seq.upper()
        name_seq = seq_record.name
        features = []
        spectrum = []
        spectrumTwo = []
        mapping = []
        protein = {'A': 0.3710, 'C': 0.08292, 'D': 0.12630, 'E': 0.00580,
                   'F': 0.09460, 'G': 0.0049, 'H': 0.02415, 'I': 0.0000,
                   'K': 0.37100, 'L': 0.0000, 'M': 0.08226, 'N': 0.00359,
                   'P': 0.01979, 'Q': 0.07606, 'R': 0.95930, 'S': 0.08292,
                   'T': 0.09408, 'V': 0.00569, 'W': 0.05481, 'Y': 0.05159}
        for i in range(len(seq)):
            if seq[i] in protein:
                mapping.append(protein[seq[i]])
        Fmap = fft(mapping)
        for i in range(len(mapping)):
            specTotal = (abs(Fmap[i]) ** 2)
            specTwo = (abs(Fmap[i]))
            spectrum.append(specTotal)
            spectrumTwo.append(specTwo)
        feature_extraction(features, spectrum, spectrumTwo)
        file_record_fourier(foutput, features, name_seq, label_dataset)
    return foutput
#############################################################################
#############################################################################
