"""
Group Anagrams
--------------

Given an array of strings, group anagrams together.

LintCode Example:

- Given ['lint', 'intl', 'inlt', 'code'], return ['lint', 'inlt', 'intl'].
- Given ['ab', 'ba', 'cd', 'dc', 'e'], return ['ab', 'ba', 'cd', 'dc'].

Note:

- All inputs will be in lowercase.
- The order of your output does not matter.
"""

import unittest


def group_anagrams(strs):
    """
    Group anagrams in given list of strings

    :param strs: a list of input strings
    :type strs: list[str]
    :return: grouped anagrams
    :rtype: list[str]
    """
    str_dict = {}
    for string in strs:
        str_sorted = ''.join(sorted(string))
        if str_sorted not in str_dict:
            str_dict[str_sorted] = [string]
        else:
            str_dict[str_sorted].append(string)
    result = []
    for v in str_dict.values():
        if len(v) > 1:
            result.extend(v)
    return result


class TestGroupAnagrams(unittest.TestCase):
    def test_group_anagrams_lintcode(self):
        self.assertListEqual(
            ['lint', 'intl', 'inlt'],
            group_anagrams(['lint', 'intl', 'inlt', 'code']))
        self.assertListEqual(
            ['ab', 'ba', 'cd', 'dc'],
            group_anagrams(['ab', 'ba', 'cd', 'dc', 'e']))


if __name__ == '__main__':
    unittest.main()
