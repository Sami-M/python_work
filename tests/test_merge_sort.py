"""
Created by Sami on 12/7/2016
"""
import unittest
import random
import copy
from ..alg.sorting.merge_sort import merge_sort

class MergeSortTest(unittest.TestCase):
    def test_if_unsorted_array_becomes_sorted(self):
        array_to_sort = [5, 2, 7, 9, 4, 1, 3]
        merge_sort(array_to_sort)
        self.assertEqual(array_to_sort, [1, 2, 3, 4, 5, 7, 9])
    def test_if_random_array_becomes_sorted(self):
        array_to_sort = random.sample(range(1, 1000), 100)
        array_to_sort_using_python = copy.deepcopy(array_to_sort)
        merge_sort(array_to_sort)
        array_to_sort_using_python.sort()
        self.assertEqual(array_to_sort, array_to_sort_using_python)