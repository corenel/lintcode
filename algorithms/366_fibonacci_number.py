"""
Fibonacci Number
----------------

The Fibonacci numbers, commonly denoted F(n) form a sequence, called the
Fibonacci sequence, such that each number is the sum of the two preceding
ones, starting from 0 and 1. That is,

- F(0) = 0,   F(1) = 1
- F(N) = F(N - 1) + F(N - 2), for N > 1.

Given N, calculate F(N).

Example 1:
    - Input: 2
    - Output: 1
    - Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.

Example 2:
    - Input: 3
    - Output: 2
    - Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.

Example 3:
    - Input: 4
    - Output: 3
    - Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.

Note:
    0 ≤ N ≤ 30.

Reference:
    - https://algorithm.yuanbin.me/zh-hans/math_and_bit_manipulation/fibonacci.html
    - https://leetcode.com/problems/fibonacci-number/
    - https://www.lintcode.com/problem/fibonacci/

"""

import unittest


def fibonacci_iterative(n):
    """
    Compute the Fibonacci numbers with given number by iterative method

    :param n: given number
    :type n: int
    :return: the Fibonacci numbers
    :rtype: int
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n < 0:
        return -1

    fn, fn1, fn2 = 0, 0, 1
    for i in range(2, n + 1):
        fn = fn1 + fn2
        fn1 = fn2
        fn2 = fn
    return fn


def fibonacci_recursive(n):
    """
    Compute the Fibonacci numbers with given number by recursive method

    :param n: given number
    :type n: int
    :return: the Fibonacci numbers
    :rtype: int
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n < 0:
        return -1

    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


class TestFibonacciNumber(unittest.TestCase):
    def test_fibonacci_number_iterative(self):
        self.assertEqual(1, fibonacci_iterative(2))
        self.assertEqual(2, fibonacci_iterative(3))
        self.assertEqual(3, fibonacci_iterative(4))

    def test_fibonacci_number_recursive(self):
        self.assertEqual(1, fibonacci_recursive(2))
        self.assertEqual(2, fibonacci_recursive(3))
        self.assertEqual(3, fibonacci_recursive(4))


if __name__ == '__main__':
    unittest.main()
