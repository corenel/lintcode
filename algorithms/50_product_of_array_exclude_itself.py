"""
Product of Array Exclude Itself
------------------------------

Given an integers array A.
Define B[i] = A[0] * ... * A[i-1] * A[i+1] * ... * A[n-1],
calculate B WITHOUT divide operation. Output B

Example 1
    - Input: A = [1, 2, 3]
    - Output: [6, 3, 2]
    - Explanation：B[0] = A[1] * A[2] = 6;
      B[1] = A[0] * A[2] = 3; B[2] = A[0] * A[1] = 2

Example 2
    - Input: A = [2, 4, 6]
    - Output: [24, 12, 8]

Reference:
    - https://algorithm.yuanbin.me/zh-hans/integer_array/product_of_array_exclude_itself.html
    - https://www.lintcode.com/problem/product-of-array-exclude-itself/
"""

import unittest


def product_exclude_itself(nums):
    """
    Compute the product of given array exclude itself

    :param nums: given array
    :type nums: list[int]
    :return: A long long array B and B[i] = A[0] * ... * A[i-1] * A[i+1] * ... * A[n-1]
    :rtype: list[int]
    """
    result = [1] * len(nums)

    # solve the left part (A[0] * ... * A[i-1]) first
    for i in range(1, len(nums)):
        result[i] = result[i - 1] * nums[i - 1]

    # solve the right part (A[i+1] * ... * A[n-1])
    temp = 1
    for i in range(len(nums) - 1, -1, -1):
        result[i] *= temp
        temp *= nums[i]

    return result


class TestProductOfArrayExcludeItself(unittest.TestCase):
    def test_product_of_array_exclude_itself(self):
        self.assertListEqual([6, 3, 2], product_exclude_itself([1, 2, 3]))
        self.assertListEqual([24, 12, 8], product_exclude_itself([2, 4, 6]))


if __name__ == '__main__':
    unittest.main()
