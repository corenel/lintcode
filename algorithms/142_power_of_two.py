"""
Power of Two
------------

Given an integer, write a function to determine if it is a power of two.

Example 1:
    - Input: 1
    - Output: true
    - Explanation: 2^0 = 1

Example 2:
    - Input: 16
    - Output: true
    - Explanation: 2^4 = 16

Example 3:
    - Input: 218
    - Output: false

Challenge
    O(1) time

Reference:
    - https://algorithm.yuanbin.me/zh-hans/math_and_bit_manipulation/o1_check_power_of_2.html
    - https://leetcode.com/problems/power-of-two/
    - https://www.lintcode.com/problem/o1-check-power-of-2/description
"""

import unittest


def is_power_of_two(n):
    """
    Determine whether or not given number is a power of two

    :param n: given number
    :type n: int
    :return: whether or not given number is a power of two
    :rtype: bool
    """
    if n != 0 and n & (n - 1) == 0:
        return True
    else:
        return False


class TestPowerOfTwo(unittest.TestCase):
    def test_power_of_two(self):
        self.assertTrue(is_power_of_two(1))
        self.assertTrue(is_power_of_two(16))
        self.assertFalse(is_power_of_two(0))
        self.assertFalse(is_power_of_two(218))


if __name__ == '__main__':
    unittest.main()
