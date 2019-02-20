"""
Valid Anagram
-------------

Given two strings s and t, write a function to determine if t is an anagram
of s.

Example 1:

- Input: s = "anagram", t = "nagaram"
- Output: true

Example 2:

- Input: s = "rat", t = "car"
- Output: false

Note:

- Two strings are anagram if they can be the same after change the order of
  characters.
- You may assume the string contains only lowercase alphabets.

Follow up:

    What if the inputs contain unicode characters? How would you adapt your
    solution to such case?

Reference:

- https://algorithm.yuanbin.me/zh-hans/string/two_strings_are_anagrams.html
- https://www.geeksforgeeks.org/check-whether-two-strings-are-anagram-of-each-other/
- https://www.lintcode.com/problem/valid-anagram
"""

import unittest
from collections import Counter


def is_anagram_counter(s, t):
    """
    Determine whether or not teo given strings are anagram by counter

    :param s: source string
    :type s: str
    :param t: target string
    :type t: str
    :return: whether or not teo given strings are anagram
    :rtype: bool
    """
    return len(s) == len(t) and Counter(s) == Counter(t)


def is_anagram_hashmap(s, t):
    """
    Determine whether or not teo given strings are anagram by counting
    characters

    Time Complexity: O(n)

    :param s: source string
    :type s: str
    :param t: target string
    :type t: str
    :return: whether or not teo given strings are anagram
    :rtype: bool
    """
    # basic case
    if len(s) != len(t):
        return False

    # construct counter
    counter = [0 for _ in range(256)]
    for i in range(len(s)):
        counter[ord(s[i])] += 1
        counter[ord(t[i])] -= 1

    # cost more time (maybe ord())
    # if len(s) >= 256:
    #     for i in range(len(counter)):
    #         if counter[i] != 0:
    #             return False
    # else:
    #     for i in range(len(s)):
    #         if counter[ord(s[i])] != 0:
    #             return False

    # compare counter
    for i in range(len(counter)):
        if counter[i] != 0:
            return False

    return True


def is_anagram_sort(s, t):
    """
    Determine whether or not teo given strings are anagram by sorting

    Time Complexity: O(n log n)

    :param s: source string
    :type s: str
    :param t: target string
    :type t: str
    :return: whether or not teo given strings are anagram
    :rtype: bool
    """
    # basic case
    if len(s) != len(t):
        return False

    # sort strings
    s_sorted = sorted(s)
    t_sorted = sorted(t)

    # check equality
    for i in range(len(s_sorted)):
        if s_sorted[i] != t_sorted[i]:
            return False

    return True


class TestValidAnagram(unittest.TestCase):
    def test_valid_anagram_counter(self):
        self.assertTrue(is_anagram_counter('anagram', 'nagaram'))
        self.assertFalse(is_anagram_counter('rat', 'car'))

    def test_valid_anagram_hashmap(self):
        self.assertTrue(is_anagram_hashmap('anagram', 'nagaram'))
        self.assertFalse(is_anagram_hashmap('rat', 'car'))

    def test_valid_anagram_sort(self):
        self.assertTrue(is_anagram_sort('anagram', 'nagaram'))
        self.assertFalse(is_anagram_sort('rat', 'car'))


if __name__ == '__main__':
    unittest.main()
