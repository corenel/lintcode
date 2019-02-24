"""
Median of Two Sorted Arrays
---------------------------

There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity
should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Example 1:
    - nums1 = [1, 3], nums2 = [2]
    - The median is 2.0

Example 2:
    - nums1 = [1, 2], nums2 = [3, 4]
    - The median is (2 + 3)/2 = 2.5

Reference:
    - https://algorithm.yuanbin.me/zh-hans/binary_search/median_of_two_sorted_arrays.html
    - https://leetcode.com/problems/median-of-two-sorted-arrays/
    - https://www.lintcode.com/problem/median-of-two-sorted-arrays/
"""

import unittest
import math


def find_median_sorted_arrays(nums1, nums2):
    """
    Find median in two sorted arrays

    :param nums1: first array
    :type nums1: list[int]
    :param nums2: second array
    :type nums2: list[int]
    :return: median of teo sorted arrays
    :rtype: float
    """
    m, n = len(nums1), len(nums2)
    if m == 0 or n == 0:
        non_empty_array = nums1 if n == 0 else nums2
        if len(non_empty_array) % 2 == 1:
            # if length is odd, return element of index len // 2
            return non_empty_array[len(non_empty_array) // 2] * 1.0
        else:
            # if length is even, return the average of elements of
            # indices len // 2 and len // 2 - 1
            return (non_empty_array[len(non_empty_array) // 2] +
                    non_empty_array[len(non_empty_array) // 2 - 1]) / 2.0

    if (m + n) % 2 == 1:
        # if total length is odd
        # return the kth largest element where k = (m + n) // 2 + 1
        # note that we need to plus 1 since k starts from 1 instead of 0
        return find_kth_smallest_element(nums1, 0, nums2, 0, (m + n) // 2 + 1)
    else:
        # if total length is odd
        # return the average of kth and (k-1)th smallest elements where k = (m + n) // 2 + 1
        return (find_kth_smallest_element(nums1, 0, nums2, 0, (m + n) // 2) +
                find_kth_smallest_element(nums1, 0, nums2, 0, (m + n) // 2 + 1)) / 2.0


def find_kth_smallest_element(nums1, left1, nums2, left2, k):
    """
    Find k-th smallest element in two sorted array

    :param nums1: first array
    :type nums1: list[int]
    :param left1: left pointer for first array
    :type left1: int
    :param nums2: second array
    :type nums2: list[int]
    :param left2: left pointer for second array
    :type left2: int
    :param k: k
    :type k: int
    :return: k-th largest element
    :rtype: int
    """
    # one pointer is overflow, so we just consider elements in the other array
    if left1 > len(nums1) - 1:
        return nums2[left2 + k - 1]
    if left2 > len(nums2) - 1:
        return nums1[left1 + k - 1]

    # return the 1-th smallest element
    if k == 1:
        return nums1[left1] if nums1[left1] < nums2[left2] else nums2[left2]

    # if nums1[left1 + k // 2 - 1] <= nums2[left2 + k // 2 - 1]
    # then nums1[0]..nums1[left1 + k // 2 + 1] are before the kth element of
    # the merged sorted array, so we move left1 to left1 + k // 2
    key1 = nums1[left1 + k // 2 - 1] if left1 + k // 2 - 1 < len(nums1) else math.inf
    key2 = nums2[left2 + k // 2 - 1] if left2 + k // 2 - 1 < len(nums2) else math.inf
    if key1 > key2:
        return find_kth_smallest_element(nums1, left1, nums2, left2 + k // 2, k - k // 2)
    else:
        return find_kth_smallest_element(nums1, left1 + k // 2, nums2, left2, k - k // 2)


class TestMedianOfTwoSortedArrays(unittest.TestCase):
    def test_median_of_two_sorted_arrays(self):
        self.assertEqual(2.0, find_median_sorted_arrays([1, 3], [2]))
        self.assertEqual(2.5, find_median_sorted_arrays([1, 2], [3, 4]))
        self.assertEqual(3.0, find_median_sorted_arrays([1, 2, 3, 4], [3, 4]))


if __name__ == '__main__':
    unittest.main()
