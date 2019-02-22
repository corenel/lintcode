"""
Subarray Sum Closest
--------------------

Given an integer array, find a subarray with sum closest to zero.
Return the indexes of the first number and last number.

Example
    - Given [-3, 1, 1, -3, 5]
    - Return [0, 2], [1, 3], [1, 1], [2, 2] or [0, 4].

Challenge
    O(n log n) time

Reference:
    - https://algorithm.yuanbin.me/zh-hans/integer_array/subarray_sum_closest.html
    - https://www.lintcode.com/problem/subarray-sum-closest/
"""

import unittest
from math import inf


def subarray_sum_closest(nums):
    """
    Find a subarray with sum closest to zero

    :param nums: given array
    :type nums: list[int]
    :return: the indexes of the first number and last number
    :rtype: list[int]
    """
    # compute sum of sub-sequences
    subarray_sum = [(0, 0) for _ in range(len(nums) + 1)]
    for i in range(len(nums)):
        subarray_sum[i + 1] = (subarray_sum[i][0] + nums[i], i + 1)

    # sort sum
    subarray_sum = sorted(subarray_sum)

    # get minimum value of diff
    min_diff = inf
    result = []
    for i in range(len(subarray_sum) - 1):
        if abs(subarray_sum[i][0] - subarray_sum[i + 1][0]) < min_diff:
            min_diff = abs(subarray_sum[i][0] - subarray_sum[i + 1][0])
            result = [min(subarray_sum[i][1], subarray_sum[i + 1][1]),
                      max(subarray_sum[i][1], subarray_sum[i + 1][1]) - 1]

    return result


class TestSubarraySumClosest(unittest.TestCase):
    def test_subarray_sum_closest(self):
        self.assertIn(
            subarray_sum_closest([-3, 1, 1, -3, 5]),
            [[0, 2], [1, 3], [1, 1], [2, 2], [0, 4]]
        )


if __name__ == '__main__':
    unittest.main()
