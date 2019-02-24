"""
Search in Rotated Sorted Array
------------------------------

Suppose an array sorted in ascending order is rotated at some pivot
unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index,
otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:
    - Input: nums = [4,5,6,7,0,1,2], target = 0
    - Output: 4

Example 2:
    - Input: nums = [4,5,6,7,0,1,2], target = 3
    - Output: -1

Reference:
    - https://algorithm.yuanbin.me/zh-hans/binary_search/search_in_rotated_sorted_array.html
    - https://leetcode.com/problems/search-in-rotated-sorted-array/
    - https://www.lintcode.com/problem/search-in-rotated-sorted-array/
"""

import unittest


def search(nums, target):
    """
    Search in given rotated sorted array

    :param nums: given array
    :type nums: list[int]
    :param target: target number
    :type target: int
    :return: index of target
    :rtype: int
    """
    left = 0
    right = len(nums) - 1
    while left + 1 < right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        # find local sorted array
        elif nums[left] < nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid
            else:
                left = mid
        else:
            if nums[mid] < target <= nums[right]:
                left = mid
            else:
                right = mid

    if left < len(nums) and nums[left] == target:
        return left
    elif right >= 0 and nums[right] == target:
        return right
    else:
        return -1


class TestSearchInRotatedSortedArray(unittest.TestCase):
    def test_search_in_rotated_sorted_array(self):
        self.assertEqual(4, search([4, 5, 6, 7, 0, 1, 2], 0))
        self.assertEqual(-1, search([4, 5, 6, 7, 0, 1, 2], 3))
        self.assertEqual(0, search([1, 3, 5], 1))


if __name__ == '__main__':
    unittest.main()
