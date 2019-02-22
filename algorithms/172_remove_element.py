"""
Remove Element
--------------

Given an array nums and a value val, remove all instances of that value
in-place and return the new length.

Do not allocate extra space for another array, you must do this by
modifying the input array in-place with O(1) extra memory.

The order of elements can be changed. It doesn't matter what you leave
beyond the new length.

Example 1:
    - Given nums = [3,2,2,3], val = 3,
    - Your function should return length = 2, with the first two elements
      of nums being 2.
    - It doesn't matter what you leave beyond the returned length.

Example 2:
    - Given nums = [0,1,2,2,3,0,4,2], val = 2,
    - Your function should return length = 5, with the first five elements
      of nums containing 0, 1, 3, 0, and 4.
    - Note that the order of those five elements can be arbitrary.
    - It doesn't matter what values are set beyond the returned length.

Clarification:
    Confused why the returned value is an integer but your answer is an array?
    Note that the input array is passed in by reference, which means modification to the input array will be known to the caller as well.

Reference:
    - https://algorithm.yuanbin.me/zh-hans/integer_array/remove_element.html
    - https://leetcode.com/problems/remove-element/
    - http://www.lintcode.com/en/problem/remove-element/
"""

import unittest
from collections import Counter


def remove_element(nums, val):
    """
    Remove elements with given value in the given array

    :param nums: given array
    :type nums: list[int]
    :param val: given value
    :type val: int
    :return: length of operated array
    :rtype: int
    """
    left = 0
    for num in nums:
        if num != val:
            nums[left] = num
            left += 1
    return left


def remove_element_two_pointers(nums, val):
    """
    Remove elements with given value in the given array

    :param nums: given array
    :type nums: list[int]
    :param val: given value
    :type val: int
    :return: length of operated array
    :rtype: int
    """
    # traverse from left to right
    left = 0
    # traverse from right to left
    right = len(nums) - 1
    while left <= right:
        # if left one is not matched, move forward
        if nums[left] != val:
            left += 1
        # if right one is matched, move backward
        elif nums[right] == val:
            right -= 1
        # replace left matched value with right unmatched one
        else:
            nums[left] = nums[right]
            right -= 1
    return left


class TestRemoveElement(unittest.TestCase):
    def test_remove_element(self):
        nums = [3, 2, 2, 3]
        self.assertEqual(2, remove_element(nums, 3))
        self.assertDictEqual(Counter([2, 2]), Counter(nums[:2]))

        nums = [0, 1, 2, 2, 3, 0, 4, 2]
        self.assertEqual(5, remove_element(nums, 2))
        self.assertDictEqual(Counter([0, 1, 3, 0, 4]), Counter(nums[:5]))

        nums = [0, 4, 4, 0, 4, 4, 4, 0, 2]
        self.assertEqual(4, remove_element(nums, 4))
        self.assertDictEqual(Counter([0, 0, 0, 2]), Counter(nums[:4]))

    def test_remove_element_two_pointer(self):
        nums = [3, 2, 2, 3]
        self.assertEqual(2, remove_element_two_pointers(nums, 3))
        self.assertDictEqual(Counter([2, 2]), Counter(nums[:2]))

        nums = [0, 1, 2, 2, 3, 0, 4, 2]
        self.assertEqual(5, remove_element_two_pointers(nums, 2))
        self.assertDictEqual(Counter([0, 1, 3, 0, 4]), Counter(nums[:5]))

        nums = [0, 4, 4, 0, 4, 4, 4, 0, 2]
        self.assertEqual(4, remove_element_two_pointers(nums, 4))
        self.assertDictEqual(Counter([0, 0, 0, 2]), Counter(nums[:4]))


if __name__ == '__main__':
    unittest.main()
