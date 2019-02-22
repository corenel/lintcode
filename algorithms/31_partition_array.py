"""
Partition Array
---------------

Given an array nums of integers and an int k, partition the array
(i.e move the elements in "nums") such that:

- All elements < k are moved to the left
- All elements >= k are moved to the right

Return the partitioning index, i.e the first index i nums[i] >= k.

Note:
    You should do really partition in array nums instead of just counting
    the numbers of integers smaller than k.
    If all elements in nums are smaller than k, then return nums.length

Example 1:
    - Input: [],9
    - Output: 0

Example 2:
    - Input: [3,2,2,1],2
    - Output:1
    - Explanation: the real array is [1,2,2,3]. So return 1

Challenge:
    Can you partition the array in-place and in O(n)?

Reference:
    - https://algorithm.yuanbin.me/zh-hans/integer_array/partition_array.html
    - https://www.lintcode.com/problem/partition-array/
"""

import unittest


def partition_array(nums, k):
    """
    Partition given array (like quick sort)

    :param nums: given array
    :type nums: list[int]
    :param k: partition value
    :type k: int
    :return: the partitioning index
    :rtype: int
    """
    left = 0
    right = len(nums) - 1
    while left <= right:
        while left <= right and nums[left] < k:
            left += 1
        while left <= right and nums[right] >= k:
            right -= 1
        if left <= right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
    return left


class TestPartitionArray(unittest.TestCase):
    def test_partition_array(self):
        nums = []
        k = 9
        self.assertEqual(0, partition_array(nums, k))
        self.assertListEqual([], nums)

        nums = [3, 2, 2, 1]
        k = 2
        self.assertEqual(1, partition_array(nums, k))
        self.assertListEqual([1, 2, 2, 3], nums)


if __name__ == '__main__':
    unittest.main()
