"""
Merge Two Sorted Arrays
-----------------------

Merge two given sorted integer array A and B into a new sorted integer array

Example 1:
    - Input:  A=[1], B=[1]
    - Output: [1,1]
    - Explanation: return array merged.

Example 2:
    - Input:  A=[1,2,3,4], B=[2,4,5,6]
    - Output: [1,2,2,3,4,4,5,6]
    - Explanation: return array merged.

Challenge:
    How can you optimize your algorithm if one array is very large and the other is very small?

Reference:
    - https://algorithm.yuanbin.me/zh-hans/integer_array/merge_sorted_array_ii.html
    - https://www.lintcode.com/problem/merge-two-sorted-arrays/
"""

import unittest


def merge(nums1, nums2):
    """
    Merge two given sorted arrays by merge sort

    :param nums1: first array
    :type nums1: list[int]
    :param nums2: second array
    :type nums2: list[int]
    :return: merged array
    :rtype: list[int]
    """
    result = []
    i = j = 0
    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            result.append(nums1[i])
            i += 1
        else:
            result.append(nums2[j])
            j += 1
    while i < len(nums1):
        result.append(nums1[i])
        i += 1
    while j < len(nums2):
        result.append(nums2[j])
        j += 1
    return result


class TestMergeSortedArrayII(unittest.TestCase):
    def test_merge_sorted_array_ii(self):
        self.assertListEqual([1, 1], merge([1], [1]))
        self.assertListEqual([1, 2, 2, 3, 4, 4, 5, 6], merge([1, 2, 3, 4], [2, 4, 5, 6]))


if __name__ == '__main__':
    unittest.main()
