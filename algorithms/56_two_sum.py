"""
Two Sum
-------

Given an array of integers, return indices of the two numbers
such that they add up to a specific target.

You may assume that each input would have exactly one solution,
and you may not use the same element twice.

Example:
    - Given nums = [2, 7, 11, 15], target = 9,
    - Because nums[0] + nums[1] = 2 + 7 = 9, return [0, 1].

Reference:
    - https://algorithm.yuanbin.me/zh-hans/integer_array/2_sum.html
    - https://leetcode.com/problems/two-sum/
    - https://www.lintcode.com/problem/two-sum/
"""

import unittest


def two_sum(nums, target):
    """
    Given an array of integers, return indices of the two numbers
    such that they add up to a specific target.

    :param nums: given array
    :type nums: list[int]
    :param target: target number
    :type target: int
    :return: indices of two numbers such that they add up to a specific target
    :rtype: list[int]
    """
    hash_table = {}
    for i in range(len(nums)):
        if target - nums[i] in hash_table:
            return [min(i, hash_table[target - nums[i]]),
                    max(i, hash_table[target - nums[i]])]
        hash_table[nums[i]] = i
    return [-1, -1]


class TestTwoSum(unittest.TestCase):
    def test_two_sum(self):
        self.assertListEqual([0, 1], two_sum([2, 7, 11, 15], 9))


if __name__ == '__main__':
    unittest.main()
