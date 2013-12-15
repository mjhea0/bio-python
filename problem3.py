########### ---------- DIRECTIONS --------- ##########

# Given coordinates and a chromosome, write a program 
# for looking up it's annotation.  Keep in mind you'll 
# be doing this annotation millions of times.
# - Input: 
# 	- Tab-delimited file: Chr<tab>Position
# 	- GTF formatted file with genome annotations.
# - Output: 
# 	- Annotated file of gene name that input position overlaps.
# - Hint: Most of these reads come from a small portion 
# of the genome. Try to use this information to improve 
# performance, if possible.


########### ---------- THOUGHTS --------- ##########

# Range Overlap. Interval Tree!
# I imagine the TSV file will have millions of rows, 
# thus I cannot read all of the rows into memory
# at once


########### ---------- STEPS --------- ##########
# Read in TSV/tab, parse, break into several files
# Compare chromosome ranges with GTF file
# Find overlaps, create interval tree
# Ouput results as new file

# break into files with 100,000 records each
from Bio import SeqIO

def parseTSV(filename):
	sequence = SeqIO.parse(open(filename),"tab")
	for i, seq in enumerate(seq_itr(sequence, 100000)) :
    	new_filename = "bucket_%i.tab" % (i+1)
    	dump = open(new_filename, "w")
    	dump.close()
    	# new files
    	print new_filename

# from problem1 - read in files recursively
filenames = []
for filename in findFastqFiles('tab-directory', '*.tab'):
    filenames.append(filename)

# parse files into sequences
def parseFastqSeq(array):
    all_sequences = []
    for filename in array:
        for sequence in SeqIO.parse(open(filename, "r"), "fasta"):
            all_sequences.append(sequence)
    return all_sequences

parseFastqSeq(filenames)


# find overlaps, create interval tree
import csv
from bx.intervals.intersection import IntervalTree
 
def rangeOverlap(fileName, delim):
    overlap = dict()
    # parse the annotations file, build the interval trees
    with open(fileName, 'r') as annotationsFile:
        reader = csv.reader(annotationsFile, delimiter=delim)
        for row in reader:
            seqid = row[0]
            # find start, end positions
            start = int(row[3])
            end = int(row[4])
                tree = None
                # one tree for each chromosome
                if seqid in overlap:
                    tree = overlap[seqid]
                else:
                    # new chromosome = new tree
                    tree = IntervalTree()
                    overlap[seqid] = tree
                # index
                tree.add(start, end, tuple(row)) 
    return overlap

overlaps = rangeOverlap('test.gtf', '\t')

# pass in all sequences (all_sequences) to find annotations overlapping a specific interval (INCOMPLETE)
# all_sequences is an array, iterate through array, passing this, as well as the intervals into the function (again, INCOMPLETE)
annotations = overlaps[specific_sequence].find(start, end)
