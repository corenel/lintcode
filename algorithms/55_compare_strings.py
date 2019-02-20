"""
Compare Strings
---

Compare two strings A and B, determine whether A contains all of the
characters in B.

Notice
- The characters in string A and B are all Upper Case letters.
- The characters of B in A are not necessary continuous or ordered.

Example:
- For A = "ABCD", B = "ACD", return true.
- For A = "ABCD", B = "AABC", return false.
"""

import unittest
from collections import defaultdict


def compare_strings(A, B):
    """
    Compare two strings A and B, determine whether A contains all of
    the characters in B.

    :param A: a string includes Upper Case letters
    :type A: str
    :param B: a string includes Upper Case letters
    :type B: str
    :return:
    :rtype: whether or not string A contains all of the characters in B
    """
    char_dict = defaultdict(int)
    for char in A:
        char_dict[char] += 1
    for char in B:
        if char not in char_dict:
            return False
        char_dict[char] -= 1
        if char_dict[char] < 0:
            return False
    return True


class TestCompareStrings(unittest.TestCase):
    def test_compare_strings(self):
        self.assertTrue(compare_strings('ABCD', 'ACD'))
        self.assertFalse(compare_strings('ABCD', 'AABC'))


if __name__ == '__main__':
    unittest.main()
