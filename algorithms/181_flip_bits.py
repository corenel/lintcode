"""
Flip Bits
---------

Determine the number of bits required to flip if you want to convert integer n to integer m.

Both n and m are 32-bit integers.

Example 1:
    - Input: n = 31, m = 14
    - Output:  2
    - Explanation: (11111) -> (01110) there are two different bits.

Example 2:
    - Input: n = 1, m = 7
    - Output:  2
    - Explanation: (001) -> (111) will change two bits.

Reference:
    - https://algorithm.yuanbin.me/zh-hans/math_and_bit_manipulation/flip_bits.html
    - https://www.lintcode.com/problem/flip-bits/description
"""

import unittest


def bit_swap_required(a, b):
    count = 0
    a_xor_b = a ^ b
    neg_flag = a_xor_b < 0

    # process negative binary number
    if neg_flag:
        a_xor_b = abs(a_xor_b) - 1

    while a_xor_b != 0:
        # remove the rightmost bit of 1
        # input: 1001100
        # -1: 1001011
        # result: 1001100 & 1001011 = 1001000
        a_xor_b &= a_xor_b - 1
        count += 1

    # for negative binary number, use 2's compliment
    if neg_flag:
        count = 32 - count

    return count


class TestFlipBits(unittest.TestCase):
    def test_flip_bits(self):
        self.assertEqual(2, bit_swap_required(31, 14))
        self.assertEqual(2, bit_swap_required(1, 7))
        self.assertEqual(31, bit_swap_required(1, -1))


if __name__ == '__main__':
    unittest.main()
