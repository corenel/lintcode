"""
Longest Palindromic Substring
-----------------------------

Given a string s, find the longest palindromic substring in s.
You may assume that the maximum length of s is 1000.

Example 1:
    - Input: "babad"
    - Output: "bab"
    - Note: "aba" is also a valid answer.

Example 2:
    - Input: "cbbd"
    - Output: "bb"

Reference:
    - https://algorithm.yuanbin.me/zh-hans/string/longest_palindromic_substring.html
    - https://leetcode.com/problems/longest-palindromic-substring/
    - https://www.lintcode.com/problem/longest-palindromic-substring/
"""

import unittest


def longest_palindrome(string):
    """
    Find the longest palindromic substring in given string

    Time complexity: O(n^2)

    :param string: given string
    :type string: str
    :return: longest palindrome
    :rtype: str
    """

    def find_palindrome(s, l, r):
        """
        Find palindrome of given string starting from position l and r

        :param s: given string
        :type s: str
        :param l: left starting position
        :type l: int
        :param r: right starting position
        :type r: int
        :return: found palindrome
        :rtype: str
        """
        while l >= 0 and r <= len(s) - 1 and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l + 1:r]

    # basic case
    if string == '':
        return string

    res = ''
    for i in range(len(string)):
        # find palindrome with even number of characters
        temp = find_palindrome(string, i, i)
        if len(temp) > len(res):
            res = temp
        # find palindrome with odd number of characters
        temp = find_palindrome(string, i, i + 1)
        if len(temp) > len(res):
            res = temp

    return res


class TestLongestPalindromicSubstring(unittest.TestCase):
    def test_longest_palindromic_substring(self):
        self.assertEqual('', longest_palindrome(''))
        self.assertEqual('bab', longest_palindrome('babad'))
        self.assertEqual('bb', longest_palindrome('cbbd'))


if __name__ == '__main__':
    unittest.main()
