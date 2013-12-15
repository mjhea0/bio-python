import unittest
from problem1 import *

class Problem1TestCase(unittest.TestCase):
    """Tests for `problem1.py`."""

    def test_find_fastq_files_recursively(self):
        """Should return all files from the sub directories"""
        self.assertEqual(findFastqFiles('./sample_files/fastq', '*.fastq'), ['./sample_files/fastq/read1/Sample_R1.fastq', './sample_files/fastq/read2/Sample_R2.fastq'])

    def parseFastqSeq(self):
        """Should return percentage of sequences > 30 vs all sequences"""
        self.assertEqual(parseFastqSeq(['mock-test1.fastq']), 0.428571428571)

if __name__ == '__main__':
    unittest.main()
