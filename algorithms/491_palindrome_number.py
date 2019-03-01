"""
Palindrome Number
-----------------

Determine whether an integer is a palindrome. An integer is a palindrome when
it reads the same backward as forward.

Example 1:
    Input: 121
    Output: true

Example 2:
   - Input: -121
   - Output: false
   - Explanation: From left to right, it reads -121. From right to left, it becomes
     121-. Therefore it is not a palindrome.

Example 3:
   - Input: 10
   - Output: false
   - Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

Follow up:
   Could you solve it without converting the integer to a string?

Reference:
    - https://algorithm.yuanbin.me/zh-hans/math_and_bit_manipulation/palindrome_number.html
    - https://leetcode.com/problems/palindrome-number/
    - https://www.lintcode.com/problem/palindrome-number/
"""

import unittest


def is_palindrome(x):
    """
    Check whether or not given number is palindrome

    :param x: given number
    :type x: int
    :return: whether or not given number is palindrome
    :rtype: bool
    """
    if x < 0:
        return False

    # for 32-bit integer, the maximum number of digits is int(log(2**31))
    mod = 1000000000
    while x // mod == 0 and mod > 1:
        mod //= 10

    while mod > 1:
        if x // mod != x % 10:
            return False
        x = (x % mod) // 10
        mod //= 100

    return True


class TestPalindromeNumber(unittest.TestCase):
    def test_palindrome_number(self):
        self.assertTrue(is_palindrome(121))
        self.assertFalse(is_palindrome(-121))
        self.assertFalse(is_palindrome(10))


if __name__ == '__main__':
    unittest.main()
