"""
Binary Tree

https://algorithm.yuanbin.me/zh-hans/basics_data_structure/binary_tree.html
"""

import unittest

from collections import deque
import functools as fn


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

    def display(self):
        """
        Display binary tree from this node
        """
        lines, _, _, _ = self.display_aux()
        for line in lines:
            print(line)

    def display_aux(self):
        """
        Returns list of strings, width, height,
        and horizontal coordinate of the root.
        """
        # No child.
        if self.right is None and self.left is None:
            line = str(self.val)
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left.display_aux()
            s = str(self.val)
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right.display_aux()
            s = str(self.val)
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left.display_aux()
        right, m, q, y = self.right.display_aux()
        s = str(self.val)
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]

        return lines, n + m + u, max(p, q) + 2, n + u // 2


class BinaryTree:

    def __init__(self, root=None, val_list=None) -> None:
        super().__init__()
        self.root = root
        if val_list is not None:
            self.from_list(val_list)

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

    def from_list_iterative(self, val_list):
        """
        Add nodes from value list

        :param val_list: value list
        :type val_list: list[int]
        """

        n = iter(val_list)
        self.root = TreeNode(next(n))
        fringe = deque([self.root])
        while True:
            head = fringe.popleft()
            try:
                head.left = TreeNode(next(n))
                fringe.append(head.left)
                head.right = TreeNode(next(n))
                fringe.append(head.right)
            except StopIteration:
                break

    def from_list(self, val_list):
        def insert_level_order(arr, root, left, right):
            """
            Function to insert nodes in level order

            :param arr: list of elements
            :type arr: list[int]
            :param root: root node
            :type root: TreeNode
            :param left: left pointer
            :type left: int
            :param right: right pointer
            :type right: int
            :return: root node
            :rtype: TreeNode
            """
            # Base case for recursion
            if left < right and arr[left] is not None:
                temp = TreeNode(arr[left])
                root = temp
                # insert left child
                root.left = insert_level_order(
                    arr, root.left, 2 * left + 1, right)
                # insert right child
                root.right = insert_level_order(
                    arr, root.right, 2 * left + 2, right)
            return root

        self.root = insert_level_order(val_list, self.root, 0, len(val_list))

    def print(self):
        print_binary_tree(
            self.root,
            lambda node: (str(node.val), node.left, node.right))


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


def print_binary_tree(node, node_info=None, inverted=False, is_top=True):
    """
    Print binary tree

    from https://stackoverflow.com/questions/48850446/how-to-print-a-binary-tree-in-as-a-structure-of-nodes-in-python

    :param node: root node
    :type node: TreeNode
    :param node_info: function to extract node info
    :param inverted: whether or not to inverse tree display
    :type inverted: bool
    :param is_top: whether or not given node is root
    :type is_top: bool
    """
    # node value string and sub nodes
    string_value, left_node, right_node = node_info(node)

    string_value_width = len(string_value)

    # recurse to sub nodes to obtain line blocks on left and right
    left_text_block = [] if not left_node \
        else print_binary_tree(left_node, node_info, inverted, False)

    right_text_block = [] if not right_node \
        else print_binary_tree(right_node, node_info, inverted, False)

    # count common and maximum number of sub node lines
    common_lines = min(len(left_text_block), len(right_text_block))
    sub_level_lines = max(len(right_text_block), len(left_text_block))

    # extend lines on shallower side to get same number of lines on both sides
    left_sub_lines = left_text_block + [''] * (sub_level_lines - len(left_text_block))
    right_sub_lines = right_text_block + [''] * (sub_level_lines - len(right_text_block))

    # compute location of value or link bar for all left and right sub nodes
    #   * left node's value ends at line's width
    #   * right node's value starts after initial spaces
    left_line_widths = [len(line) for line in left_sub_lines]
    right_line_indents = [len(line) - len(line.lstrip(' ')) for line in right_sub_lines]

    # top line value locations, will be used to determine position of current node & link bars
    first_left_width = (left_line_widths + [0])[0]
    first_right_indent = (right_line_indents + [0])[0]

    # width of sub node link under node value (i.e. with slashes if any)
    # aims to center link bars under the value if value is wide enough
    #
    # ValueLine:    v     vv    vvvvvv   vvvvv
    # LinkLine:    / \   /  \    /  \     / \
    #
    link_spacing = min(string_value_width, 2 - string_value_width % 2)
    left_link_bar = 1 if left_node else 0
    right_link_bar = 1 if right_node else 0
    min_link_width = left_link_bar + link_spacing + right_link_bar
    value_offset = (string_value_width - link_spacing) // 2

    # find optimal position for right side top node
    #   * must allow room for link bars above and between left and right top nodes
    #   * must not overlap lower level nodes on any given line (allow gap of minSpacing)
    #   * can be offset to the left if lower subNodes of right node
    #     have no overlap with subNodes of left node
    min_spacing = 2
    right_node_position = fn.reduce(lambda r, i: max(r, i[0] + min_spacing + first_right_indent - i[1]), \
                                    zip(left_line_widths, right_line_indents[0:common_lines]), \
                                    first_left_width + min_link_width)

    # extend basic link bars (slashes) with underlines to reach left and right
    # top nodes.
    #
    #        vvvvv
    #       __/ \__
    #      L       R
    #
    link_extra_width = max(0, right_node_position - first_left_width - min_link_width)
    right_link_extra = link_extra_width // 2
    left_link_extra = link_extra_width - right_link_extra

    # build value line taking into account left indent and link bar extension (on left side)
    value_indent = max(0, first_left_width + left_link_extra + left_link_bar - value_offset)
    value_line = " " * max(0, value_indent) + string_value
    slash = '\\' if inverted else '/'
    backslash = '/' if inverted else '\\'
    u_line = '¯' if inverted else '_'

    # build left side of link line
    left_link = '' if not left_node else (' ' * first_left_width + u_line * left_link_extra + slash)

    # build right side of link line (includes blank spaces under top node value)
    right_link_offset = link_spacing + value_offset * (1 - left_link_bar)
    right_link = '' if not right_node else (' ' * right_link_offset + backslash + u_line * right_link_extra)

    # full link line (will be empty if there are no sub nodes)
    link_line = left_link + right_link

    # will need to offset left side lines if right side sub nodes extend beyond left margin
    # can happen if left subtree is shorter (in height) than right side subtree
    left_indent_width = max(0, first_right_indent - right_node_position)
    left_indent = ' ' * left_indent_width
    indented_left_lines = [(left_indent if line else '') + line for line in left_sub_lines]

    # compute distance between left and right sublines based on their value position
    # can be negative if leading spaces need to be removed from right side
    merge_offsets = [len(line) for line in indented_left_lines]
    merge_offsets = [left_indent_width + right_node_position - first_right_indent - w for w in merge_offsets]
    merge_offsets = [p if right_sub_lines[i] else 0 for i, p in enumerate(merge_offsets)]

    # combine left and right lines using computed offsets
    #   * indented left sub lines
    #   * spaces between left and right lines
    #   * right sub line with extra leading blanks removed.
    merged_sub_lines = zip(range(len(merge_offsets)), merge_offsets, indented_left_lines)
    merged_sub_lines = [(i, p, line + (' ' * max(0, p))) for i, p, line in merged_sub_lines]
    merged_sub_lines = [line + right_sub_lines[i][max(0, -p):] for i, p, line in merged_sub_lines]

    # Assemble final result combining
    #  * node value string
    #  * link line (if any)
    #  * merged lines from left and right sub trees (if any)
    tree_lines = [left_indent + value_line] + ([] if not link_line else [left_indent + link_line]) + merged_sub_lines

    # invert final result if requested
    tree_lines = reversed(tree_lines) if inverted and is_top else tree_lines

    # return intermediate tree lines or print final result
    if is_top:
        print('\n'.join(tree_lines))
    else:
        return tree_lines


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
