"""
Balanced Binary Tree
--------------------

Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the depth of the two subtrees of every node never
differ by more than 1.

Example 1:
    Given the following tree [3,9,20,null,null,15,7]:
        3
       / \
      9  20
        /  \
       15   7
    Return true.

Example 2:
    Given the following tree [1,2,2,3,3,null,null,4,4]:
           1
          / \
         2   2
        / \
       3   3
      / \
     4   4
    Return false.

Reference:
    - https://algorithm.yuanbin.me/zh-hans/binary_tree/balanced_binary_tree.html
    - https://leetcode.com/problems/balanced-binary-tree/
    - https://www.lintcode.com/problem/balanced-binary-tree/
"""

import unittest
from utils import TreeNode, BinaryTree
import collections


def is_balanced(root):
    """
    Determine whether or not given binary tree is height-balanced

    :param root: root node of given binary tree
    :type root: TreeNode or None
    :return: whether or not given binary tree is height-balanced
    :rtype: bool
    """
    # basic case
    if root is None:
        return True
    left_depth = max_depth(root.left)
    right_depth = max_depth(root.right)
    if abs(left_depth - right_depth) > 1:
        return False
    else:
        return is_balanced(root.left) and is_balanced(root.right)


def max_depth(root):
    """
    Get maximum depth of given tree by BFS

    :param root: root node of given binary tree
    :type root: TreeNode or None
    :return: maximum depth of given tree
    :rtype: int
    """
    # basic case
    if root is None:
        return 0

    # breadth-first traversal
    queue = collections.deque([root])
    depth = 0
    while queue:
        queue_size = len(queue)
        for i in range(queue_size):
            curr = queue.popleft()
            if curr.left is not None:
                queue.append(curr.left)
            if curr.right is not None:
                queue.append(curr.right)
        depth += 1

    return depth


class TestBalancedBinaryTree(unittest.TestCase):
    def test_balanced_binary_tree(self):
        # self.assertTrue(
        #     is_balanced(BinaryTree(val_list=[3, 9, 20, None, None, 15, 7]).root))
        # self.assertFalse(
        #     is_balanced(BinaryTree(val_list=[1, 2, 2, 3, 3, None, None, 4, 4]).root))
        BinaryTree(val_list=[1, 2, 3, 4, 5, None, 6, 7, None, None, None, None, None, None, 8]).print()
        self.assertFalse(
            is_balanced(BinaryTree(val_list=[
                1,
                2, 3,
                4, 5, None, 6,
                7, None, None, None, None, None, None, 8]).root))


if __name__ == '__main__':
    unittest.main()
