"""
Fast Power
----------

Calculate the an % b where a, b and n are all 32bit positive integers.

Example:
    - For 2^31 % 3 = 2
    - For 100^1000 % 1000 = 0

Challenge:
    O(log n)

Reference:
    - https://algorithm.yuanbin.me/zh-hans/math_and_bit_manipulation/fast_power.html
    - https://www.lintcode.com/problem/fast-power/
"""

import unittest


def fast_power(a, b, n):
    """
    Calculate the a^n % b

    :param a: a 32-bit integer
    :type a: int
    :param b: a 32-bit integer
    :type b: int
    :param n: a 32-bit integer
    :type n: int
    :return: result
    :rtype: int
    """
    # basic cases
    if n == 0:
        return 1 % b
    elif n == 1:
        return a % b
    elif n < 0:
        return -1

    # (a * c) % b = ((a % b) * (c % b)) % b
    product = fast_power(a, b, n // 2)
    product = (product * product) % b
    if n % 2 == 1:
        product = (product * a) % b

    return product


class TestFastPower(unittest.TestCase):
    def test_fast_power(self):
        self.assertEqual(2, fast_power(2, 3, 31))
        self.assertEqual(0, fast_power(100, 1000, 1000))


if __name__ == '__main__':
    unittest.main()
