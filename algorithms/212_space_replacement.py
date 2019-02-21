"""
Space Replacement
-----------------

Write a method to replace all spaces in a string with %20. The string
is given in a characters array, you can assume it has enough space for
replacement and you are given the true length of the string.

You code should also return the new length of the string after replacement.

Note:
    If you are using Java or Python，please use characters array instead of string.

Example 1:
    - Input: string[] = "Mr John Smith" and length = 13
    - Output: string[] = "Mr%20John%20Smith" and return 17
    - Explanation: The string after replacement should be "Mr%20John%20Smith",
       you need to change the string in-place and return the new length 17.

Example 2:
    - Input: string[] = "LintCode and Jiuzhang" and length = 21
    - Output: string[] = "LintCode%20and%20Jiuzhang" and return 25
    - Explanation: The string after replacement should be
      "LintCode%20and%20Jiuzhang", you need to change the string in-place and
      return the new length 25.

Challenge:
    Do it in-place.

Reference:
    - https://algorithm.yuanbin.me/zh-hans/string/space_replacement.html
    - https://www.lintcode.com/problem/space-replacement/
"""

import unittest


def replace_blank(string, length):
    """
    Replace all spaces in a string with %20 in place

    Time complexity: O(n)
    Space complexity: O(1)

    :param string: given string
    :type string: list[str]
    :param length: the true length of given string
    :type length: int
    :return: replaced string
    :rtype: list[str]
    """
    # get the number of spaces
    num_space = 0
    for i in range(length):
        if string[i].isspace():
            num_space += 1
    # compute new length
    new_length = num_space * 2 + length
    # assign new value from right to left
    for i in range(length - 1, -1, -1):
        if string[i] == ' ':
            string[new_length - 1] = '0'
            string[new_length - 2] = '2'
            string[new_length - 3] = '%'
            new_length -= 3
        else:
            string[new_length - 1] = string[i]
            new_length -= 1
    return num_space * 2 + length


class TestSpaceReplacement(unittest.TestCase):
    def test_space_replacement(self):
        s = list('Mr John Smith') + [''] * 4
        res = replace_blank(s, 13)
        self.assertListEqual(list('Mr%20John%20Smith'), s)
        self.assertEqual(17, res)

        s = list('LintCode and Jiuzhang') + [''] * 4
        res = replace_blank(s, 21)
        self.assertListEqual(list('LintCode%20and%20Jiuzhang'), s)
        self.assertEqual(25, res)

        s = list(' ') + [''] * 2
        res = replace_blank(s, 1)
        self.assertListEqual(list('%20'), s)
        self.assertEqual(3, res)


if __name__ == '__main__':
    unittest.main()
