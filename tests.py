""" Tests the elon_sort algorithm """
import unittest
from elon_sort import elon_sort

class TestReturnType(unittest.TestCase):
    """ I'm not putting a docstring here"""

    test_data = [1, 2, 2, 2, 4, 5, -1, -2]

    def test_return_type_is_list(self):
        """ Make sure the return type is a list"""
        self.assertIsInstance(elon_sort(self.test_data), list)

class TestSortingAlgorithm(unittest.TestCase):
    """I'm also not putting a docstring here"""
    test_data = [1, 2, 2, 2, 4, 5, -1, -2]

    def test_sorted_in_ascending_order(self):
        """ Test that we sorted in ascending order"""
        sorted_data = elon_sort(self.test_data)
        self.assertLess(sorted_data[0], sorted_data[-1])
        # a very useful test case
        self.assertGreater(sorted_data[-1], sorted_data[0])

class TestExceptions(unittest.TestCase):
    """Test that exceptions get raised"""

    def test_exception_is_raised_for_str_input(self):
        """ Raise an exception if the input is a string """

        test_data = "not an array"
        self.assertRaises(ValueError, elon_sort, test_data)

    def test_exception_is_raised_for_dict_input(self):
        """ Raise an exception if the input is a string """

        test_data = {"also": "not an array"}
        self.assertRaises(ValueError, elon_sort, test_data)


if __name__ == "__main__":
    unittest.main()
