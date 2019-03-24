"""
Lowest Common Ancestor of a Binary Tree
---------------------------------------

Given the root and two nodes in a Binary Tree. Find the lowest common
ancestor(LCA) of the two nodes.

The lowest common ancestor is the node with largest depth which is the
ancestor of both nodes.

Note: Assume two nodes are exist in tree.

Example 1:
    - Input:  For the following binary tree（only one node）:
        1
    - LCA(1,1) = 1

Example 2:
    - Input:  For the following binary tree:
          4
         / \
        3   7
           / \
          5   6

    - LCA(3, 5) = `4`
    - LCA(5, 6) = `7`
    - LCA(6, 7) = `7`

Reference:
    - https://algorithm.yuanbin.me/zh-hans/binary_tree/lowest_common_ancestor.html
    - https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
    - https://www.lintcode.com/problem/lowest-common-ancestor-of-a-binary-tree/
"""

import unittest
from utils import TreeNode, BinaryTree
from enum import IntEnum


class NodeState(IntEnum):
    BOTH_PENDING = 0
    LEFT_DONE = 1
    BOTH_DONE = 2


def lowest_common_ancestor(root, p, q):
    """
    Find the least common ancestor(LCA) of the two nodes.

    :param root: root node of given binary tree
    :type root: TreeNode or None
    :param p: a node in a binary tree
    :type p: TreeNode
    :param q: a node in a binary tree
    :type q: TreeNode
    :return: the least common ancestor(LCA) of the two nodes.
    :rtype: TreeNode
    """
    if p == q:
        return p

    stack = [(root, NodeState.BOTH_PENDING)]
    lca_idx = -1
    match_counter = 0
    while len(stack) > 0:
        parent_node, parent_state = stack[-1]
        if parent_state != NodeState.BOTH_DONE:
            if parent_state == NodeState.BOTH_PENDING:
                if parent_node == p or parent_node == q:
                    if match_counter == 1:
                        return stack[lca_idx][0]
                    else:
                        match_counter += 1
                        lca_idx = len(stack) - 1
                child_node = parent_node.left
            else:
                child_node = parent_node.right
            stack.pop()
            stack.append((parent_node, NodeState(parent_state + 1)))
            if child_node is not None:
                stack.append((child_node, NodeState.BOTH_PENDING))
        else:
            if match_counter == 1 and lca_idx == len(stack) - 1:
                lca_idx -= 1
            stack.pop()
    return stack[lca_idx][0]


class TestLowestCommonAncestor(unittest.TestCase):
    def test_lowest_common_ancestor(self):
        tree = BinaryTree(val_list=[1])
        self.assertEqual(
            tree.root,
            lowest_common_ancestor(
                tree.root, tree.root, tree.root))

        tree = BinaryTree(val_list=[4, 3, 7, None, None, 5, 6])
        self.assertEqual(
            tree.root,
            lowest_common_ancestor(tree.root, tree.root.left, tree.root.right.left)
        )
        self.assertEqual(
            tree.root.right,
            lowest_common_ancestor(tree.root,
                                   tree.root.right.left,
                                   tree.root.right.right)
        )
        self.assertEqual(
            tree.root.right,
            lowest_common_ancestor(tree.root,
                                   tree.root.right.right,
                                   tree.root.right)
        )
        self.assertEqual(
            tree.root.right,
            lowest_common_ancestor(tree.root,
                                   tree.root.right,
                                   tree.root.right)
        )


if __name__ == '__main__':
    unittest.main()
