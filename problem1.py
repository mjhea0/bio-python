########### ---------- DIRECTIONS --------- ##########

# Recursively find all FASTQ files in a directory and 
# report each file name and the percent of sequences 
# in that file that are greater than 30 nt long.

import os, fnmatch
from Bio import SeqIO

# find all files, output names
def findFastqFiles(directory, pattern):
    """Walks the directory structure, appending filenames to an array"""
    filenames = []
    for root, dirs, files in os.walk(directory):
        for basename in files:
            if fnmatch.fnmatch(basename, pattern):
                filename = os.path.join(root, basename)
                filenames.append(filename)
    return filenames

# parse sequences, output percent
def parseFastqSeq(array):
    all_sequences   = []
    large_sequences = []
    for filename in array:
        for sequence in SeqIO.parse(open(filename, "r"), "fastq"):
            if len(sequence.seq) > 30:
                large_sequences.append(sequence)
            all_sequences.append(sequence)
    percent = len(large_sequences) / float(len(all_sequences))
    return percent



#### run code ####

print findFastqFiles('./sample_files/fastq', '*.fastq')
filenames = findFastqFiles('./sample_files/fastq', '*.fastq')
print parseFastqSeq(filenames)
