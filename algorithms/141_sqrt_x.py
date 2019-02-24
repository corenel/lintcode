"""
Sqrt(x)
-------

Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to be
a non-negative integer.

Since the return type is an integer, the decimal digits are truncated
and only the integer part of the result is returned.

Example 1:
    - Input: 4
    - Output: 2

Example 2:
    - Input: 8
    - Output: 2
    - Explanation: The square root of 8 is 2.82842..., and since the
      decimal part is truncated, 2 is returned.

Reference:
    - https://algorithm.yuanbin.me/zh-hans/binary_search/sqrt_x.html
    - https://leetcode.com/problems/sqrtx/
    - https://www.lintcode.com/problem/sqrtx/
"""

import unittest


def my_sqrt(x):
    """
    Compute integer part of the square root of given number

    :param x: given integer
    :type x: int
    :return: integer part of the square root
    :rtype: int
    """
    if x < 0:
        return -1
    elif x == 0:
        return 0

    left, right = 1, x
    while left + 1 < right:
        mid = (left + right) // 2
        mid_2 = mid * mid
        if mid_2 == x:
            return mid
        elif mid_2 > x:
            right = mid
        else:
            left = mid
    return left


class TestSqrtX(unittest.TestCase):
    def test_sqrt_x(self):
        self.assertEqual(1, my_sqrt(1))
        self.assertEqual(1, my_sqrt(2))
        self.assertEqual(2, my_sqrt(4))
        self.assertEqual(2, my_sqrt(8))


if __name__ == '__main__':
    unittest.main()
