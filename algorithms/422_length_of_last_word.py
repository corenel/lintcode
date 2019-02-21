"""
Length of Last Word
-------------------

Given a string s consists of upper/lower-case alphabets and empty space
characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note:
    A word is defined as a character sequence consists of non-space
    characters only.

Example:
    - Input: "Hello World"
    - Output: 5

Reference:
    - https://algorithm.yuanbin.me/zh-hans/string/length_of_last_word.html
    - https://leetcode.com/problems/length-of-last-word/
    - https://www.lintcode.com/problem/length-of-last-word/
"""

import unittest


def length_of_last_word(s):
    """
    Returns the length of last word in the given string

    :param s: given string
    :type s: str
    :return: the length of last word
    :rtype: int
    """
    return len(s.strip().split(' ')[-1])


class TestLengthOfLastWord(unittest.TestCase):
    def test_length_of_last_word(self):
        self.assertEqual(5, length_of_last_word('Hello World'))


if __name__ == '__main__':
    unittest.main()
