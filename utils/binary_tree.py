"""
Binary Tree

https://algorithm.yuanbin.me/zh-hans/basics_data_structure/binary_tree.html
"""

import unittest

from collections import deque


class TreeNode:

    def __init__(self, val) -> None:
        """
        Node for bianry tree

        :param val: value
        :type val: Any
        """
        self.val = val
        self.left = self.right = None

    def add_child(self, child):
        if self.left is None:
            self.left = child
        elif self.right is None:
            self.right = child
        else:
            raise RuntimeError('Node can only have two children')

    def get_children(self):
        """
        Return existed children

        :return: existed children
        :rtype: list[TreeNode]
        """
        children = [child for child in (self.left, self.right)
                    if child is not None]
        return children

    def __repr__(self):
        return 'Node {}'.format(self.val)


class BinaryTree:

    def __init__(self, root=None) -> None:
        super().__init__()
        self.root = root

    def depth_first_traverse(self, order='preorder'):
        """
        Traverse binary tree by depth first in given order

        :param order: desired order
        :type order: str
        :return: traversed node list
        :rtype: list
        """
        assert order in ['preorder', 'inorder', 'postorder']
        if order == 'preorder':
            return depth_first_traverse_preorder(self.root)
        elif order == 'inorder':
            return depth_first_traverse_inorder(self.root)
        else:
            return depth_first_traverse_postorder(self.root)

    def breadth_first_traverse(self):
        """
        Traverse binary tree by breadth first

        :return: traversed node list
        :rtype: list
        """
        return breadth_first_traverse(self.root)


class BinarySearchTree(BinaryTree):
    def search(self, key):
        """
        Search node with given key in binary search tree

        :param key: key to search
        :type key: Any
        :return: node with given key
        :rtype: TreeNode
        """
        return search_in_bst(self.root, key)

    def insert(self, node) -> None:
        """
        Insert node in the binary search tree

        :param node: node to insert
        :type node: TreeNode
        """
        self.root = insert_in_bst(self.root, node)

    def delete(self, node) -> None:
        """
        Delete node from the binary search tree

        :param node: node to insert
        :type node: TreeNode
        """
        self.root = delete_in_bst(self.root, node)


def depth_first_traverse_preorder(root):
    """
    Traverse a binary tree in preorder

    :param root: root node of the binary tree
    :type root: TreeNode
    :return: traversed list
    :rtype: list[TreeNode]
    """
    node_list = []
    if root is not None:
        node_list.append(root)
        node_list.extend(depth_first_traverse_preorder(root.left))
        node_list.extend(depth_first_traverse_preorder(root.right))

    return node_list


def depth_first_traverse_inorder(root):
    """
    Traverse a binary tree in inorder

    :param root: root node of the binary tree
    :type root: TreeNode
    :return: traversed list
    :rtype: list[TreeNode]
    """
    node_list = []
    if root is not None:
        node_list.extend(depth_first_traverse_inorder(root.left))
        node_list.append(root)
        node_list.extend(depth_first_traverse_inorder(root.right))

    return node_list


def depth_first_traverse_postorder(root):
    """
    Traverse a binary tree in postorder

    :param root: root node of the binary tree
    :type root: TreeNode
    :return: traversed list
    :rtype: list[TreeNode]
    """
    node_list = []
    if root is not None:
        node_list.extend(depth_first_traverse_postorder(root.left))
        node_list.extend(depth_first_traverse_postorder(root.right))
        node_list.append(root)

    return node_list


def breadth_first_traverse(root):
    """
    breadth-first traversal

    :param root: root node of the binary tree
    :type root: TreeNode
    :return: traversed list
    :rtype: list[TreeNode]
    """
    node_list = []
    node_stack = deque([root])
    while node_stack:
        curr = node_stack.popleft()
        node_list.append(curr)
        for child in curr.get_children():
            node_stack.append(child)

    return node_list


def search_in_bst(root, key):
    """
    Search node with given key in the binary search tree

    :param root: root node of the binary search tree
    :type root: TreeNode
    :param key: key to search
    :type key: Any
    :return: node with given key
    :rtype: TreeNode
    """
    if root is None or root.val == key:
        return root
    if root.val < key:
        return search_in_bst(root.right, key)
    else:
        return search_in_bst(root.left, key)


def insert_in_bst(root, node):
    """
    Insert node in the binary search tree

    :param root: root node of the binary search tree
    :type root: TreeNode
    :param node: node to insert
    :type node: TreeNode
    :return: root node
    :rtype: TreeNode
    """
    if root is None:
        root = node
    else:

        if root.val < node.val:
            if root.right is None:
                root.right = node
            else:
                insert_in_bst(root.right, node)
        else:
            if root.left is None:
                root.left = node
            else:
                insert_in_bst(root.left, node)
    return root


def get_min_value_node(root):
    """
    Get node with minimum value in given binary search tree

    :param root: root node of the binary search tree
    :type root: TreeNode
    :return: node with minimum value
    :rtype: TreeNode
    """
    curr = root
    while curr.left is not None:
        curr = curr.left
    return curr


def delete_in_bst(root, node):
    """
    Delete node from the binary search tree

    :param root: root node of the binary search tree
    :type root: TreeNode
    :param node: node to insert
    :type node: TreeNode
    :return: root node of operated binary search tree
    :rtype: TreeNode
    """
    if root is None:
        return root

    if root.val < node.val:
        root.right = delete_in_bst(root.right, node)
    elif root.val > node.val:
        root.left = delete_in_bst(root.left, node)
    else:
        if root.left is None:
            temp = root.right
            del root
            return temp
        elif root.right is None:
            temp = root.left
            del root
            return temp
        else:
            min_node = get_min_value_node(root.right)
            root.val = min_node.val
            root.right = delete_in_bst(root.right, min_node)

    return root


def generate_test_binary_tree():
    """
    Generate a binary tree for test case

    :return: generated binary tree
    :rtype: BinaryTree
    """
    #       0
    #     /  \
    #    1    2
    #   / \   / \
    #  3  4  5   6
    root = TreeNode(0)
    root.add_child(TreeNode(1))
    root.add_child(TreeNode(2))
    root.left.add_child(TreeNode(3))
    root.left.add_child(TreeNode(4))
    root.right.add_child(TreeNode(5))
    root.right.add_child(TreeNode(6))

    return BinaryTree(root)


def generate_test_binary_search_tree():
    """
    Generate a binary search tree for test case

    :return: generated binary tree
    :rtype: BinarySearchTree
    """
    #      50
    #     /  \
    #   30    70
    #   / \   / \
    #  20 40 60 80
    bst = BinarySearchTree()
    bst.insert(TreeNode(50))
    bst.insert(TreeNode(30))
    bst.insert(TreeNode(20))
    bst.insert(TreeNode(40))
    bst.insert(TreeNode(70))
    bst.insert(TreeNode(60))
    bst.insert(TreeNode(80))
    return bst


def to_list(node_list):
    return [node.val for node in node_list if isinstance(node, TreeNode)]


class TestBinaryTree(unittest.TestCase):

    def test_depth_first_traversal_preorder(self):
        bt = generate_test_binary_tree()
        val_list = to_list(bt.depth_first_traverse('preorder'))
        self.assertListEqual([0, 1, 3, 4, 2, 5, 6], val_list)

    def test_depth_first_traversal_inorder(self):
        bt = generate_test_binary_tree()
        val_list = to_list(bt.depth_first_traverse('inorder'))
        self.assertListEqual([3, 1, 4, 0, 5, 2, 6], val_list)

    def test_depth_first_traversal_postorder(self):
        bt = generate_test_binary_tree()
        val_list = to_list(bt.depth_first_traverse('postorder'))
        self.assertListEqual([3, 4, 1, 5, 6, 2, 0], val_list)

    def test_breadth_first_traversal(self):
        bt = generate_test_binary_tree()
        val_list = to_list(bt.breadth_first_traverse())
        self.assertListEqual([0, 1, 2, 3, 4, 5, 6], val_list)

    def test_binary_search_tree_search(self):
        bst = generate_test_binary_search_tree()
        self.assertEqual(20, bst.search(20).val)
        self.assertEqual(50, bst.search(50).val)
        self.assertEqual(80, bst.search(80).val)
        self.assertEqual(None, bst.search(100))

    def test_binary_search_tree_insert(self):
        bst = generate_test_binary_search_tree()
        val_list = to_list(bst.depth_first_traverse('inorder'))
        self.assertListEqual([20, 30, 40, 50, 60, 70, 80], val_list)

    def test_binary_search_tree_delete(self):
        bst = generate_test_binary_search_tree()
        # delete lesf node
        bst.delete(TreeNode(20))
        val_list = to_list(bst.depth_first_traverse('inorder'))
        self.assertListEqual([30, 40, 50, 60, 70, 80], val_list)
        # delete node with two child
        bst.delete(TreeNode(40))
        val_list = to_list(bst.depth_first_traverse('inorder'))
        self.assertListEqual([30, 50, 60, 70, 80], val_list)
        # delete node with two child
        bst.delete(TreeNode(70))
        val_list = to_list(bst.depth_first_traverse('inorder'))
        self.assertListEqual([30, 50, 60, 80], val_list)
        # delete root node
        bst.delete(TreeNode(50))
        val_list = to_list(bst.depth_first_traverse('inorder'))
        self.assertListEqual([30, 60, 80], val_list)


if __name__ == '__main__':
    unittest.main()
