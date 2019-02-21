"""
Longest Common Substring
------------------------

Given two strings, find the longest common substring.

Return the length of it.

Note:
    The characters in substring should occur continuously in original string.
    This is different with sub-sequence.

Example 1:
    - Input:  "ABCD" and "CBCE"
    - Output:  2
    - Explanation: Longest common substring is "BC"

Example 2:
    - Input: "ABCD" and "EACB"
    - Output:  1
    - Explanation: Longest common substring is 'A' or 'C' or 'B'

Challenge:
    O(n x m) time and memory.

Reference:
    - https://algorithm.yuanbin.me/zh-hans/string/longest_common_substring.html
    - http://www.lintcode.com/en/problem/longest-common-substring/
"""

import unittest


def longest_common_substring(s, t):
    """
    Find the longest common substring between the given two strings


    :param s: source string
    :type s: str
    :param t: target string
    :type t: str
    :return: the length of the longest common substring
    :rtype: int
    """
    if s == '' or t == '':
        return 0
    f = [[0 for _ in range(len(t) + 1)]
         for _ in range(len(s) + 1)]
    for i in range(len(s)):
        for j in range(len(t)):
            if s[i] == t[j]:
                f[i + 1][j + 1] = f[i][j] + 1
    return max(map(max, f))


class TestLongestCommonSubstring(unittest.TestCase):
    def test_longest_common_substring(self):
        self.assertEqual(2, longest_common_substring('ABCD', 'CBCE'))
        self.assertEqual(1, longest_common_substring('ABCD', 'EACB'))


if __name__ == '__main__':
    unittest.main()
