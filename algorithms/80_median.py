"""
Median
------

Given a unsorted array with integers, find the median of it.

A median is the middle number of the array after it is sorted.

If there are even numbers in the array, return the N/2-th number after sorted.

Example:
    - Given [4, 5, 1, 2, 3], return 3.
    - Given [7, 9, 4, 5], return 5.

Challenge:
    O(n) time.

Reference:
    - https://algorithm.yuanbin.me/zh-hans/integer_array/median.html
    - https://www.lintcode.com/problem/median/description
"""

import unittest


def median(nums):
    """
    Find median of given unsorted array

    :param nums: given array
    :type nums: list[int]
    :return: median
    :rtype: int
    """
    if len(nums) == 0:
        return -1
    return kth_largest_element(nums, 0, len(nums) - 1, (len(nums) - 1) // 2)


def kth_largest_element(nums, left, right, k):
    """
    Find kth largest element in given array (like quick sort)

    :param nums: given array
    :type nums: list[int]
    :param left: left position to begin
    :type left: int
    :param right: right position to end
    :type right: int
    :param k: kth
    :type k: int
    :return: kth-largest element
    :rtype: int
    """
    pivot = nums[right]
    i = left - 1
    for j in range(left, right):
        if nums[j] <= pivot:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]
    nums[i + 1], nums[right] = nums[right], nums[i + 1]

    if i + 1 == k:
        return nums[i + 1]
    elif i + 1 > k:
        return kth_largest_element(nums, left, i, k)
    else:
        return kth_largest_element(nums, i + 2, right, k)


class TestMedian(unittest.TestCase):
    def test_median(self):
        self.assertEqual(3, median([4, 5, 1, 2, 3]))
        self.assertEqual(5, median([7, 9, 4, 5]))


if __name__ == '__main__':
    unittest.main()
