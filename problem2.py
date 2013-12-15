########### ---------- DIRECTIONS --------- ##########

# Given a FASTA file with DNA sequences, find 10 most 
# frequent sequences and return the sequence and their 
# counts in the file.


from Bio import SeqIO
from collections import Counter

def freqFastqSeq(filename):
    for sequence in SeqIO.parse(filename, "fastq"):
        seq = str(sequence.seq)
        for i in range(len(seq)):
            cnt = Counter(seq[i:i+30])
        for subseq, count in cnt.items():
           print subseq + '\t' + str(count)

#### run code ####

fastaFile = "test.fastq"
freqFastqSeq(fastaFile)
