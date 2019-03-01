"""
Plus One
--------

Given a non-empty array of digits representing a non-negative integer,
plus one to the integer.

The digits are stored such that the most significant digit is at the
head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except
the number 0 itself.

Example 1:
    - Input: [1,2,3]
    - Output: [1,2,4]
    - Explanation: The array represents the integer 123.

Example 2:
    - Input: [4,3,2,1]
    - Output: [4,3,2,2]
    - Explanation: The array represents the integer 4321.

Reference:
    - https://algorithm.yuanbin.me/zh-hans/math_and_bit_manipulation/plus_one.html
    - https://leetcode.com/problems/plus-one/
    - https://www.lintcode.com/problem/plus-one/
"""

import unittest


def plus_one(digits):
    """
    Given a non-empty array of digits representing a non-negative integer,
    plus one to the integer.

    :param digits: list of digits of a non-negative integer,
    :type digits: list[int]
    :return: digits of operated integer
    :rtype: list[int]
    """
    result = []
    carry = 1

    for i in range(len(digits) - 1, -1, -1):
        result.append((digits[i] + carry) % 10)
        carry = (digits[i] + carry) // 10

    if carry:
        result.append(1)

    return list(reversed(result))


class TestPlusOne(unittest.TestCase):
    def test_plus_one(self):
        self.assertListEqual([1, 2, 4], plus_one([1, 2, 3]))
        self.assertListEqual([4, 3, 2, 2], plus_one([4, 3, 2, 1]))
        self.assertListEqual([1, 0, 0, 0], plus_one([9, 9, 9]))


if __name__ == '__main__':
    unittest.main()
