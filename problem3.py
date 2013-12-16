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


from Bio import SeqIO
import csv
# from bx.intervals.intersection import IntervalTree

def parseTSV(filename):
    chromosomes = []
    with open(filename,'rb') as tabbed_file:
        tabbed_file = csv.reader(tabbed_file, delimiter='\t')
        for row in tabbed_file:
            chromosomes.append(row[0])
    return chromosomes

def parseGTF(filename, array):
    with open(filename,'rb') as tabbed_file:
        tabbed_file = csv.reader(tabbed_file, delimiter='\t')
        for row in tabbed_file:
            for chrom in array:
                if row[0] == chrom:
                    print row[8]



#### run code ####

filename = "./sample_files/annotate/coordinates_to_annotate.txt"
parseTSV(filename)

filename = "./sample_files/gtf/hg19_annotations.gtf"
array = parseTSV(filename)
parseGTF(filename, array)
