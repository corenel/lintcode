"""
Binary Tree Preorder Traversal
------------------------------

Given a binary tree, return the preorder traversal of its nodes' values.

Example:
    - Input: [1,null,2,3]
       1
        \
         2
        /
       3
    - Output: [1,2,3]

Follow up: Recursive solution is trivial, could you do it iteratively?

Reference:
    - https://algorithm.yuanbin.me/zh-hans/binary_tree/binary_tree_preorder_traversal.html
    - https://leetcode.com/problems/binary-tree-preorder-traversal/
    - https://www.lintcode.com/problem/binary-tree-preorder-traversal/description
"""

import unittest

from utils import TreeNode, BinaryTree


def preorder_traversal_recursive(root):
    """
    Return the preorder traversal of nodes' values.

    - Worst Time complexity: O(n)
    - Worst Space complexity: O(n)

    :param root: root node of given binary tree
    :type root: TreeNode or None
    :return: preorder traversal of nodes' values
    :rtype: list[int]
    """
    # basic case
    if root is None:
        return []

    # preorder traversal: root + left + right
    left = preorder_traversal_recursive(root.left)
    right = preorder_traversal_recursive(root.right)

    return [root.val] + left + right


def preorder_traversal_iterative(root):
    """
    Return the preorder traversal of nodes' values.

    - Worst Time complexity: O(n)
    - Worst Space complexity: O(n)

    :param root: root node of given binary tree
    :type root: TreeNode or None
    :return: preorder traversal of nodes' values
    :rtype: list[int]
    """
    # basic case
    if root is None:
        return []

    # use stack to traverse
    result = []
    stack = [root]
    while len(stack) != 0:
        root = stack.pop()
        result.append(root.val)
        if root.right is not None:
            stack.append(root.right)
        if root.left is not None:
            stack.append(root.left)

    return result


class TestPreorderTraversal(unittest.TestCase):
    def test_preorder_traversal(self):
        # 1
        #  \
        #   2
        #  /
        # 3
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.left = TreeNode(3)
        self.assertListEqual([1, 2, 3], preorder_traversal_recursive(root))
        self.assertListEqual([1, 2, 3], preorder_traversal_iterative(root))


if __name__ == '__main__':
    unittest.main()
