"""
Merge k Sorted Lists
--------------------

Merge k sorted linked lists and return it as one sorted list.
Analyze and describe its complexity.

Example:
    - Input: [1->4->5, 1->3->4, 2->6]
    - Output: 1->1->2->3->4->4->5->6

Reference:
    - https://algorithm.yuanbin.me/zh-hans/linked_list/merge_k_sorted_lists.html
    - https://leetcode.com/problems/merge-k-sorted-lists/
    - https://www.lintcode.com/problem/merge-k-sorted-lists/
"""

from utils import ListNode, LinkedList
from utils.linked_list import generate_linked_list
import unittest


def merge_k_lists(lists):
    """
    Merge k sorted linked lists

    :param lists: list of head nodes of sorted linked lists
    :type lists: list[ListNode]
    :return: head node of merged linked list
    :rtype: ListNode
    """
    if len(lists) == 0:
        return None

    return merge_k_lists_helper(lists, 0, len(lists) - 1)


def merge_k_lists_helper(lists, left, right):
    """
    Helper for merging k sorted linked lists

    :param lists: list of head nodes of sorted linked lists
    :type lists: list[ListNode]
    :param left: left position of linked list to merge
    :type left: int
    :param right: right position of linked list to merge
    :type right: int
    :return: head node of merged linked list
    :rtype: ListNode
    """
    if left >= right:
        return lists[left]
    elif left + 1 == right:
        return merge_two_lists(lists[left], lists[right])

    mid = (left + right) // 2
    left_node = merge_k_lists_helper(lists, left, mid)
    right_node = merge_k_lists_helper(lists, mid + 1, right)

    return merge_two_lists(left_node, right_node)


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
        head = merge_k_lists(
            [generate_linked_list([1, 4, 5]).get_head(),
             generate_linked_list([1, 3, 4]).get_head(),
             generate_linked_list([2, 6]).get_head()])
        result = LinkedList(head=head)
        self.assertListEqual([1, 1, 2, 3, 4, 4, 5, 6], result.to_list())


if __name__ == '__main__':
    unittest.main()
