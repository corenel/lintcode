"""
Find First and Last Position of Element in Sorted Array
-------------------------------------------------------

Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

"""

import unittest


def search_range(nums, target):
    """
    Find first and last position of target in given array by binary search

    :param nums: given array
    :type nums : list[int]
    :param target: target number
    :type target: int
    :return: first and last position of target
    :rtype: list[int]
    """
    result = [-1, -1]
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        # note that we move right pointer when nums[mid] == target
        # to find the first occurrence of target
        if nums[mid] >= target:
            right = mid - 1
        else:
            left = mid + 1
    if 0 <= left < len(nums) and nums[left] == target:
        result[0] = left

    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        # note that we move left pointer when nums[mid] == target
        # to find the last occurrence of target
        if nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    if 0 <= right < len(nums) and nums[right] == target:
        result[1] = right

    return result


class TestFindFirstAndLastPositionOfElementInSortedArray(unittest.TestCase):
    def test_find_first_and_last_position_of_element_in_sorted_array(self):
        self.assertListEqual([3, 4], search_range([5, 7, 7, 8, 8, 10], 8))
        self.assertListEqual([-1, -1], search_range([5, 7, 7, 8, 8, 10], 6))


if __name__ == '__main__':
    unittest.main()
