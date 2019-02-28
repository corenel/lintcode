"""
Majority Element III
-------------------

Given an array of integers and a number k, the majority number is the number
that occurs more than 1/k of the size of the array.

Note: There is only one majority number in the array.

Example 1:
    - Input: [3,1,2,3,2,3,3,4,4,4] and k=3,
    - Output: 3.

Example 2:
    - Input: [1,1,2] and k=3,
    - Output: 1.

Challenge
    O(n) time and O(k) extra space

Reference:
    - https://algorithm.yuanbin.me/zh-hans/math_and_bit_manipulation/majority_number_iii.html
    - https://www.jiuzhang.com/solutions/majority-number-iii/#tag-highlight-lang-python
    - https://www.lintcode.com/problem/majority-number-iii/
"""

import unittest


def majority_element(nums, k):
    """
    Find the majority elements in given array

    :param nums: list[int]
    :type nums: given array of numbers
    :param k: k for 1/k times
    :type k: int
    :return: the majority elements
    :rtype: list[int]
    """
    if len(nums) == 0:
        return -1
    counter = {}
    max_count = 0
    majority = None
    for n in nums:
        counter[n] = counter.get(n, 0) + 1
        if counter[n] > max_count:
            max_count = counter[n]
            majority = n
    return majority


class TestMajorityElementIII(unittest.TestCase):
    def test_majority_element_iii(self):
        self.assertEqual(3, majority_element([3, 1, 2, 3, 2, 3, 3, 4, 4, 4], 3))
        self.assertEqual(1, majority_element([1, 1, 2], 3))


if __name__ == '__main__':
    unittest.main()
