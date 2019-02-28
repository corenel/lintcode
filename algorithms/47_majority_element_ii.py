"""
Majority Element II
-------------------

Given an array of integers, the majority number is the number that
occurs more than 1/3 of the size of the array.

Note:
    - The algorithm should run in linear time and in O(1) space.
    - There is only one majority number in the array.

Example 1:
    - Input: [99,2,99,2,99,3,3],
    - Output: 99.

Example 2:
    - Input: [1, 2, 1, 2, 1, 3, 3],
    - Output: 1.

Challenge:
    O(n) time and O(1) extra space.

Reference:
    - https://algorithm.yuanbin.me/zh-hans/math_and_bit_manipulation/majority_number_ii.html
    - https://leetcode.com/problems/majority-element-ii/
    - https://www.lintcode.com/problem/majority-element-ii/
"""

import unittest
import math


def majority_element(nums):
    """
    Find the majority elements in given array

    :param nums: list[int]
    :type nums: given array of numbers
    :return: the majority elements
    :rtype: list[int]
    """
    if len(nums) == 0:
        return -1

    k1, k2, c1, c2 = math.inf, math.inf, 0, 0
    for n in nums:
        if c1 == 0 and k1 != n and k2 != n:
            k1 = n
        elif c2 == 0 and k2 != n and k1 != n:
            k2 = n

        if k1 == n:
            c1 += 1
        elif k2 == n:
            c2 += 1
        else:
            c1 -= 1
            c2 -= 1

    c1, c2 = 0, 0
    for n in nums:
        if n == k1:
            c1 += 1
        elif n == k2:
            c2 += 1
    if c1 > c2:
        return c1
    else:
        return c2


class TestMajorityElementII(unittest.TestCase):
    def test_majority_element_ii(self):
        self.assertEqual(99, majority_element([99, 2, 99, 2, 99, 3, 3]))
        self.assertEqual(1, majority_element([1, 2, 1, 2, 1, 3, 3]))


if __name__ == '__main__':
    unittest.main()
