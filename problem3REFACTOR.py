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


# Clarification Questio Basically, I need to find the chromosome in the TSV file as well as the coordinate, then see # if that 
# chromosome is in the GTF file and if so, see if the coordinate falls within the coordinates. If so, the results need to be 
# outputted - is that right?

from Bio import SeqIO
import csv
from collections import OrderedDict
import pprint
from BCBio import GFF



def parseGTF(filename):
    """convert TSV to dict"""
     
    in_file = filename
    in_handle = open(in_file)
    for rec in GFF.parse(in_handle):
        print rec
    in_handle.close()






#### run code ####

# filename1 = "./mock-test3.tsv"
filename2 = "./sample_files/gtf/hg19_annotations.gtf"
# array = parseTSVforChromes(filename1)
# arrayMinusDups = removeListDups(array)
print parseGTF(filename2)
