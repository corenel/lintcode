"""
Factorial Trailing Zeroes
-------------------------

Given an integer n, return the number of trailing zeroes in n!.

Example 1:
    - Input: 3
    - Output: 0
    - Explanation: 3! = 6, no trailing zero.

Example 2:
    - Input: 5
    - Output: 1
    - Explanation: 5! = 120, one trailing zero.

Note:
    Your solution should be in logarithmic time complexity.

Reference:
    - https://algorithm.yuanbin.me/zh-hans/math_and_bit_manipulation/factorial_trailing_zeroes.html
    - https://leetcode.com/problems/factorial-trailing-zeroes/
    - https://www.lintcode.com/problem/trailing-zeros/description
"""

import unittest


def trailing_zeroes(n):
    """
    Find the number of trailing zeroes in n!

    :param n: given number
    :type n: int
    :return: the number of trailing zeroes in n!
    :rtype: int
    """
    if n < 0:
        return -1

    count = 0
    while n > 0:
        # 2 * 5 = 10, which add trailing zeroes
        # since even number is much more than numbers can be divided by 5
        # we just consider n % 5 == 0
        n //= 5
        count += n
    return count


class TestFactorialTrailingZeroes(unittest.TestCase):
    def test_factorial_trailing_zeroes(self):
        self.assertEqual(0, trailing_zeroes(3))
        self.assertEqual(1, trailing_zeroes(5))


if __name__ == '__main__':
    unittest.main()
