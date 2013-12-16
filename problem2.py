########### ---------- DIRECTIONS --------- ##########

# Given a FASTA file with DNA sequences, find 10 most 
# frequent sequences and return the sequence and their 
# counts in the file.


from Bio import SeqIO

def freqFastaSeq(file):
    sequences = []
    fasta_sequences = SeqIO.parse(open(file),'fasta')
    for fasta in fasta_sequences:
        sequence = fasta.seq.tostring()
        sequences.append(sequence)
    from collections import Counter
    c = Counter(sequences)
    most_common_seq = c.most_common(10)
    return most_common_seq

#### run code ####

fastaFile = "./sample_files/fasta/sample.fasta"
print freqFastaSeq(fastaFile)




