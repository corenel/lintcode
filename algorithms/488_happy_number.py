"""
Happy Number
------------

Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with
any positive integer, replace the number by the sum of the squares of its
digits, and repeat the process until the number equals 1 (where it will stay),
or it loops endlessly in a cycle which does not include 1. Those numbers for
which this process ends in 1 are happy numbers.

Example:
    - Input: 19
    - Output: true
    - Explanation:
        1^2 + 9^2 = 82
        8^2 + 2^2 = 68
        6^2 + 8^2 = 100
        1^2 + 0^2 + 0^2 = 1

Reference:
    - https://algorithm.yuanbin.me/zh-hans/math_and_bit_manipulation/happy_number.html
    - https://leetcode.com/problems/happy-number/
    - https://www.lintcode.com/problem/happy-number/
"""

import unittest


def is_happy(n):
    """
    Determine whether or not a number is happy

    :param n: given number
    :type n: int
    :return: whether or not a number is happy
    :rtype: bool
    """

    def digits_square(num):
        """
        Compute the sum of the squares of digits of given number

        :param num: given number
        :type num: int
        :return: result
        :rtype: int
        """
        new_num = 0
        while num > 0:
            new_num += (num % 10) ** 2
            num //= 10
        return new_num

    if n < 0:
        return False
    elif n == 1:
        return True

    count = []
    while n != 1:
        n = digits_square(n)
        if n == 1:
            return True
        elif n in count:
            return False
        else:
            count.append(n)


class TestHappyNumber(unittest.TestCase):
    def test_happy_number(self):
        self.assertTrue(is_happy(19))


if __name__ == '__main__':
    unittest.main()
