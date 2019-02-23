"""
Remove Duplicates from Sorted Array
-----------------------------------

Given a sorted array nums, remove the duplicates in-place such that
each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by
modifying the input array in-place with O(1) extra memory.

Example 1:
    - Given nums = [1,1,2],
    - Your function should return length = 2, with the first two
      elements of nums being 1 and 2 respectively.
    - It doesn't matter what you leave beyond the returned length.

Example 2:
    - Given nums = [0,0,1,1,1,2,2,3,3,4],
    - Your function should return length = 5, with the first five
    elements of nums being modified to 0, 1, 2, 3, and 4 respectively.
    - It doesn't matter what values are set beyond the returned length.

Clarification:
    Confused why the returned value is an integer but your answer is an array?
    Note that the input array is passed in by reference, which means
    modification to the input array will be known to the caller as well.

Reference:
    - https://algorithm.yuanbin.me/zh-hans/integer_array/remove_duplicates_from_sorted_array.html
    - https://leetcode.com/problems/remove-duplicates-from-sorted-array/
    - https://www.lintcode.com/problem/remove-duplicates-from-sorted-array/
"""

import unittest


def remove_duplicates(nums):
    """
    Remove the duplicates in the given sorted array in-place

    :param nums: given array
    :type nums: list[int]
    :return: new length
    :rtype: int
    """
    if len(nums) <= 1:
        return len(nums)
    new_length = 0
    for i in range(len(nums)):
        if nums[i] != nums[new_length]:
            new_length += 1
            nums[new_length] = nums[i]
    return new_length + 1


class TestRemoveDuplicatesFromSortedArray(unittest.TestCase):
    def test_remove_duplicates_from_sorted_array(self):
        nums = [1, 1, 2]
        self.assertEqual(2, remove_duplicates(nums))
        self.assertListEqual([1, 2], nums[:2])

        nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
        self.assertEqual(5, remove_duplicates(nums))
        self.assertListEqual([0, 1, 2, 3, 4], nums[:5])


if __name__ == '__main__':
    unittest.main()
