"""
Print Numbers by Recursion
--------------------------

Print numbers from 1 to the largest number with N digits by recursion.

It's pretty easy to do recursion like:

Example 1:
    - Input : N = 1
    - Output :[1,2,3,4,5,6,7,8,9]

Example 2:
    - Input : N = 2
    - Output :[[1,2,3,4,5,6,7,8,9,10,11,12,...,99]

Challenge
    Do it in recursion, not for-loop.

Reference:
    - https://algorithm.yuanbin.me/zh-hans/math_and_bit_manipulation/print_numbers_by_recursion.html
    - https://www.lintcode.com/problem/print-numbers-by-recursion/description
"""

import unittest


def numbers_by_recursion(n):
    """
    Print numbers from 1 to the largest number with N digits by recursion.

    :param n: given number
    :type n: int
    :return: numbers from 1 to the largest number with N digits
    :rtype: list[int]
    """
    result = []
    if n > 0:
        result = numbers_by_recursion(n - 1)
        for i in range(10 ** (n - 1) , 10 ** n):
            result.append(i)
    return result


class TestPrintNumbersByRecursion(unittest.TestCase):
    def test_print_numbers_by_recursion(self):
        self.assertListEqual(
            [i for i in range(1, 10)],
            numbers_by_recursion(1))
        self.assertListEqual(
            [i for i in range(1, 100)],
            numbers_by_recursion(2))


if __name__ == '__main__':
    unittest.main()
