"""
Valid Palindrome
----------------

Given a string, determine if it is a palindrome, considering only alphanumeric
characters and ignoring cases.

Note:
    For the purpose of this problem, we define empty string as
    valid palindrome.

Example 1:
    - Input: "A man, a plan, a canal: Panama"
    - Output: true

Example 2:
    - Input: "race a car"
    - Output: false

Reference:
    - https://algorithm.yuanbin.me/zh-hans/string/valid_palindrome.html
    - https://leetcode.com/problems/valid-palindrome/
    - https://www.lintcode.com/problem/valid-palindrome/
"""

import unittest


def is_palindrome(s):
    """
    Determine whether or not given string is valid palindrome

    :param s: given string
    :type s: str
    :return: whether or not given string is valid palindrome
    :rtype: bool
    """
    # basic case
    if s == '':
        return True

    # two pointers
    # one from left, one from right
    i = 0
    j = len(s) - 1
    while i < j:
        # find left alphanumeric character
        if not s[i].isalnum():
            i += 1
            continue
        # find right alphanumeric character
        elif not s[j].isalnum():
            j -= 1
            continue
        # case insensitive compare
        if s[i].lower() != s[j].lower():
            return False
        i += 1
        j -= 1

    return True


class TestValidPalindrome(unittest.TestCase):
    def test_valid_palindrome(self):
        self.assertTrue(is_palindrome(''))
        self.assertFalse(is_palindrome('0P'))
        self.assertTrue(is_palindrome('a'))
        self.assertTrue(is_palindrome('A man, a plan, a canal: Panama'))
        self.assertFalse(is_palindrome('race a car'))


if __name__ == '__main__':
    unittest.main()
