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
# from bx.intervals.intersection import IntervalTree

def parseTSVforChromes(filename):
    chromosomes = []
    with open(filename,'rb') as tabbed_file:
        tabbed_file = csv.reader(tabbed_file, delimiter='\t')
        for row in tabbed_file:
            chromosomes.append(row)
    return chromosomes

def removeListDups(array):
    outlist = []
    for element in array:
        if element[0] not in outlist:
            outlist.append(element[0])
    return outlist

def parseGTF(filename, array, arrayMinusDups):
    with open(filename,'rb') as tabbed_file:
        tabbed_file = csv.reader(tabbed_file, delimiter='\t')
        for row in tabbed_file:
            for chrom in arrayMinusDups:
                if row[0] == chrom:
                    for cordRow in array:
                        if (row[3] <= cordRow[1] <= row[4]):
                            print row



#### run code ####

filename1 = "./sample_files/annotate/coordinates_to_annotate.txt"
filename2 = "./sample_files/gtf/hg19_annotations.gtf"
array = parseTSVforChromes(filename1)
arrayMinusDups = removeListDups(array)
parseGTF(filename2, array, arrayMinusDups)
