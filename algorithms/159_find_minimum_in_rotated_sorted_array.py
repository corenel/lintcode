"""
Find Minimum in Rotated Sorted Array
------------------------------------

Suppose an array sorted in ascending order is rotated at some pivot
unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

You may assume no duplicate exists in the array.

Example 1:
    - Input: [3,4,5,1,2]
    - Output: 1

Example 2:
    - Input: [4,5,6,7,0,1,2]
    - Output: 0

Reference:
    - https://algorithm.yuanbin.me/zh-hans/binary_search/find_minimum_in_rotated_sorted_array.html
    - https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
    - https://www.lintcode.com/problem/find-minimum-in-rotated-sorted-array/
"""

import unittest


def find_min(nums):
    """
    Find minimum element in rotated sorted array

    :param nums: given array
    :type nums: list[int]
    :return: minimum element
    :rtype: int
    """
    left, right = 0, len(nums) - 1
    while left + 1 < right:
        mid = (left + right) // 2
        if nums[mid] < nums[right]:
            right = mid
        else:
            left = mid
    if nums[left] < nums[right]:
        return nums[left]
    else:
        return nums[right]


class TestFindMinimumElementInRotatedSortedArray(unittest.TestCase):
    def test_find_minimum_element_in_rotated_sorted_array(self):
        self.assertEqual(1, find_min([3, 4, 5, 1, 2]))
        self.assertEqual(0, find_min([4, 5, 6, 7, 0, 1, 2]))


if __name__ == '__main__':
    unittest.main()
