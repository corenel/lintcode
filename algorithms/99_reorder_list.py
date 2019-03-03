"""
Reorder List
------------

Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You may not modify the values in the list's nodes, only nodes itself may be
changed.

Example 1:
    Given 1->2->3->4, reorder it to 1->4->2->3.

Example 2:
    Given 1->2->3->4->5, reorder it to 1->5->2->4->3.

Reference:
    - https://algorithm.yuanbin.me/zh-hans/linked_list/reorder_list.html
    - https://leetcode.com/problems/reorder-list/
    - https://www.lintcode.com/problem/reorder-list/
"""

from utils import ListNode, LinkedList
from utils.linked_list import generate_linked_list
import unittest


def reorder_list(head) -> None:
    """
    Reorder singly list

    :param head: head node of given linked list
    :type head: ListNode
    """
    # basic case
    if head is None:
        return head

    # get node one position ahead from middle node
    slow = head
    fast = head.next
    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next
    curr = slow.next
    slow.next = None

    # reverse the right-half
    prev = None
    while curr is not None:
        tmp = curr.next
        curr.next = prev
        prev = curr
        curr = tmp

    # merge left-half and right-half
    left = head
    right = prev
    while left is not None and right is not None:
        tmp_left = left.next
        left.next = right
        tmp_right = right.next
        right.next = tmp_left
        left = tmp_left
        right = tmp_right


class TestReorderList(unittest.TestCase):
    def test_reorder_list(self):
        def assert_operation(in_list, out_list):
            linked_list = generate_linked_list(in_list)
            reorder_list(linked_list.get_head())
            self.assertListEqual(out_list, linked_list.to_list())

        assert_operation([1, 2, 3, 4], [1, 4, 2, 3])
        assert_operation([1, 2, 3, 4, 5], [1, 5, 2, 4, 3])


if __name__ == '__main__':
    unittest.main()
