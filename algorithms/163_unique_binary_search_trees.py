"""
Unique Binary Search Trees
--------------------------

Given n, how many structurally unique BST's (binary search trees) that store
values 1 ... n?

Example:
    - Input: 3
    - Output: 5
    - Explanation: Given n = 3, there are a total of 5 unique BST's:

..
    1         3     3      2      1
     \       /     /      / \      \
      3     2     1      1   3      2
     /     /       \                 \
    2     1         2                 3

Reference:
    - https://algorithm.yuanbin.me/zh-hans/math_and_bit_manipulation/unique_binary_search_trees.html
    - https://leetcode.com/problems/unique-binary-search-trees/
    - https://www.lintcode.com/problem/unique-binary-search-trees/
"""

import unittest


def num_trees(n):
    """
    Find number of unique binary search trees of value 1..n

    :param n: number of values
    :type n: int
    :return: number of BSTs
    :rtype: int
    """
    if n < 0:
        return -1

    count = [0] * (n + 1)
    count[0] = 1
    for i in range(1, n + 1):
        for j in range(i):
            # if we use i as thr root node
            # which has count[i] possible unique BSTs
            # then the values in left sub-trees are 1..i-1
            # which has count[i-1] possible unique BSTs
            # and the values in the right sub-trees are i+1..n
            # which has count[n-(i+1)] possible unique BSTs
            # so we have the state transformation equation:
            # count[i] = count[i-1] * count[n-i-1]
            count[i] += count[j] * count[i - j - 1]

    return count[n]


class TestUniqueBinarySearchTrees(unittest.TestCase):
    def test_unique_binary_search_trees(self):
        self.assertEqual(5, num_trees(3))


if __name__ == '__main__':
    unittest.main()
