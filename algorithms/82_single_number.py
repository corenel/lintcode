"""
Single Number
-------------

Given a non-empty array of integers, every element appears twice except
for one. Find that single one.

Note:
    Your algorithm should have a linear runtime complexity. Could you implement
    it without using extra memory?

Example 1:
    Input: [2,2,1]
    Output: 1

Example 2:
    Input: [4,1,2,1,2]
    Output: 4

Reference:
    - https://algorithm.yuanbin.me/zh-hans/math_and_bit_manipulation/single_number.html
    - https://leetcode.com/problems/single-number/
    - https://www.lintcode.com/problem/single-number/
"""

import unittest


def single_number(nums):
    """
    Find single number in given array

    :param nums: given array
    :type nums: list[int]
    :return: single number
    :rtype: int
    """
    result = 0
    if len(nums) != 0:
        for number in nums:
            result = result ^ number
    return result


class TestSingleNumber(unittest.TestCase):
    def test_single_number(self):
        self.assertEqual(1, single_number([2, 2, 1]))
        self.assertEqual(4, single_number([4, 1, 2, 1, 2]))


if __name__ == '__main__':
    unittest.main()
