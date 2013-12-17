import unittest
from problem1 import *
from problem2 import *
from problem3 import *

class Problem1TestCase(unittest.TestCase):
    """Tests for `problem1.py`."""

    def test_find_fastq_files_recursively(self):
        """Should return all files from the sub directories"""
        self.assertEqual(findFastqFiles('./sample_files/fastq', '*.fastq'), ['./sample_files/fastq/read1/Sample_R1.fastq', './sample_files/fastq/read2/Sample_R2.fastq'])

    def test_parseFastqSeq(self):
        """Should return percentage of sequences > 30 vs all sequences"""
        self.assertEqual(parseFastqSeq(['mock-test1.fastq']), 0.42857142857142855)

class Problem2TestCase(unittest.TestCase):
    """Tests for `problem2.py`."""

    def test_find_most_common_sequences(self):
    	"""Should return 10 most common sequences"""
    	self.assertEqual(freqFastaSeq('mock-test2.fasta'), [('AAA', 8), ('BBB', 3), ('NNN', 1), ('VVV', 1), ('TRTR', 1), ('123', 1), ('111', 1), ('RTR', 1), ('FFF', 1), ('CCC', 1)])


class Problem3TestCase(unittest.TestCase):
    """Tests for `problem3.py`."""

    def test_parse_TSV(self):
        """Should return an array of [chromosome,position]"""
        self.assertEqual(parseTSVforChromes('mock-test3.tsv'), [['chr12', '20704380'], ['chr12', '20704379'], ['chr21', '9827238'], ['chr5', '71146882'], ['chr8', '38283717'], ['chr12', '20704371'], ['chr12', '20704377'], ['chr21', '9827364'], ['chr4', '184083607'], ['chr11', '85195011'], ['chr11', '85195078'], ['chr12', '20704387'], ['chr21', '9827418'], ['chr12', '20704369'], ['chr12', '20704360'], ['chr2', '133012823']])

if __name__ == '__main__':
    unittest.main()
