"""
Partition Array by Odd and Even
-------------------------------

Partition an integers array into odd number first and even number second.

Example:
    Given [1, 2, 3, 4], return [1, 3, 2, 4]

Challenge:
    Do it in-place.

Reference:
    - https://algorithm.yuanbin.me/zh-hans/integer_array/partition_array_by_odd_and_even.html
    - https://www.lintcode.com/problem/partition-array-by-odd-and-even/
"""

import unittest


def partition_array(nums) -> None:
    """
    Partition an integers array into odd number first and even number second

    :param nums: given array
    :type nums: list[int]
    """
    left = 0
    right = len(nums) - 1
    while left < right:
        if nums[left] % 2 == 1:
            left += 1
            continue
        elif nums[right] % 2 == 0:
            right -= 1
            continue
        else:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1


class TestPartitionArrayByOddAndEven(unittest.TestCase):
    def test_partition_array_by_odd_even(self):
        nums = [1, 2, 3, 4]
        partition_array(nums)
        self.assertListEqual([1, 3, 2, 4], nums)


if __name__ == '__main__':
    unittest.main()
