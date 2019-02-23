"""
Search Insert Position
----------------------

Given a sorted array and a target value, return the index if the target
is found. If not, return the index where it would be if it were inserted
in order.

You may assume NO duplicates in the array.

Example:
    - [1,3,5,6], 5 → 2
    - [1,3,5,6], 2 → 1
    - [1,3,5,6], 7 → 4
    - [1,3,5,6], 0 → 0

Challenge:
    O(log(n)) time

Reference:
    - https://algorithm.yuanbin.me/zh-hans/binary_search/search_insert_position.html
    - https://www.lintcode.com/problem/search-insert-position/description
"""

import unittest


def search_insert(nums, target):
    """
    Search insert position of target in given array

    :param nums: given array
    :type nums : list[int]
    :param target: target number
    :type target: int
    :return: insert position of target
    :rtype: int
    """
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] >= target:
            right = mid - 1
        else:
            left = mid + 1

    # find first element that not less than target
    if left < len(nums) and nums[left] >= target:
        return left
    else:
        return len(nums)


class TestSearchInsertPosition(unittest.TestCase):
    def test_search_insert_position(self):
        self.assertEqual(2, search_insert([1, 3, 5, 6], 5))
        self.assertEqual(1, search_insert([1, 3, 5, 6], 2))
        self.assertEqual(4, search_insert([1, 3, 5, 6], 7))
        self.assertEqual(0, search_insert([1, 3, 5, 6], 0))


if __name__ == '__main__':
    unittest.main()
