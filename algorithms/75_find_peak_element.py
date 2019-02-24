"""
Find Peak Element
-----------------

A peak element is an element that is greater than its neighbors.

Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element
and return its index.

The array may contain multiple peaks, in that case return the index to any
one of the peaks is fine.

You may imagine that nums[-1] = nums[n] = -∞.

Example 1:
    - Input: nums = [1,2,3,1]
    - Output: 2
    - Explanation: 3 is a peak element and your function should return
      index number 2.

Example 2:
    - Input: nums = [1,2,1,3,5,6,4]
    - Output: 1 or 5
    - Explanation: Your function can return either index number 1 where
      the peak element is 2, or index number 5 where the peak element is 6.

Note:
    Your solution should be in logarithmic complexity.

Reference:
    - https://algorithm.yuanbin.me/zh-hans/binary_search/find_peak_element.html
    - https://leetcode.com/problems/find-peak-element/
    - https://www.lintcode.com/problem/find-peak-element/description
"""

import unittest


def find_peak_element(nums):
    """
    Find a peak element in given array by binary search

    :param nums: given array
    :type nums: list[int]
    :return: index of peak element
    :rtype: int
    """
    if len(nums) == 0:
        return -1
    left = 0
    right = len(nums) - 1
    while left + 1 < right:
        mid = (left + right) // 2
        # search on larger side
        if nums[mid - 1] > nums[mid]:
            right = mid - 1
        elif nums[mid + 1] > nums[mid]:
            left = mid + 1
        else:
            return mid
    if left < len(nums) and nums[left] > nums[right]:
        return left
    else:
        return right


def find_peak_element_2(nums):
    """
    Find a peak element in given array

    :param nums: given array
    :type nums: list[int]
    :return: index of peak element
    :rtype: int
    """
    return nums.index(max(nums))


class TestFindPeakElement(unittest.TestCase):
    def test_find_peak_element(self):
        self.assertEqual(2, find_peak_element([1, 2, 3, 1]))
        self.assertIn(find_peak_element([1, 2, 1, 3, 5, 6, 4]), [1, 5])

    def test_find_peak_element_2(self):
        self.assertEqual(2, find_peak_element_2([1, 2, 3, 1]))
        self.assertIn(find_peak_element_2([1, 2, 1, 3, 5, 6, 4]), [1, 5])


if __name__ == '__main__':
    unittest.main()
