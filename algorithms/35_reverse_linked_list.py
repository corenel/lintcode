"""
Reverse Linked List
-------------------

Reverse a singly linked list.

Example:
    Input: 1->2->3->4->5->NULL
    Output: 5->4->3->2->1->NULL

Follow up:
    A linked list can be reversed either iteratively or recursively.
    Could you implement both?

Reference:
    - https://algorithm.yuanbin.me/zh-hans/linked_list/reverse_linked_list.html
    - https://leetcode.com/problems/reverse-linked-list/
    - https://www.lintcode.com/problem/reverse-linked-list/
"""

from utils import ListNode, LinkedList
from utils.linked_list import generate_linked_list
import unittest


def reverse_list_iterative(head):
    """
    Reverse a singly linked list by iterative method

    :param head: head node of given linked list
    :type head: ListNode
    :return: head node of reversed linked list
    :rtype: ListNode
    """
    curr = head
    prev = None
    while curr is not None:
        tmp = curr.next
        curr.next = prev
        prev = curr
        curr = tmp
    return prev


def reverse_list_recursive(head):
    """
    Reverse a singly linked list by recursive method

    :param head: head node of given linked list
    :type head: ListNode
    :return: head node of reversed linked list
    :rtype: ListNode
    """
    if head is None or head.next is None:
        return head

    new_head = reverse_list_recursive(head.next)

    head.next.next = head
    head.next = None

    return new_head


class TestReverseLinkedList(unittest.TestCase):
    def test_reverse_linked_list_iterative(self):
        linked_list = generate_linked_list([1, 2, 3, 4, 5])
        head = reverse_list_iterative(linked_list.get_head())
        linked_list.set_head(head)
        self.assertListEqual([5, 4, 3, 2, 1], linked_list.to_list())

    def test_reverse_linked_list_recursive(self):
        linked_list = generate_linked_list([1, 2, 3, 4, 5])
        head = reverse_list_recursive(linked_list.get_head())
        linked_list.set_head(head)
        self.assertListEqual([5, 4, 3, 2, 1], linked_list.to_list())


if __name__ == '__main__':
    unittest.main()
