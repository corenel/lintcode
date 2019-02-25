"""
Single Number III
-----------------

Given an array of numbers nums, in which exactly two elements appear only once
and all the other elements appear exactly twice. Find the two elements that
appear only once.

Example:
    - Input:  [1,2,1,3,2,5]
    - Output: [3,5]

Note:
    - The order of the result is not important. So in the above example, [5, 3] is also correct.
    - Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?

Reference:
    - https://algorithm.yuanbin.me/zh-hans/math_and_bit_manipulation/single_number_iii.html
    - https://www.geeksforgeeks.org/find-two-non-repeating-elements-in-an-array-of-repeating-elements/
    - https://leetcode.com/problems/single-number-iii/
    - https://www.lintcode.com/problem/single-number-iii/
"""

import unittest


def single_number(nums):
    """
    Find two single numbers in given array

    All the bits that are set in xor will be set in one non-repeating element
    (x1 or x2) and not in other. So if we take any set bit of xor and divide
    the elements of the array in two sets – one set of elements with same bit
    set and other set with same bit not set. By doing so, we will get x in one
    set and y in another set. Now if we do XOR of all the elements in first
    set, we will get first non-repeating element, and by doing same in other
    set we will get the second non-repeating element.

    :param nums: given array
    :type nums: list[int]
    :return: single number
    :rtype: list[int]
    """
    # get the xor of all elements
    x1_xor_x2 = 0
    for n in nums:
        x1_xor_x2 ^= n

    # get the rightmost set bit
    last_1_bit = x1_xor_x2 & ~(x1_xor_x2 - 1)

    # now divide elements in two sets by comparing rightmost set
    # bit of xor with bit at same position in each element.
    x1, x2 = 0, 0
    for n in nums:
        if last_1_bit & n == 0:
            x1 ^= n
        else:
            x2 ^= n

    return [x1, x2]


class TestSingleNumberIII(unittest.TestCase):
    def test_single_number_ii(self):
        self.assertIn(single_number([1, 2, 1, 3, 2, 5]), [[3, 5], [5, 3]])


if __name__ == '__main__':
    unittest.main()
