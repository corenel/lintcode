"""
StrStr
------

Implement strStr().

Return the index of the first occurrence of needle in haystack,
or -1 if needle is not part of haystack.

Example 1
    - Input: haystack = "hello", needle = "ll"
    - Output: 2

Example 2:
    - Input: haystack = "aaaaa", needle = "bba"
    - Output: -1

Clarification:
    What should we return when needle is an empty string? This is a great question
    to ask during an interview.

    For the purpose of this problem, we will return 0 when needle is an empty
    string. This is consistent to C's strstr() and Java's indexOf().

Reference:
    - https://algorithm.yuanbin.me/zh-hans/string/strstr.html
    - https://leetcode.com/problems/implement-strstr/
    - https://www.lintcode.com/problem/implement-strstr
    - https://www.geeksforgeeks.org/naive-algorithm-for-pattern-searching/
    - https://www.geeksforgeeks.org/kmp-algorithm-for-pattern-searching/
"""

import unittest


def str_str_naive(haystack, needle):
    """
    Solution for strStr() in naive algorithm

    Worst case complexity: O(m(n-m+1))

    :param haystack: source string (length n) to be searched in
    :type haystack: str
    :param needle: target string (length m) to search
    :type needle: str
    :return: index of occurrence
    :rtype: int
    """
    # basic case
    if len(needle) == 0:
        return 0
    if len(haystack) == 0 or len(haystack) < len(needle):
        return -1

    # double for-loop to slide pattern one by one
    for i in range(len(haystack) - len(needle) + 1):
        # For current index i, check for pattern match
        for j in range(len(needle)):
            if haystack[i + j] != needle[j]:
                break
        else:
            return i

    return -1


def str_str_kmp(haystack, needle):
    """
    Solution for strStr() in KMP (Knuth Morris Pratt) way.

    The KMP matching algorithm uses degenerating property (pattern having
    same sub-patterns appearing more than once in the pattern) of the pattern
    and improves the worst case complexity to O(n). The basic idea behind
    KMP’s algorithm is: whenever we detect a mismatch (after some matches),
    we already know some of the characters in the text of the next window.

    Worst case complexity: O(n)

    :param haystack: source string to be searched in
    :type haystack: str
    :param needle: target string to search
    :type needle: str
    :return: index of occurrence
    :rtype: int
    """
    # basic case
    if len(needle) == 0:
        return 0
    if len(haystack) == 0 or len(haystack) < len(needle):
        return -1

    # preprocess the pattern
    # create lps[] that will hold the longest prefix suffix
    # values for pattern
    lps = [0 for _ in range(len(needle))]
    length = 0
    i = 1
    # the loop calculates lps[i] for i = 1 to M-1
    while i < len(needle):
        if needle[i] == needle[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            # this is tricky. Consider the example.
            # AAACAAAA and i = 7. The idea is similar
            # to search step.
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

    # start searching
    i = j = 0
    # indices = []
    while i < len(haystack):
        if haystack[i] == needle[j]:
            i += 1
            j += 1
        if j == len(needle):
            # indices.append(i)
            # j = lps[j - 1]
            return i - j
        # mismatch after j matches
        elif i < len(haystack) and haystack[i] != needle[j]:
            # do not match lps[0..lps[j-1]] characters,
            # they will match anyway
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return -1


class TestStrStr(unittest.TestCase):
    def test_str_str_naive(self):
        self.assertEqual(2, str_str_naive('hello', 'll'))
        self.assertEqual(-1, str_str_naive('aaaaa', 'bba'))
        self.assertEqual(0, str_str_naive('hello', ''))
        self.assertEqual(-1, str_str_naive('', 'hello'))

    def test_str_str_kmp(self):
        self.assertEqual(2, str_str_kmp('hello', 'll'))
        self.assertEqual(-1, str_str_kmp('aaaaa', 'bba'))
        self.assertEqual(0, str_str_kmp('hello', ''))
        self.assertEqual(-1, str_str_kmp('', 'hello'))


if __name__ == '__main__':
    unittest.main()
