"""
Merge Two Sorted Lists
----------------------

Merge two sorted linked lists and return it as a new list.
The new list should be made by splicing together the nodes
of the first two lists.

Example:
    - Input: 1->2->4, 1->3->4
    - Output: 1->1->2->3->4->4

Reference:
    - https://algorithm.yuanbin.me/zh-hans/linked_list/merge_two_sorted_lists.html
    - https://leetcode.com/problems/merge-two-sorted-lists/
    - https://www.lintcode.com/problem/merge-two-sorted-lists/description
"""

from utils import ListNode, LinkedList
from utils.linked_list import generate_linked_list
import unittest


def merge_two_lists(l1, l2):
    """
    Merge two sorted linked lists

    :param l1: head node of first linked list
    :type l1: ListNode
    :param l2: head node of second linked list
    :type l2: ListNode
    :return: head node of merged linked list
    :rtype: ListNode
    """
    dummy = ListNode(None)
    curr = dummy
    while l1 is not None and l2 is not None:
        if l1.val < l2.val:
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l2.next
        curr = curr.next

    # link remaining linked list to current node in the result linked list
    if l1 is not None:
        curr.next = l1
    else:
        curr.next = l2

    return dummy.next


class TestMergeTwoSortedLists(unittest.TestCase):
    def test_merge_two_sorted_lists(self):
        l1 = generate_linked_list([1, 2, 4])
        l2 = generate_linked_list([1, 3, 4])
        head = merge_two_lists(l1.get_head(), l2.get_head())
        l3 = LinkedList(head=head)
        self.assertListEqual([1, 1, 2, 3, 4, 4], l3.to_list())


if __name__ == '__main__':
    unittest.main()
