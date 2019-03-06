"""
Binary Tree Inorder Traversal
-----------------------------

Given a binary tree, return the inorder traversal of its nodes' values.

Example:
    - Input:
        1
         \
          2
         /
        3
    - Output: [1,3,2]

Follow up: Recursive solution is trivial, could you do it iteratively?

Reference:
    - https://algorithm.yuanbin.me/zh-hans/binary_tree/binary_tree_inorder_traversal.html
    - https://leetcode.com/problems/binary-tree-inorder-traversal/
    - https://www.lintcode.com/problem/binary-tree-inorder-traversal/
"""

import unittest

from utils import TreeNode, BinaryTree


def inorder_traversal_recursive(root):
    """
    Return the inorder traversal of nodes' values.

    - Worst Time complexity: O(n)
    - Worst Space complexity: O(n)

    :param root: root node of given binary tree
    :type root: TreeNode or None
    :return: inorder traversal of nodes' values
    :rtype: list[int]
    """
    # basic case
    if root is None:
        return []

    # inorder traversal: left + root + right
    left = inorder_traversal_recursive(root.left)
    right = inorder_traversal_recursive(root.right)

    return left + [root.val] + right


def inorder_traversal_iterative(root):
    """
    Return the inorder traversal of nodes' values.

    - Worst Time complexity: O(n)
    - Worst Space complexity: O(n)

    :param root: root node of given binary tree
    :type root: TreeNode or None
    :return: inorder traversal of nodes' values
    :rtype: list[int]
    """
    # basic case
    if root is None:
        return []

    # use stack to traverse
    result = []
    stack = []
    while root is not None or len(stack) != 0:
        # put left nodes into stack
        if root is not None:
            stack.append(root)
            root = root.left
        # bottom-up to traverse
        else:
            root = stack.pop()
            result.append(root.val)
            root = root.right

    return result


class TestInorderTraversal(unittest.TestCase):
    def test_inorder_traversal(self):
        # 1
        #  \
        #   2
        #  /
        # 3
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.left = TreeNode(3)
        self.assertListEqual([1, 3, 2], inorder_traversal_recursive(root))
        self.assertListEqual([1, 3, 2], inorder_traversal_iterative(root))


if __name__ == '__main__':
    unittest.main()
