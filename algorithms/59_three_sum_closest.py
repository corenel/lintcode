"""
Three Sum Closest
-----------------

Given an array nums of n integers and an integer target, find three integers
in nums such that the sum is closest to target. Return the sum of the three
integers. You may assume that each input would have exactly one solution.

Example:
    - Given array nums = [-1, 2, 1, -4], and target = 1.
    - The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

Reference:
    - https://algorithm.yuanbin.me/zh-hans/integer_array/3_sum_closest.html
    - https://leetcode.com/problems/3sum-closest/
    - https://www.lintcode.com/problem/3sum-closest/
"""

import unittest
import math


def three_sum_closest(nums, target):
    """
    Find a triplet whose sum are closest to target in given array

    :param nums: given array
    :type nums: list[int]
    :param target: target sum
    :type target: int
    :return: the sum of three integers
    :rtype: int
    """
    result = math.inf
    length = len(nums)
    if length < 3:
        return result

    # sort array
    nums.sort()

    # find closest three-sum
    larger_count = 0
    for i in range(length):
        left = i + 1
        right = length - 1
        # check whether or not the smallest sum is larger than target
        if left < right and nums[i] + nums[left] + nums[left + 1] > target:
            larger_count += 1
            # if twice, exit
            if larger_count > 1:
                return result
        # use two pointers to find closest sum to target
        while left < right:
            three_sum = nums[i] + nums[left] + nums[right]
            # get smaller difference to target
            if abs(three_sum - target) < abs(result - target):
                result = three_sum
            # FIXME: flag for previous difference of three_sum and target
            # 0 for initial, -1 for negative, 1 for positive
            prev_diff = 0
            if three_sum > target:
                # move right pointer to get a smaller sum next time
                right -= 1
                # previous value is smaller, now sum is larger, break
                if prev_diff == -1:
                    break
                # current value is larger
                prev_diff = 1
            elif three_sum < target:
                # move left pointer to get a larger sum next time
                left += 1
                # previous value is larger, now sum is smaller, break
                if prev_diff == 1:
                    break
                # current value is smaller
                prev_diff = -1
            else:
                return result

    return result


class TestThreeSumClosest(unittest.TestCase):
    def test_three_sum_closest(self):
        # self.assertEqual(2, three_sum_closest([-1, 2, 1, -4], 1))
        # self.assertEqual(3, three_sum_closest([1, 1, 1, 1], 100))
        self.assertEqual(82, three_sum_closest([1, 2, 4, 8, 16, 32, 64, 128], 82))


if __name__ == '__main__':
    unittest.main()
