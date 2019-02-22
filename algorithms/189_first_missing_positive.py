"""
First Missing Positive
----------------------

Given an unsorted integer array, find the smallest missing positive integer.

Example 1:
    - Input: [1,2,0]
    - Output: 3

Example 2:
    - Input: [3,4,-1,1]
    - Output: 2

Example 3:
    - Input: [7,8,9,11,12]
    - Output: 1

Note:
    Your algorithm should run in O(n) time and uses constant extra space.

Reference:
    - https://algorithm.yuanbin.me/zh-hans/integer_array/first_missing_positive.html
    - https://leetcode.com/problems/first-missing-positive/
    - https://www.lintcode.com/problem/first-missing-positive/
"""

import unittest


def first_missing_positive(nums):
    """
    Find the smallest missing positive integer in given unsorted array

    :param nums: given array
    :type nums: list[int]
    :return: the smallest missing positive integer
    :rtype: int
    """
    # in-place bucket sort, position i for positive integer i + 1
    for i in range(len(nums)):
        while 0 < nums[i] <= len(nums) and \
                nums[i] != i + 1 and nums[i] != nums[nums[i] - 1]:
            nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
    # find smallest positive integer
    for i in range(len(nums)):
        if nums[i] != i + 1:
            return i + 1
    return len(nums) + 1


class TestFirstMissingPositive(unittest.TestCase):
    def test_first_missing_positive(self):
        self.assertEqual(3, first_missing_positive([1, 2, 0]))
        self.assertEqual(2, first_missing_positive([3, 4, -1, 1]))
        self.assertEqual(1, first_missing_positive([7, 8, 9, 11, 12]))


if __name__ == '__main__':
    unittest.main()
