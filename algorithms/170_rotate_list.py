"""
Rotate List
-----------

Given a linked list, rotate the list to the right by k places,
where k is non-negative.

Example 1:
    - Input: 1->2->3->4->5->NULL, k = 2
    - Output: 4->5->1->2->3->NULL
    - Explanation:
        - rotate 1 steps to the right: 5->1->2->3->4->NULL
        - rotate 2 steps to the right: 4->5->1->2->3->NULL

Example 2:
    - Input: 0->1->2->NULL, k = 4
    - Output: 2->0->1->NULL
    - Explanation:
        - rotate 1 steps to the right: 2->0->1->NULL
        - rotate 2 steps to the right: 1->2->0->NULL
        - rotate 3 steps to the right: 0->1->2->NULL
        - rotate 4 steps to the right: 2->0->1->NULL

Reference:
    - https://algorithm.yuanbin.me/zh-hans/linked_list/rotate_list.html
    - https://leetcode.com/problems/rotate-list/
    - https://www.lintcode.com/problem/rotate-list/
"""

from utils import ListNode, LinkedList
from utils.linked_list import generate_linked_list
import unittest


def rotate_right(head, k):
    """
    Rotate the given linked list to the right by k places

    :param head: head node of given linked list
    :type head: ListNode
    :param k: position to rotate
    :type k: int
    :return: head node of rotated linked list
    :rtype: Node
    """
    # basic case
    if head is None:
        return head

    # get length of linked list
    length = 1
    end = head
    while end.next is not None:
        length += 1
        end = end.next

    # get actual k
    k %= length

    # get k-1 node
    node_k_pre = head
    for _ in range(length - k - 1):
        node_k_pre = node_k_pre.next

    # rotate list
    if node_k_pre.next is not None:
        node_k = node_k_pre.next
        node_k_pre.next = None
        end.next = head
    else:
        node_k = head

    return node_k


class TestRotateList(unittest.TestCase):
    def test_rotate_list(self):
        def assert_operation(in_list, k, out_list):
            linked_list = generate_linked_list(in_list)
            head = rotate_right(linked_list.get_head(), k)
            linked_list.set_head(head)
            self.assertListEqual(out_list, linked_list.to_list())

        assert_operation([1, 2, 3, 4, 5], 2, [4, 5, 1, 2, 3])
        assert_operation([0, 1, 2], 4, [2, 0, 1])
        assert_operation([1], 0, [1])
        assert_operation([], 0, [])
        assert_operation([], 1, [])


if __name__ == '__main__':
    unittest.main()
