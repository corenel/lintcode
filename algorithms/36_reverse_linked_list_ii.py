"""
Reverse Linked List II
----------------------

Reverse a linked list from position m to n. Do it in one-pass.

Note: 1 ≤ m ≤ n ≤ length of list.

Example:
    - Input: 1->2->3->4->5->NULL, m = 2, n = 4
    - Output: 1->4->3->2->5->NULL

Reference:
    - https://algorithm.yuanbin.me/zh-hans/linked_list/reverse_linked_list_ii.html
    - https://leetcode.com/problems/reverse-linked-list-ii/
    - https://www.lintcode.com/problem/reverse-linked-list-ii/description
"""

from utils import ListNode
from utils.linked_list import generate_linked_list
import unittest


def reverse_between(head, m, n):
    """
    Reverse a linked list from position m to

    :param head: head node of given linked list
    :type head: ListNode
    :param m: beginning position to reverse
    :type m: int
    :param n: ending position to reverse
    :type n: int
    :return: head node of reversed linked list
    :rtype: ListNode
    """
    if head is None or m < 0 or n < 0:
        return head

    dummy = ListNode(None)
    dummy.next = head

    # forward to node m-1
    node_m_pre = dummy
    for _ in range(1, m):
        if node_m_pre is None:
            return None
        node_m_pre = node_m_pre.next
    node_m = node_m_pre.next

    # reverse linkde list in [m, n]
    node_n = node_m
    node_n_post = node_m.next
    for _ in range(m, n):
        if node_n_post is None:
            return None
        tmp = node_n_post.next
        node_n_post.next = node_n
        node_n = node_n_post
        node_n_post = tmp

    # relink node m-1 to current node m (original node n)
    node_m_pre.next = node_n
    # relink current node n (original node m) to node n+1
    node_m.next = node_n_post

    return dummy.next


class TestReverseLinkedList(unittest.TestCase):
    def test_reverse_linked_list_iterative(self):
        linked_list = generate_linked_list([1, 2, 3, 4, 5])
        head = reverse_between(linked_list.get_head(), 2, 4)
        linked_list.set_head(head)
        self.assertListEqual([1, 4, 3, 2, 5], linked_list.to_list())


if __name__ == '__main__':
    unittest.main()
