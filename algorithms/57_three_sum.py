"""
Three Sum
---------

Given an array nums of n integers, are there elements a, b, c in nums
such that a + b + c = 0? Find all unique triplets in the array which
gives the sum of zero.

Note:
    The solution set must not contain duplicate triplets.

Example:
    - Given array nums = [-1, 0, 1, 2, -1, -4],
    - A solution set is: [[-1, 0, 1], [-1, -1, 2]]

Reference:
    - https://algorithm.yuanbin.me/zh-hans/integer_array/3_sum.html
    - https://leetcode.com/problems/3sum/
    - https://www.lintcode.com/problem/3sum/description
"""

import unittest


def three_sum(nums):
    """
    Find all unique triplets whose sum is zero in given array

    :param nums: given array
    :type nums: list[int]
    :return: all unique triplets that sum to zero in given array
    :rtype: list[list[int]]
    """
    triplets = []
    if len(nums) >= 3:
        nums.sort()
        for i in range(len(nums)):
            # two sum for target (0 - nums[i])
            hash_table = {}
            target = 0 - nums[i]
            for j in range(i + 1, len(nums)):
                if target - nums[j] in hash_table:
                    triplet = [nums[i], target - nums[j], nums[j]]
                    if triplet not in triplets:
                        triplets.append(triplet)
                hash_table[nums[j]] = j
    return triplets


class TestThreeSum(unittest.TestCase):
    def test_three_sum(self):
        self.assertListEqual(
            [[-1, 0, 1], [-1, -1, 2]],
            three_sum([-1, 0, 1, 2, -1, -4])
        )


if __name__ == '__main__':
    unittest.main()
