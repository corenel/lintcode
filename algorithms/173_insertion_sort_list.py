"""
Insertion Sort List
-------------------

Sort a linked list using insertion sort.

Algorithm of Insertion Sort:
    - Insertion sort iterates, consuming one input element each repetition,
      and growing a sorted output list.
    - At each iteration, insertion sort removes one element from the input
      data, finds the location it belongs within the sorted list, and inserts
      it there.
    - It repeats until no input elements remain.

Example 1:
    Input: 4->2->1->3
    Output: 1->2->3->4

Example 2:
    Input: -1->5->3->4->0
    Output: -1->0->3->4->5

Reference:
    - https://algorithm.yuanbin.me/zh-hans/linked_list/insertion_sort_list.html
    - https://leetcode.com/problems/insertion-sort-list/
    - https://www.lintcode.com/problem/insertion-sort-list/
"""

from utils import ListNode, LinkedList
from utils.linked_list import generate_linked_list
import unittest


def insertion_sort_list(head):
    """
    Sort a linked list by insertion sort

    :param head: head node of given linked list
    :type head: ListNode
    :return: head node of sorted linked list
    :rtype: ListNode
    """
    dummy = ListNode(None)
    dummy.next = head

    curr = head
    while curr is not None:
        if curr.next is not None and curr.next.val < curr.val:
            # find insertion position
            pre = dummy
            while pre.next is not None and pre.next.val < curr.next.val:
                pre = pre.next
            # insert the next node of curr to the position after node pre
            tmp = pre.next
            pre.next = curr.next
            curr.next = curr.next.next
            pre.next.next = tmp
        else:
            curr = curr.next
    return dummy.next


class TestSortList(unittest.TestCase):
    def test_sort_list(self):
        def assert_operation(in_list, out_list):
            linked_list = generate_linked_list(in_list)
            head = insertion_sort_list(linked_list.get_head())
            linked_list.set_head(head)
            self.assertListEqual(out_list, linked_list.to_list())

        assert_operation([4, 2, 1, 3], [1, 2, 3, 4])
        assert_operation([-1, 5, 3, 4, 0], [-1, 0, 3, 4, 5])


if __name__ == '__main__':
    unittest.main()
