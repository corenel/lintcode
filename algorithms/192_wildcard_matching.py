"""
Wildcard Matching
-----------------

Given an input string (s) and a pattern (p), implement wildcard pattern
matching with support for '?' and '*'.

    - '?' Matches any single character.
    - '*' Matches any sequence of characters (including the empty sequence).
    - The matching should cover the entire input string (not partial).
    - s could be empty and contains only lowercase letters a-z.
    - p could be empty and contains only lowercase letters a-z, and characters like ? or *.

Example 1:
    - Input: s = "aa", p = "a"
    - Output: false
    - Explanation: "a" does not match the entire string "aa".

Example 2:
    - Input: s = "aa", p = "*"
    - Output: true
    - Explanation: '*' matches any sequence.

Example 3:
    - Input: s = "cb", p = "?a"
    - Output: false
    - Explanation: '?' matches 'c', but the second letter is 'a',
      which does not match 'b'.

Example 4:
    - Input: s = "adceb", p = "*a*b"
    - Output: true
    - Explanation: The first '*' matches the empty sequence, while
       the second '*' matches the substring "dce".

Example 5:
    - Input: s = "acdcb", p = "a*c?b"
    - Output: false

Reference:
    - https://algorithm.yuanbin.me/zh-hans/string/wildcard_matching.html
    - https://leetcode.com/problems/wildcard-matching/
    - https://www.lintcode.com/problem/wildcard-matching/
    - http://yucoding.blogspot.com/2013/02/leetcode-question-123-wildcard-matching.html
"""

import unittest


def is_match(s, p):
    """
    Wildcard pattern matching with given string and pattern

    :param s: given string
    :type s: str
    :param p: given pattern
    :type p: str
    :return: whether or not pattern is matched
    :rtype: bool
    """
    curr_s = curr_p = match = 0
    star_p = -1
    while curr_s < len(s):
        # if *s==*p or *p == ? which means this is a match
        # then goes to next element
        if curr_p < len(p) and (s[curr_s] == p[curr_p] or p[curr_p] == '?'):
            curr_s += 1
            curr_p += 1
        # if p=='*', this is also a match
        # but one or many chars may be available
        # so let us save this *'s position and the matched s position
        elif curr_p < len(p) and p[curr_p] == '*':
            match = curr_s
            star_p = curr_p
            curr_p += 1
        # if not match, then we check if there is a * previously showed up
        # if there is an *,  we set current p to the next element of *
        # and set current s to the next saved s position.
        elif star_p != -1:
            curr_p = star_p + 1
            match += 1
            curr_s = match
        # if not match and there is no *,  return False;
        else:
            return False
    # check the rest element in p
    # if all are *, True, else False
    while curr_p < len(p) and p[curr_p] == '*':
        curr_p += 1
    return curr_p == len(p)


class TestWildcardMatching(unittest.TestCase):
    def test_wildcard_matching(self):
        self.assertFalse(is_match('aa', 'a'))
        self.assertTrue(is_match('aa', '*'))
        self.assertFalse(is_match('cb', '?a'))
        self.assertTrue(is_match('adceb', '*a*b'))
        self.assertFalse(is_match('acdcb', 'a*c?b'))


if __name__ == '__main__':
    unittest.main()
