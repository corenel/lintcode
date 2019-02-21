"""
Compare Strings
---------------

Compare two strings A and B, determine whether A contains all of the
characters in B.

Notice:
    - The characters in string A and B are all Upper Case letters.
    - The characters of B in A are not necessary continuous or ordered.

Example:
    - For A = "ABCD", B = "ACD", return true.
    - For A = "ABCD", B = "AABC", return false.

Reference:
    - https://algorithm.yuanbin.me/zh-hans/string/compare_strings.html
    - http://www.lintcode.com/en/problem/compare-strings/
"""

import unittest
from collections import defaultdict


def compare_strings(s, t):
    """
    Compare two strings A and B, determine whether A contains all of
    the characters in B.

    :param s: a string includes Upper Case letters
    :type s: str
    :param t: a string includes Upper Case letters
    :type t: str
    :return: whether or not string A contains all of the characters in B
    :rtype: bool
    """
    char_dict = defaultdict(int)
    for char in s:
        char_dict[char] += 1
    for char in t:
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
