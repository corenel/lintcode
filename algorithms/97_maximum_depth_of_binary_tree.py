"""
Maximum Depth of Binary Tree
----------------------------

Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node
down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:
    - Given binary tree [3,9,20,null,null,15,7],
          3
         / \
        9  20
          /  \
         15   7
    - return its depth = 3.

Reference:
    - https://algorithm.yuanbin.me/zh-hans/binary_tree/maximum_depth_of_binary_tree.html
    - https://leetcode.com/problems/maximum-depth-of-binary-tree/
    - https://www.lintcode.com/problem/maximum-depth-of-binary-tree/
"""

import unittest
from utils import TreeNode, BinaryTree
import collections


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


class TestMaximumDepthOfBinaryTree(unittest.TestCase):
    def test_maximum_depth_of_binary_tree(self):
        self.assertEqual(
            3,
            max_depth(BinaryTree(val_list=[3, 9, 20, None, None, 15, 7]).root))
        self.assertEqual(
            3,
            max_depth(BinaryTree(val_list=[1, 2, 3, 4, None, None, 5]).root))


if __name__ == '__main__':
    unittest.main()
