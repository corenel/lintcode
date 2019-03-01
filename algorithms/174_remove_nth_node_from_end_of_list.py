"""
Remove Nth Node From End of List
--------------------------------

Given a linked list, remove the n-th node from the end of list and return
its head.

Example:
    - Given linked list: 1->2->3->4->5, and n = 2.
    - After removing the second node from the end, the linked list
      becomes 1->2->3->5.

Note:
    Given n will always be valid.

Follow up:
    Could you do this in one pass?

Reference:
    - https://algorithm.yuanbin.me/zh-hans/linked_list/remove_nth_node_from_end_of_list.html
    - https://leetcode.com/problems/remove-nth-node-from-end-of-list/
    - https://www.lintcode.com/problem/remove-nth-node-from-end-of-list/description
"""

from utils import ListNode, LinkedList
from utils.linked_list import generate_linked_list
import unittest


def remove_nth_from_end(head, n):
    """
    Remove the n-th node from the end of list

    :param head: head node of given linked list
    :type head: ListNode
    :param n: order n
    :type n: int
    :return: head node of operated linked list
    :rtype: ListNode
    """
    # basic case
    if head is None:
        return head

    # initialize variables
    dummy = ListNode(None)
    dummy.next = head
    slow = fast = dummy

    # slow pointer is slower than fast pointer by n positions
    count = 0
    while fast.next is not None:
        fast = fast.next
        count += 1
        if count > n:
            slow = slow.next

    # if need to remove node
    if count >= n:
        tmp = slow.next
        slow.next = slow.next.next
        del tmp

    return dummy.next


class TestRemoveNthFromEndOfList(unittest.TestCase):
    def test_remove_nth_from_end_of_list(self):
        linked_list = generate_linked_list([1, 2, 3, 4, 5])

        head = remove_nth_from_end(linked_list.get_head(), 2)
        linked_list.set_head(head)
        self.assertListEqual([1, 2, 3, 5], linked_list.to_list())

        head = remove_nth_from_end(linked_list.get_head(), 1)
        linked_list.set_head(head)
        self.assertListEqual([1, 2, 3], linked_list.to_list())

        head = remove_nth_from_end(linked_list.get_head(), 3)
        linked_list.set_head(head)
        self.assertListEqual([2, 3], linked_list.to_list())


if __name__ == '__main__':
    unittest.main()
