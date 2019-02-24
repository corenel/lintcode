"""
Search in Rotated Sorted Array II
---------------------------------

Suppose an array sorted in ascending order is rotated at some pivot
unknown to you beforehand.

(i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).

You are given a target value to search. If found in the array return
true, otherwise return false.

Example 1:
    - Input: nums = [2,5,6,0,0,1,2], target = 0
    - Output: true

Example 2:
    - Input: nums = [2,5,6,0,0,1,2], target = 3
    - Output: false

Follow up:
    - This is a follow up problem to Search in Rotated Sorted Array,
      where nums may contain duplicates.
    - Would this affect the run-time complexity? How and why?

Reference:
    - https://algorithm.yuanbin.me/zh-hans/binary_search/search_in_rotated_sorted_array_ii.html
    - https://leetcode.com/problems/search-in-rotated-sorted-array-ii/
    - https://www.lintcode.com/problem/search-in-rotated-sorted-array-ii/
"""

import unittest


def search(nums, target):
    """
    Search in given rotated sorted array

    :param nums: given array
    :type nums: list[int]
    :param target: target number
    :type target: int
    :return:
    :rtype: bool
    """
    left, right = 0, len(nums) - 1

    while left + 1 < right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return True
        elif nums[left] < nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid
            else:
                left = mid
        elif nums[left] > nums[mid]:
            if nums[mid] < target <= nums[right]:
                left = mid
            else:
                right = mid
        else:
            # we cannot determine which side is sorted subarray
            # when nums[left] == nums[mid]
            # so just move left pointer step forward or
            # move right pointer step backward
            left += 1

    if (left < len(nums) and nums[left] == target) or \
            (right >= 0 and nums[right] == target):
        return True
    return False


class TestSearchInRotatedSortedArrayII(unittest.TestCase):
    def test_search_in_rotated_sorted_array_ii(self):
        self.assertTrue(search([2, 5, 6, 0, 0, 1, 2], 0))
        self.assertFalse(search([2, 5, 6, 0, 0, 1, 2], 3))


if __name__ == '__main__':
    unittest.main()
