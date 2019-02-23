"""
Merge Sorted Array
------------------

Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1
as one sorted array.

Note:
    - The number of elements initialized in nums1 and nums2 are m and n
      respectively.
    - You may assume that nums1 has enough space (size that is greater or
      equal to m + n) to hold additional elements from nums2.

Example:
    - Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
    - Output: [1,2,2,3,5,6]

Reference:
    - https://algorithm.yuanbin.me/zh-hans/integer_array/merge_sorted_array.html
    - https://leetcode.com/problems/merge-sorted-array/
    - https://www.lintcode.com/problem/merge-sorted-array/description
"""

import unittest


def merge(nums1, m, nums2, n) -> None:
    """
    Merge two given sorted arrays

    :param nums1: first array
    :type nums1: list[int]
    :param m: length of first array
    :type m: int
    :param nums2: second array
    :type nums2: list[int]
    :param n: length of second array
    :type n: int
    """
    # pointer of the original nums1, from right to left
    i = m - 1
    # pointer of nums2, from right to left
    j = n - 1
    # pointer of nums1, from right to left
    k = m + n - 1

    # merge nums2 into nums1
    while i >= 0 and j >= 0 and k >= 0:
        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1

    # move remaining elements of nums2 to nums1
    while j >= 0:
        nums1[k] = nums2[j]
        k -= 1
        j -= 1


class TestRemoveDuplicatesFromSortedArray(unittest.TestCase):
    def test_remove_duplicates_from_sorted_array(self):
        nums1 = [1, 2, 3, 0, 0, 0]
        m = 3
        nums2 = [2, 5, 6]
        n = 3
        merge(nums1, m, nums2, n)
        self.assertListEqual([1, 2, 2, 3, 5, 6], nums1)


if __name__ == '__main__':
    unittest.main()
