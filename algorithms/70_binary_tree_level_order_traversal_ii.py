"""
Binary Tree Level Order Traversal II
---------------------------------

Given a binary tree, return the bottom-up level order traversal of
its nodes' values. (ie, from left to right, level by level from leaf
 to root).

For example:
    - Given binary tree [3,9,20,null,null,15,7],
          3
         / \
        9  20
          /  \
         15   7
    - return its level order traversal as:
        [
          [15,7],
          [9,20],
          [3]
        ]

Reference:
    - https://algorithm.yuanbin.me/zh-hans/binary_tree/binary_tree_level_order_traversal_ii.html
    - https://leetcode.com/problems/binary-tree-level-order-traversal-ii/
    - https://www.lintcode.com/problem/binary-tree-level-order-traversal-ii/
"""

import unittest

from utils import TreeNode, BinaryTree
import collections


def level_order_bottom_reverse(root):
    """
    Return the bottom-up level order traversal of nodes' values.

    :param root: root node of given binary tree
    :type root: TreeNode or None
    :return: bottom-up level-order traversal of nodes' values
    :rtype: list[list[int]]
    """
    # basic case
    if root is None:
        return []

    result = []
    queue = collections.deque()
    queue.append(root)
    while len(queue) != 0:
        result_curr_level = []
        queue_size = len(queue)
        for i in range(queue_size):
            curr: TreeNode = queue.pop()
            result_curr_level.append(curr.val)
            if curr.left is not None:
                queue.appendleft(curr.left)
            if curr.right is not None:
                queue.appendleft(curr.right)
        result.append(result_curr_level)

    return result[::-1]


def level_order_bottom_stack(root):
    """
    Return the bottom-up level order traversal of nodes' values.

    :param root: root node of given binary tree
    :type root: TreeNode or None
    :return: bottom-up level-order traversal of nodes' values
    :rtype: list[list[int]]
    """
    # basic case
    if root is None:
        return []

    stack = []
    result = []
    queue = collections.deque()
    queue.append(root)
    while len(queue) != 0:
        result_curr_level = []
        queue_size = len(queue)
        for i in range(queue_size):
            curr: TreeNode = queue.pop()
            result_curr_level.append(curr.val)
            if curr.left is not None:
                queue.appendleft(curr.left)
            if curr.right is not None:
                queue.appendleft(curr.right)
        stack.append(result_curr_level)

    for _ in range(len(stack)):
        result.append(stack.pop())

    return result


class TestLevelOrderTraversal(unittest.TestCase):
    def test_level_order_traversal(self):
        #   3
        #  / \
        # 9  20
        #    / \
        #  15   7
        tree = BinaryTree(val_list=[3, 9, 20, None, None, 15, 7])
        result_list = [
            [15, 7],
            [9, 20],
            [3]
        ]
        self.assertListEqual(
            result_list,
            level_order_bottom_reverse(tree.root))
        self.assertListEqual(
            result_list,
            level_order_bottom_stack(tree.root))


if __name__ == '__main__':
    unittest.main()
