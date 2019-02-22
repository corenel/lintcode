"""
Reverse Words in a String
-------------------------

Given an input string, reverse the string word by word.

Example:
    - Input: "the sky is blue",
    - Output: "blue is sky the".

Note:
    - A word is defined as a sequence of non-space characters.
    - Input string may contain leading or trailing spaces. However, your reversed string should not contain leading or trailing spaces.
    - You need to reduce multiple spaces between two words to a single space in the reversed string.

Follow up:
    For C programmers, try to solve it in-place in O(1) space.

Reference:
    - https://algorithm.yuanbin.me/zh-hans/string/reverse_words_in_a_string.html
    - https://leetcode.com/problems/reverse-words-in-a-string/
    - https://www.lintcode.com/problem/reverse-words-in-a-string/
"""

import unittest


def reverse_words_in_a_string(string):
    """
    Given an input string, reverse the string word by word.

    :param string: given string
    :type string: str
    :return: reversed string
    :rtype: str
    """
    # return ' '.join(string.strip().split(' ')[::-1])
    splited = [word for word in string.split(' ')
               if word != '']
    return ' '.join(splited[::-1])


class TestReverseWordsInAString(unittest.TestCase):
    def test_reverse_words_in_a_string(self):
        self.assertEqual(
            'blue is sky the',
            reverse_words_in_a_string('the sky is blue'))
        self.assertEqual(
            'blue is sky the',
            reverse_words_in_a_string('the  sky    is blue '))
        self.assertEqual(
            '',
            reverse_words_in_a_string(' '))
        self.assertEqual(
            '',
            reverse_words_in_a_string('  '))


if __name__ == '__main__':
    unittest.main()
