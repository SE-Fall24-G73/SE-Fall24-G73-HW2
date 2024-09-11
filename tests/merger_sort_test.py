import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(_file_), '..')))

from hw2_debugging import merge_sort

def testcase_init_sortedArr():
    """
    Testcase to check if the function can handle an already sorted array.
    """
    arr = [1, 2, 3, 4, 5]
    assert merge_sort(arr) == [1, 2, 3, 4, 5], "Testcase 1 Passed"


def testcase_init_reverse_sortedArr():
    """
    Testcase to check if the function can handle a reverse sorted array.
    """
    arr = [5, 4, 3, 2, 1]
    assert merge_sort(arr) == [1, 2, 3, 4, 5], "Testcase 2 Passed"


def testcase_init_randomArr():
    """
    Testcase to check if the function can handle a random array.
    """
    arr = [3, 1, 5, 2, 4]
    assert merge_sort(arr) == [1, 2, 3, 4, 5], "Testcase 3 Passed"