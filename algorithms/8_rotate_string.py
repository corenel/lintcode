"""
Rotate String
-------------

Given a string (Given in the way of char array) and an offset,
rotate the string by offset in place. (rotate from left to right)

Note:
    offset >= 0

Example 1:
    - Input: str="abcdefg", offset = 3
    - Output:"efgabcd"

Example 2:
    - Input: str="abcdefg", offset = 0
    - Output: "abcdefg"

Example 3:
    - Input: str="abcdefg", offset = 1
    - Output: "gabcdef"

Example 4
    - Input: str="abcdefg", offset =2
    - Output:"fgabcde"

"""

import unittest


def rotate_string(string, offset):
    """
    Rotate string in place

    :param string: given array of characters
    :type string: list[str]
    :param offset: offset for rotation
    :type offset: int
    :return: list[str]
    :rtype: rotated string
    """
    if len(string) == 0 or offset == 0:
        return string

    offset %= len(string)

    # solution 1
    # temp = string[len(string) - offset:] + string[:len(string) - offset]
    # for i in range(len(string)):
    #     string[i] = temp[i]

    # solution 2
    # string[::] = string[len(string) - offset:] + string[:len(string) - offset]

    # solution 3
    string[len(string) - offset:] = string[len(string) - offset:][::-1]
    string[:len(string) - offset] = string[:len(string) - offset][::-1]
    string[::] = string[::-1]

    return string


class TestRotateString(unittest.TestCase):
    def test_rotate_string(self):
        self.assertEqual(list('efgabcd'), rotate_string(list('abcdefg'), 3))
        self.assertEqual(list('abcdefg'), rotate_string(list('abcdefg'), 0))
        self.assertEqual(list('gabcdef'), rotate_string(list('abcdefg'), 1))
        self.assertEqual(list('fgabcde'), rotate_string(list('abcdefg'), 2))


if __name__ == '__main__':
    unittest.main()
