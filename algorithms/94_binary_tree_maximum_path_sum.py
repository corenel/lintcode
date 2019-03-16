"""
Binary Tree Maximum Path Sum
----------------------------

Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some
starting node to any node in the tree along the parent-child connections.
The path must contain at least one node and does not need to go through
the root.

Example 1:
    - Input: [1,2,3]
           1
          / \
         2   3
    - Output: 6

Example 2:
    - Input: [-10,9,20,null,null,15,7]

       -10
       / \
      9  20
        /  \
       15   7
    - Output: 42

Reference:
    - https://algorithm.yuanbin.me/zh-hans/binary_tree/binary_tree_maximum_path_sum.html
    - https://leetcode.com/problems/binary-tree-maximum-path-sum/
    - https://www.lintcode.com/problem/binary-tree-maximum-path-sum/
"""

import unittest
from utils import TreeNode, BinaryTree
import math


def max_path_sum(root):
    """
    Get maximum path sum of given tree

    :param root: root node of given binary tree
    :type root: TreeNode or None
    :return: maximum path sum
    :rtype: int
    """
    # basic case
    if root is None:
        return 0

    # find maximum path sum
    global result
    result = -math.inf
    dfs(root)

    return result


def dfs(node):
    """
    Helper function to get maximum path sum of given tree

    :param node: root node of given binary tree
    :type node: TreeNode or None
    :return: maximum path sum
    :rtype: int
    """
    if node is None:
        return 0

    # find maximum path sum by comparing existed result
    # and path sum of current node with its children
    global result
    left_path_sum = dfs(node.left)
    right_path_sum = dfs(node.right)
    result = max(
        result,
        max(0, left_path_sum) + node.val + max(0, right_path_sum)
    )

    # return maximum one-side path sum
    return node.val + max(
        max(0, left_path_sum),
        max(0, right_path_sum),
    )


class TestFoo(unittest.TestCase):
    def test_foo(self):
        # self.assertEqual(6, max_path_sum(BinaryTree(val_list=[1, 2, 3]).root))
        self.assertEqual(42, max_path_sum(BinaryTree(val_list=[-10, 9, 20, None, None, 15, 7]).root))


if __name__ == '__main__':
    unittest.main()
