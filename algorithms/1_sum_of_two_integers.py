"""
Sum of Two Integers
-------------------

Calculate the sum of two integers a and b, but you are not allowed to use the
operator + and -.

Example 1:
    Input: a = 1, b = 2
    Output: 3

Example 2:
    Input: a = -2, b = 3
    Output: 1

Reference:
    - https://algorithm.yuanbin.me/zh-hans/math_and_bit_manipulation/fibonacci.html
    - https://leetcode.com/problems/sum-of-two-integers/
    - https://www.lintcode.com/problem/a-b-problem/
"""

import unittest


def get_sum(a: int, b: int) -> int:
    """
    Add two numbers without using arithmetic operators

    We consider doing it bitwise then we can do simply by adding bits from
    left to right with carry.

    If we draw truth table then sum = a_bit ^ b_bit ^ c, and
    carry = a_bit&b_bit | c &(a_bit^b_bit).

    But problem with negative numbers. If we do 2's complement of the negative
    numbers then we are fine (e.g., 4+(-3)=4+(2's complement of 3)). Also if
    return number is negative the python still considers that as unsigned int.

    Hence we have to do a little hack to make it negative.

    :param a: first number
    :type a: int
    :param b: second number
    :type b: int
    :return: the sum of two given numbers
    :rtype: int
    """
    # if given numbers are negative then do 2's complement
    if a < 0:
        a = get_2_complement(a)
    if b < 0:
        b = get_2_complement(b)

    # add two numbers
    res = get_sum_helper(a, b)

    # if MSB of result is 1, then return negative
    if res & 1 << 31:
        res = res ^ (-1)
        return (-1) * get_sum_helper(res, 1)

    return res


def get_2_complement(n):
    return get_sum_helper((-1 * n) ^ (-1), 1)


def get_sum_helper(a, b):
    c = 0
    res = 0
    for i in range(64):
        val1 = a & 1
        val2 = b & 1
        val3 = val1 ^ val2 ^ c
        c = val1 & val2 | c & (val1 ^ val2)
        a = a >> 1
        b = b >> 1
        val3 = val3 << i
        res = res | val3
    return res


def get_sum_2(a, b):
    """
    Add two numbers without using arithmetic operators

    :param a: first number
    :type a: int
    :param b: second number
    :type b: int
    :return: the sum of two given numbers
    :rtype: int
    """
    INT_RANGE = 0xFFFFFFFF
    while b != 0:
        a, b = a ^ b, (a & b) << 1
        a &= INT_RANGE
    return a if a >> 31 <= 0 else a ^ ~INT_RANGE


class TestSumOfTwoIntegers(unittest.TestCase):
    def test_sum_of_two_integers(self):
        self.assertEqual(3, get_sum(1, 2))
        self.assertEqual(1, get_sum(-2, 3))
        self.assertEqual(-1, get_sum(2, -3))

    def test_sum_of_two_integers_2(self):
        self.assertEqual(3, get_sum_2(1, 2))
        self.assertEqual(1, get_sum_2(-2, 3))
        self.assertEqual(-1, get_sum_2(2, -3))


if __name__ == '__main__':
    unittest.main()
