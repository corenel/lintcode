"""
Kth Largest Element in an Array
-------------------------------

Find the kth largest element in an unsorted array. Note that it is
the kth largest element in the sorted order, not the kth distinct element.

Example 1:
    - Input: [3,2,1,5,6,4] and k = 2
    - Output: 5

Example 2:
    - Input: [3,2,3,1,2,4,5,5,6] and k = 4
    - Output: 4

Note:
    You may assume k is always valid, 1 ≤ k ≤ array's length.

Reference:
    - https://algorithm.yuanbin.me/zh-hans/integer_array/kth_largest_element.html
    - https://leetcode.com/problems/kth-largest-element-in-an-array/
    - https://www.lintcode.com/problem/kth-largest-element/description
"""

import unittest
import heapq


def find_kth_largest_qsort(nums, k):
    """
    Find kth largest element in given array by quick sort

    :param nums: given array
    :type nums: list[int]
    :param k: kth
    :type k: int
    :return: kth-largest element
    :rtype: int
    """
    return kth_largest_element(nums, 0, len(nums) - 1, k - 1)


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
        if nums[j] >= pivot:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]
    nums[i + 1], nums[right] = nums[right], nums[i + 1]

    if i + 1 == k:
        return nums[i + 1]
    elif i + 1 > k:
        return kth_largest_element(nums, left, i, k)
    else:
        return kth_largest_element(nums, i + 2, right, k)


def find_kth_largest_heap(nums, k):
    heap = []
    for n in nums:
        heapq.heappush(heap, n)
        if len(heap) > k:
            heapq.heappop(heap)
    return heap[0]


class TestKthLargestElementInAnArray(unittest.TestCase):
    def test_kth_largest_element_in_an_array_qsort(self):
        self.assertEqual(5, find_kth_largest_qsort([3, 2, 1, 5, 6, 4], 2))
        self.assertEqual(4, find_kth_largest_qsort([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))

    def test_kth_largest_element_in_an_array_heap(self):
        self.assertEqual(5, find_kth_largest_heap([3, 2, 1, 5, 6, 4], 2))
        self.assertEqual(4, find_kth_largest_heap([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))


if __name__ == '__main__':
    unittest.main()
