"""
Ugly Number
-----------

Write a program to check whether a given number is an ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.

Example 1:
    - Input: 6
    - Output: true
    - Explanation: 6 = 2 × 3

Example 2:
    - Input: 8
    - Output: true
    - Explanation: 8 = 2 × 2 × 2

Example 3:
    - Input: 14
    - Output: false
    - Explanation: 14 is not ugly since it includes another prime factor 7.

Note:
    - 1 is typically treated as an ugly number.
    - Input is within the 32-bit signed integer range: [−2^31,  2^31 − 1].

Reference:
    - https://algorithm.yuanbin.me/zh-hans/math_and_bit_manipulation/ugly_number.html
    - https://www.geeksforgeeks.org/ugly-numbers/
    - https://leetcode.com/problems/ugly-number/
    - https://www.lintcode.com/problem/ugly-number/
"""
import unittest


def is_ugly(num, factors=(2, 3, 5)):
    """
    Check whether a given number is an ugly number

    :param num: given number
    :type num: int
    :param factors: prime factors for ugly number
    :type factors: list[int] or tuple[int]
    :return: whether a given number is an ugly number
    :rtype: bool
    """
    if num == 1:
        return True
    elif num <= 0:
        return False

    for factor in factors:
        while num % factor == 0:
            num //= factor
    return num == 1


def kth_ugly_number(k):
    """
    Find kth ugly number

    :param k: given k
    :type k: int
    :return: kth ugly number
    :rtype: int
    """
    # list of ngly numbers
    ugly_numbers = [0] * k
    # 1 is the first ugly number
    ugly_numbers[0] = 1
    # indices of multiplier
    i_2 = i_3 = i_5 = 0
    # value of pointer
    num_2, num_3, num_5 = 2, 3, 5

    # start loop to find value from ugly[1] to ugly[n]
    for i in range(1, k):
        # choose the min value of all available multiples
        ugly_numbers[i] = min(num_2, num_3, num_5)
        # increment the value of index accordingly
        if ugly_numbers[i] == num_2:
            i_2 += 1
            num_2 = ugly_numbers[i_2] * 2
        if ugly_numbers[i] == num_3:
            i_3 += 1
            num_3 = ugly_numbers[i_3] * 3
        if ugly_numbers[i] == num_5:
            i_5 += 1
            num_5 = ugly_numbers[i_5] * 5

    # return ugly[n] value
    return ugly_numbers[-1]


class TestUglyNumber(unittest.TestCase):
    def test_ugly_number(self):
        self.assertTrue(is_ugly(6, factors=(2, 3, 5)))
        self.assertTrue(is_ugly(8, factors=(2, 3, 5)))
        self.assertFalse(is_ugly(14, factors=(2, 3, 5)))

    def test_kth_ugly_number(self):
        self.assertEqual(5832, kth_ugly_number(150))


if __name__ == '__main__':
    unittest.main()
