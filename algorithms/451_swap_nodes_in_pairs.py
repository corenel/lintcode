"""
Swap Nodes in Pairs
-------------------

Given a linked list, swap every two adjacent nodes and return its head.

You may not modify the values in the list's nodes, only nodes itself may
be changed.

Example:
    Given 1->2->3->4, you should return the list as 2->1->4->3.

Reference:
    - https://algorithm.yuanbin.me/zh-hans/linked_list/swap_nodes_in_pairs.html
    - https://leetcode.com/problems/swap-nodes-in-pairs/
    - https://www.lintcode.com/problem/swap-nodes-in-pairs/
"""

from utils import ListNode
from utils.linked_list import generate_linked_list
import unittest


def swap_pairs(head):
    """
    Swap every two adjacent nodes in given linked list

    :param head: head node of given linked list
    :type head: ListNode
    :return: head node of swapped linked list
    :rtype: ListNode
    """
    # basic case
    if head is None:
        return head

    # dummy head
    dummy = ListNode(None)
    dummy.next = head

    # swap pairs
    curr = dummy
    while curr.next is not None and curr.next.next is not None:
        tmp_next = curr.next
        tmp_nnnext = curr.next.next.next
        curr.next = curr.next.next
        curr.next.next = tmp_next
        curr.next.next.next = tmp_nnnext
        curr = curr.next.next

    return dummy.next


class TestSwapNodesInPairs(unittest.TestCase):
    def test_swap_nodes_in_pairs(self):
        def assert_operation(in_list, out_list):
            linked_list = generate_linked_list(in_list)
            head = swap_pairs(linked_list.get_head())
            linked_list.set_head(head)
            self.assertListEqual(out_list, linked_list.to_list())

        assert_operation([1, 2, 3, 4], [2, 1, 4, 3])


if __name__ == '__main__':
    unittest.main()
