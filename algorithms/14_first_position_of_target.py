"""
First Position of Target
------------------------

For a given sorted array (ascending order) and a target number, find the first
index of this number in O(log n) time complexity.

If the target number does not exist in the array, return -1.

Example 1:
    - Input:  [1,4,4,5,7,7,8,9,9,10], 1
    - Output: 0
    - Explanation: the first index of  1 is 0.

Example 2:
    - Input: [1, 2, 3, 3, 4, 5, 10], 3
    - Output: 2
    - Explanation: the first index of 3 is 2.

Example 3:
    - Input: [1, 2, 3, 3, 4, 5, 10], 6
    - Output: -1
    - Explanation: Not exist 6 in array.

Challenge:
    If the count of numbers is bigger than 2^32, can your code work properly?

Reference:
    - https://algorithm.yuanbin.me/zh-hans/binary_search/first_position_of_target.html
    - https://www.lintcode.com/problem/first-position-of-target/
"""

import unittest


def binary_search(nums, target):
    """
    Find first position of target in given array by binary search

    :param nums: given array
    :type nums : list[int]
    :param target: target number
    :type target: int
    :return: first position of target
    :rtype: int
    """
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        # note that we move right pointer when nums[mid] == target
        # to find the first occurrence of target
        if nums[mid] >= target:
            right = mid - 1
        else:
            left = mid + 1

    if nums[left] == target:
        return left
    else:
        return -1


class TestFirstPositionOfTarget(unittest.TestCase):
    def test_first_position_of_target(self):
        self.assertEqual(0, binary_search([1, 4, 4, 5, 7, 7, 8, 9, 9, 10], 1))
        self.assertEqual(2, binary_search([1, 2, 3, 3, 4, 5, 10], 3))
        self.assertEqual(-1, binary_search([1, 2, 3, 3, 4, 5, 10], 6))

    if __name__ == '__main__':
        unittest.main()
