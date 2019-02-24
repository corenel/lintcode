"""
Find Minimum in Rotated Sorted Array II
---------------------------------------

Suppose an array sorted in ascending order is rotated at some pivot
unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

The array may contain duplicates.

Example 1:
    - Input: [1,3,5]
    - Output: 1

Example 2:
    - Input: [2,2,2,0,1]
    - Output: 0

Note:
    - This is a follow up problem to Find Minimum in Rotated Sorted Array.
    - Would allow duplicates affect the run-time complexity? How and why?

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
        elif nums[mid] > nums[right]:
            left = mid
        else:
            # we cannot determine which side is sorted subarray
            # when nums[left] == nums[mid]
            # so just move right pointer step backward
            right -= 1

    if nums[left] < nums[right]:
        return nums[left]
    else:
        return nums[right]


class TestFindMinimumElementInRotatedSortedArray(unittest.TestCase):
    def test_find_minimum_element_in_rotated_sorted_array(self):
        self.assertEqual(1, find_min([1, 3, 5]))
        self.assertEqual(0, find_min([2, 2, 2, 0, 1]))
        self.assertEqual(1, find_min([1, 3, 3]))


if __name__ == '__main__':
    unittest.main()
