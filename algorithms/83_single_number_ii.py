"""
Single Number II
----------------

Given a non-empty array of integers, every element appears three times
except for one, which appears exactly once. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement
it without using extra memory?

Example 1:
    - Input: [2,2,3,2]
    - Output: 3

Example 2:
    - Input: [0,1,0,1,0,1,99]
    - Output: 99

Reference:
    - https://algorithm.yuanbin.me/zh-hans/math_and_bit_manipulation/single_number_ii.html
    - https://www.geeksforgeeks.org/find-the-element-that-appears-once/
    - https://leetcode.com/problems/single-number-ii/
    - https://www.lintcode.com/problem/single-number-ii/
"""

import unittest


def single_number(nums):
    """
    Find single number in given array

    :param nums: given array
    :type nums: list[int]
    :return: single number
    :rtype: int
    """
    # Use two bit operator to save three states
    m1, m2 = 0, 0
    # n = 1, change in this order
    # m1 0 -> 0 -> 1 -> 0
    # m2 0 -> 1 -> 0 -> 0
    # n = 0, remain it same
    for n in nums:
        tmp = m1
        m1 = m1 ^ n & (m1 ^ m2)
        m2 = m2 ^ n & (~tmp)
    return m2


def single_number_2(nums):
    """
    Find single number in given array

    :param nums: given array
    :type nums: list[int]
    :return: single number
    :rtype: int
    """
    ones, twos = 0, 0
    for n in nums:
        # The expression "one & arr[i]" gives the bits that are
        # there in both 'ones' and new element from arr[].  We
        # add these bits to 'twos' using bitwise OR
        twos |= ones & n
        # XOR the new bits with previous 'ones' to get all bits
        # appearing odd number of times
        ones ^= n
        # The common bits are those bits which appear third time
        # So these bits should not be there in both 'ones' and 'twos'.
        # common_bit_mask contains all these bits as 0, so that the bits can
        # be removed from 'ones' and 'twos'
        common_bit_mask = ~(ones & twos)
        # Remove common bits (the bits that appear third time) from 'ones'
        ones &= common_bit_mask
        # Remove common bits (the bits that appear third time) from 'twos'
        twos &= common_bit_mask
        # uncomment this code to see intermediate values
        # print("ones: {:04b} twos: {:04b} n: {:04b}".format(ones, twos, n))
    return ones


def single_number_3(nums):
    """
    Find single number in given array

    :param nums: given array
    :type nums: list[int]
    :return: single number
    :rtype: int
    """

    def twos_comp(val, bits):
        """
        Compute the 2's compliment of int value val

        e.g. -4 ==> 11100 == -(10000) + 01100

        :param val: value
        :type val: int
        :param bits: number of bits
        :type bits: int
        :return: 2's compliment of int value
        :rtype: int
        """
        return -(val & (1 << (bits - 1))) | (val & ((1 << (bits - 1)) - 1))

    result = 0
    # iterate through every bit
    for i in range(32):
        # find sum of set bits at ith position in all array elements
        bit_i_sum = 0
        for num in nums:
            bit_i_sum += ((num >> i) & 1)
        # the bits with sum not multiple of 3, are the bits of element with
        # single occurrence.
        result |= ((bit_i_sum % 3) << i)
    # since the integer representation can be infinity in Python 3
    # we need convert the value of result into 2's compliment
    return twos_comp(result, 32)


def single_number_generalized(nums, k, l):
    """
    Given an array of integers, every element appears k times except for one.
    Find that single one which appears l times.

    We need a array x[i] with size k for saving the bits appears i times.
    For every input number a, generate the new counter by
    x[j] = (x[j-1] & a) | (x[j] & ~a). Except x[0] = (x[k] & a) | (x[0] & ~a).

    In the equation, the first part indicates the the carries from previous one.
    The second part indicates the bits not carried to next one.

    Then the algorithms run in O(kn) and the extra space O(k).

    :param nums: given array
    :type nums: list[int]
    :param k: times for every but one elements
    :type k: int
    :param l: times for single element
    :type l: int
    :return: single element
    :rtype: int
    """
    if len(nums) == 0:
        return 0
    x = [0] * k
    x[0] = ~0
    for i in range(len(nums)):
        t = x[k - 1]
        for j in range(k - 1, 0, -1):
            x[j] = (x[j - 1] & nums[i]) | (x[j] & ~nums[i])
        x[0] = (t & nums[i]) | (x[0] & ~nums[i])
    return x[l]


class TestSingleNumber(unittest.TestCase):
    def test_single_number(self):
        self.assertEqual(3, single_number([2, 2, 3, 2]))
        self.assertEqual(99, single_number([0, 1, 0, 1, 0, 1, 99]))

    def test_single_number_1(self):
        self.assertEqual(3, single_number_2([2, 2, 3, 2]))
        self.assertEqual(99, single_number_2([0, 1, 0, 1, 0, 1, 99]))

    def test_single_number_2(self):
        self.assertEqual(3, single_number_3([2, 2, 3, 2]))
        self.assertEqual(99, single_number_3([0, 1, 0, 1, 0, 1, 99]))

    def test_single_number_generalized(self):
        self.assertEqual(3, single_number_generalized([2, 2, 3, 2], 3, 1))
        self.assertEqual(99, single_number_generalized([0, 1, 0, 1, 0, 1, 99], 3, 1))
        self.assertEqual(2, single_number_generalized([2, 0, 1, 0, 1, 0, 1, 2], 3, 2))


if __name__ == '__main__':
    unittest.main()
