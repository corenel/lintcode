"""
Number of 1 Bits
----------------

Write a function that takes an unsigned integer and return the number of '1'
bits it has (also known as the Hamming weight).

Example 1:
    - Input: 00000000000000000000000000001011
    - Output: 3
    - Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.

Example 2:
    - Input: 00000000000000000000000010000000
    - Output: 1
    - Explanation: The input binary string 00000000000000000000000010000000 has a total of one '1' bit.

Example 3:
    - Input: 11111111111111111111111111111101
    - Output: 31
    - Explanation: The input binary string 11111111111111111111111111111101 has a total of thirty one '1' bits.

Note:
    - Note that in some languages such as Java, there is no unsigned integer type. In this case, the input will be given as signed integer type and should not affect your implementation, as the internal binary representation of the integer is the same whether it is signed or unsigned.
    - In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 3 above the input represents the signed integer -3.

Follow up:
    If this function is called many times, how would you optimize it?

Reference:
    - https://algorithm.yuanbin.me/zh-hans/math_and_bit_manipulation/count_1_in_binary.html
    - https://leetcode.com/problems/number-of-1-bits/
    - https://www.lintcode.com/problem/count-1-in-binary/
"""

import unittest


def hamming_weight(n):
    """
    Count the number of '1' bits the given number has (also known as the Hamming weight).

    - Time complexity: O(m)
    - Space complexity: O(1)

    where m is the number of '1' bits

    :param n: given unsigned numebr
    :type n: int
    :return: the number of '1' bits the given number has
    :rtype: int
    """
    if n < 0:
        n = (1 << 32) + n
    count = 0
    while n != 0:
        n &= n - 1
        count += 1
    return count


def hamming_weight_2(n):
    """
    Count the number of '1' bits the given number has (also known as the Hamming weight).

    - Time complexity: O(n)
    - Space complexity: O(1)

    :param n: given unsigned numebr
    :type n: int
    :return: the number of '1' bits the given number has
    :rtype: int
    """
    if n < 0:
        n = (1 << 32) + n
    count = 0
    for i in range(32):
        count += n & 1
        n >>= 1
    return count


class TestNumberOf1Bits(unittest.TestCase):

    def test_number_of_1_bits_1(self):
        self.assertEqual(3, hamming_weight(0b00000000000000000000000000001011))
        self.assertEqual(1, hamming_weight(0b00000000000000000000000010000000))
        self.assertEqual(31,
                         hamming_weight(0b11111111111111111111111111111101))
        self.assertEqual(32, hamming_weight(-1))

    def test_number_of_1_bits_2(self):
        self.assertEqual(3,
                         hamming_weight_2(0b00000000000000000000000000001011))
        self.assertEqual(1,
                         hamming_weight_2(0b00000000000000000000000010000000))
        self.assertEqual(31,
                         hamming_weight_2(0b11111111111111111111111111111101))
        self.assertEqual(32, hamming_weight_2(-1))


if __name__ == '__main__':
    unittest.main()
