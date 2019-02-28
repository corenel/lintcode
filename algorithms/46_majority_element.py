"""
Majority Element
----------------

Given an array of size n, find the majority element. The majority element is
the element that appears more than n/2 times.

You may assume that the array is non-empty and the majority element always
exist in the array.

Example 1:
    - Input: [3,2,3]
    - Output: 3

Example 2:
    - Input: [2,2,1,1,1,2,2]
    - Output: 2

Reference:
    - https://algorithm.yuanbin.me/zh-hans/math_and_bit_manipulation/majority_number.html
    - https://www.geeksforgeeks.org/majority-element/
    - https://leetcode.com/problems/majority-element/
    - https://www.lintcode.com/problem/majority-element/
"""

import unittest


def majority_element(nums):
    """
    Find the majority element in given array

    This algorithm loops through each element and maintains a count of
    nums[maj_index]. If the next element is same then increment the count,
    if the next element is not same then decrement the count, and if the
    count reaches 0 then changes the maj_index to the current element and
    set the count again to 1. So, the algorithm gives us  a candidate element.

    :param nums: list[int]
    :type nums: given array of numbers
    :return: the majority element
    :rtype: int
    """
    if len(nums) == 0:
        return -1

    k, count = -1, 0
    for n in nums:
        if count == 0:
            k = n
        if k == n:
            count += 1
        else:
            count -= 1
    return k


class TestMajorityElement(unittest.TestCase):
    def test_majority_element(self):
        self.assertEqual(3, majority_element([3, 2, 3]))
        self.assertEqual(2, majority_element([2, 2, 1, 1, 1, 2, 2]))


if __name__ == '__main__':
    unittest.main()
