## Coding tasks

### Write a program to

1. Recursively find all FASTQ files in a directory and report each file name and the percent of sequences in that file that are greater than 30 nt long.

2. Given a FASTA file with DNA sequences, find 10 most frequent sequences and return the sequence and their counts in the file.

3. Given coordinates and a chromosome, write a program for looking up it's annotation. Keep in mind you'll be doing this annotation millions of times.
  - Input: 
    - Tab-delimited file: Chr<tab>Position
	- GTF formatted file with genome annotations.
  - Output: 
	- Annotated file of gene name that input position overlaps.
  > Hint: Most of these reads come from a small portion of the genome. Try to use this information to improve performance, if possible.

### NOTE:
- Sample input files have been provided for each task.
- Please make sure each task can run on the command line.
- In the spirit of assessing your programming abilities, please avoid using 3rd-party tools to solve these problems (parsers and formatters excluded).
