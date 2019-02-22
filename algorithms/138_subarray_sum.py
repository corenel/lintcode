"""
Subarray Sum
------------

Given an integer array, find a subarray where the sum of numbers is zero.
Your code should return the index of the first number and the index of the
last number.

There is at least one subarray that it's sum equals to zero.

Example 1:
    - Input:  [-3, 1, 2, -3, 4]
    - Output: [0, 2] or [1, 3].
    - Explanation: return anyone that the sum is 0.

Example 2:
    - Input:  [-3, 1, -4, 2, -3, 4]
    - Output: [1,5]

Reference:
    - https://algorithm.yuanbin.me/zh-hans/integer_array/zero_sum_subarray.html
    - https://www.lintcode.com/problem/subarray-sum/
"""

import unittest


def subarray_sum(nums):
    """
    Find a subarray where the sum of numbers is zero

    :param nums: given array
    :type nums: list[int]
    :return: the index of the first number and the index of the last number
    :rtype: list[int]
    """
    hash_table = {0: 0}
    curr_sum = 0
    # traverse through array and store prefix sums
    for i in range(len(nums)):
        curr_sum += nums[i]
        # if current sum is stored before, then we find a zero sum subarray
        if curr_sum in hash_table:
            return [hash_table[curr_sum], i]
        else:
            hash_table[curr_sum] = i + 1
    return [0, 0]


class TestSubarraySum(unittest.TestCase):
    def test_subarray_sum(self):
        self.assertIn(subarray_sum([-3, 1, 2, -3, 4]), [[0, 2], [1, 3]])
        self.assertIn(subarray_sum([-3, 1, -4, 2, -3, 4]), [[1, 5], ])


if __name__ == '__main__':
    unittest.main()
