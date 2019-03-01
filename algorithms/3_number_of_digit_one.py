"""
Number of digit one
-------------------

Given an integer n, count the total number of digit 1 appearing in all
non-negative integers less than or equal to n.

Example:
    - Input: 13
    - Output: 6

Explanation:
    Digit 1 occurred in the following numbers: 1, 10, 11, 12, 13.

Reference:
    - https://algorithm.yuanbin.me/zh-hans/math_and_bit_manipulation/digit_counts.html
    - https://leetcode.com/problems/number-of-digit-one/discuss/64381/4%2B-lines-O(log-n)-C%2B%2BJavaPython
    - https://leetcode.com/problems/number-of-digit-one/
    - https://www.lintcode.com/problem/digit-counts/description
"""

import unittest


def count_digit(k, n):
    """
    Count the number of k's between 0 and n. k can be 0 - 9.

    :param k: given digit
    :type k: int
    :param n: given number
    :type n: int
    :return: number of k's between 0 and n
    :rtype: int
    """
    count = 0
    for i in range(n + 1):
        # treat number as string
        # count digit character in the string
        count += str(i).count(str(k))
    return count


def count_digit_one(n):
    """
    Count the number of 1's between 0 and n

    :param n: given number
    :type n: int
    :return: number of 1's between 0 and n
    :rtype: int
    """
    ones, m = 0, 1
    while m <= n:
        # traverse each digit of n, if n=3401512
        # for m=100, split n into a=n//m=34015 and b=n%m=12
        # if a%10==1, #1=a//10*m+(b+1);
        # if a%10==0, #2=a//10*m;
        # if a%10>1; #3=a//10*m+m;
        # In general, #4=(a+8)//10*m+(a % 10 == 1)*(b + 1).
        # For general expression above:
        # if a%10>1, then (a+8)//10=a//10+1, #4=#3
        # if a%10==0, (a+8)//10=a//10, (a % 10 == 1)=false, #4=#2
        # if a%10==1, (a+8)//10=a//10, (a % 10 == 1)=true, #4=#1
        # This is how "(a+8)//10*m+(a % 10 == 1)*(b + 1)" covers
        # all three conditions.
        ones += (n // m + 8) // 10 * m + (n // m % 10 == 1) * (n % m + 1)
        m *= 10
    return ones


class TestCountDigit(unittest.TestCase):
    def test_count_digit(self):
        self.assertEqual(6, count_digit(1, 13))
        self.assertEqual(1, count_digit(1, 1))
        self.assertEqual(5, count_digit(1, 12))

    def test_count_digit_one(self):
        self.assertEqual(6, count_digit_one(13))
        self.assertEqual(1, count_digit_one(1))
        self.assertEqual(5, count_digit_one(12))


if __name__ == '__main__':
    unittest.main()
