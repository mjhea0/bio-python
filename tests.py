import unittest
from problem1 import *
from problem2 import *
# from problem3 import *

class Problem1TestCase(unittest.TestCase):
    """Tests for `problem1.py`."""

    def test_find_fastq_files_recursively(self):
        """Should return all files from the sub directories"""
        self.assertEqual(findFastqFiles('./sample_files/fastq', '*.fastq'), ['./sample_files/fastq/read1/Sample_R1.fastq', './sample_files/fastq/read2/Sample_R2.fastq'])

    def test_parseFastqSeq(self):
        """Should return percentage of sequences > 30 vs all sequences"""
        self.assertEqual(parseFastqSeq(['mock-test1.fastq']), 0.42857142857142855)

# class Problem2TestCase(unittest.TestCase):
#     """Tests for `problem2.py`."""

#     pass

# class Problem3TestCase(unittest.TestCase):
#     """Tests for `problem3.py`."""

#     pass

if __name__ == '__main__':
    unittest.main()
