"""
Invert Binary Tree
------------------

Invert a binary tree.

Example:
    - Input:
             4
           /   \
          2     7
         / \   / \
        1   3 6   9
    - Output:
             4
           /   \
          7     2
         / \   / \
        9   6 3   1

Trivia:
    - This problem was inspired by this original tweet by Max Howell:
    - Google: 90% of our engineers use the software you wrote (Homebrew), but you can’t invert a binary tree on a whiteboard so f*** off.

Reference:
    - https://algorithm.yuanbin.me/zh-hans/binary_tree/invert_binary_tree.html
    - https://leetcode.com/problems/invert-binary-tree/
"""

import unittest
from utils import TreeNode, BinaryTree
from utils.binary_tree import breadth_first_traverse
from collections import deque


def invert_tree_recursive(root):
    """
    Invert binary tree

    :param root: root node
    :type root: TreeNode
    :return: root node of inverted tree
    :rtype: TreeNode
    """
    # basic case
    if root is None:
        return None

    root.left, root.right = invert_tree_recursive(root.right), invert_tree_recursive(root.left)

    return root


def invert_tree_iterative(root):
    """
    Invert binary tree

    :param root: root node
    :type root: TreeNode
    :return: root node of inverted tree
    :rtype: TreeNode
    """
    # basic case
    if root is None:
        return None

    queue = deque([root])
    while queue:
        curr = queue.popleft()
        curr.left, curr.right = curr.right, curr.left
        if curr.left is not None:
            queue.append(curr.left)
        if curr.right is not None:
            queue.append(curr.right)

    return root


class TestInvertBinaryTree(unittest.TestCase):
    def test_invert_binary_tree_recurive(self):
        tree = BinaryTree(val_list=[4, 2, 7, 1, 3, 6, 9])
        self.assertListEqual([4, 7, 2, 9, 6, 3, 1],
                             [node.val for node in breadth_first_traverse(invert_tree_recursive(tree.root))])

    def test_invert_binary_tree_iterative(self):
        tree = BinaryTree(val_list=[4, 2, 7, 1, 3, 6, 9])
        self.assertListEqual([4, 7, 2, 9, 6, 3, 1],
                             [node.val for node in breadth_first_traverse(invert_tree_iterative(tree.root))])


if __name__ == '__main__':
    unittest.main()
