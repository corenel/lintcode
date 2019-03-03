"""
Sort List
---------

Sort a linked list in O(n log n) time using constant space complexity.

Example 1:
    - Input: 4->2->1->3
    - Output: 1->2->3->4

Example 2:
    - Input: -1->5->3->4->0
    - Output: -1->0->3->4->5

Reference:
    - https://algorithm.yuanbin.me/zh-hans/linked_list/sort_list.html
    - https://leetcode.com/problems/sort-list/
    - https://www.lintcode.com/problem/sort-list/
"""

from utils import ListNode, LinkedList
from utils.linked_list import generate_linked_list
import unittest


def sort_list(head):
    """
    Sort a linked list in O(n log n) time using constant space complexity

    :param head: head node of given linked list
    :type head: ListNode
    :return: head node of sorted linked list
    :rtype: Node
    """
    if head is None or head.next is None:
        return head

    # get middle node
    mid = find_middle(head)

    # sort right-half
    right_head = sort_list(mid.next)
    # sort left-half
    mid.next = None
    left_head = sort_list(head)

    return merge_list(left_head, right_head)


def find_middle(head):
    """
    Find middle node of given linked list

    :param head: head node of given linked list
    :type head: ListNode
    :return: middle node of given linked list
    :rtype: ListNode
    """
    if head is None or head.next is None:
        return head

    slow = head
    fast = head.next
    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next

    return slow


def merge_list(l1, l2):
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


class TestReverseLinkedListII(unittest.TestCase):
    def test_reverse_linked_list_ii(self):
        def assert_operation(in_list, out_list):
            linked_list = generate_linked_list(in_list)
            head = sort_list(linked_list.get_head())
            linked_list.set_head(head)
            self.assertListEqual(out_list, linked_list.to_list())

        assert_operation([4, 2, 1, 3], [1, 2, 3, 4])
        assert_operation([-1, 5, 3, 4, 0], [-1, 0, 3, 4, 5])


if __name__ == '__main__':
    unittest.main()
