"""
Update Bits
-----------

Given two 32-bit numbers, N and M, and two bit positions, i and j. Write a
method to set all bits between i and j in N equal to M (e g , M becomes a
substring of N start from i to j)


Note:
    - In the function, the numbers N and M will given in decimal, you should
      also return a decimal number.
    - You can assume that the bits j through i have enough space to fit all
      of M. That is, if M=10011， you can assume that there are at least 5
      bits between j and i. You would not, for example, have j=3 and i=2,
      because M could not fully fit between bit 3 and bit 2.

Example 1:
    - Input: N=(10000000000)2 M=(10101)2 i=2 j=6
    - Output: N=(10001010100)2

Example 2:
    - Input: N=(10000000000)2 M=(11111)2 i=2 j=6
    - Output: N=(10001111100)2

Challenge:
    Minimum number of operations?

Reference:
    - https://algorithm.yuanbin.me/zh-hans/math_and_bit_manipulation/update_bits.html
    - https://www.lintcode.com/problem/update-bits/
"""

import unittest


def update_bits(n, m, i, j):
    """
    Update n with m at bit position from i to j

    :param n: original number to be updated
    :type n: int
    :param m: number to update
    :type m: int
    :param i: beginning bit position
    :type i: int
    :param j: ending bit position
    :type j: int
    :return: updated number
    :rtype: int
    """
    # mask = left | right
    # left = 1111...000...000
    # right = 0000...000...111
    if j < 31:
        mask = (~0 << (j + 1)) | ((1 << i) - 1)
        result = (n & mask) | (m << i)
    else:
        # integer of Python 3 is not 32-bit but infinity
        # so to simulate as 32-bit, we need to check the 32th bit
        # and compute the compliment
        mask = (1 << i) - 1
        result = (n & mask) | (m << i)
        if (result >> 32) == 0:
            result -= 1 << 32
    return result


class TestUpdateBits(unittest.TestCase):
    def test_update_bits(self):
        # self.assertEqual(
        #     0b10001010100,
        #     update_bits(0b10000000000, 0b10101, 2, 6))
        # self.assertEqual(
        #     0b10001111100,
        #     update_bits(0b10000000000, 0b11111, 2, 6))
        # self.assertEqual(
        #     2147483127,
        #     update_bits(-521, 0, 31, 31))
        self.assertEqual(
            -134217272,
            update_bits(456, 31, 27, 31))


if __name__ == '__main__':
    unittest.main()
