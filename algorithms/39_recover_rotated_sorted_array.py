"""
Recover Rotated Sorted Array
----------------------------

Given a rotated sorted array, recover it to sorted array in-place.

Clarification:
    What is rotated array?
    For example, the orginal array is [1,2,3,4], The rotated array of it
    can be [1,2,3,4], [2,3,4,1], [3,4,1,2], [4,1,2,3]

Example1:
    [4, 5, 1, 2, 3] -> [1, 2, 3, 4, 5]

Example2:
    [6,8,9,1,2] -> [1,2,6,8,9]

Challenge:
    In-place, O(1) extra space and O(n) time.

Reference:
    - https://algorithm.yuanbin.me/zh-hans/integer_array/recover_rotated_sorted_array.html
    - https://www.lintcode.com/problem/recover-rotated-sorted-array/
"""

import unittest


def recover_rotated_sorted_array(nums) -> None:
    """
    recover the given rotated sorted array to sorted array in-place.

    :param nums: given array
    :type nums: list[int]
    """
    # find rotation index
    rotate_idx = -1
    for i in range(len(nums) - 1):
        if nums[i] > nums[i + 1]:
            rotate_idx = i + 1
            break
    else:
        return

    # rotate array
    nums[:rotate_idx] = nums[:rotate_idx][::-1]
    nums[rotate_idx:] = nums[rotate_idx:][::-1]
    nums[::] = nums[::-1]


class TestRecoverRotatedSortedArray(unittest.TestCase):
    def test_recover_rotated_sorted_array(self):
        nums = [4, 5, 1, 2, 3]
        recover_rotated_sorted_array(nums)
        self.assertListEqual([1, 2, 3, 4, 5], nums)

        nums = [6, 8, 9, 1, 2]
        recover_rotated_sorted_array(nums)
        self.assertListEqual([1, 2, 6, 8, 9], nums)

        nums = [1, 2, 3, 4, 5]
        recover_rotated_sorted_array(nums)
        self.assertListEqual([1, 2, 3, 4, 5], nums)


if __name__ == '__main__':
    unittest.main()
