"""
Remove Linked List Elements
---------------------------

Remove all elements from a linked list of integers that have value val.

Example:
    - Input:  1->2->6->3->4->5->6, val = 6
    - Output: 1->2->3->4->5

Reference:
    - https://algorithm.yuanbin.me/zh-hans/linked_list/remove_linked_list_elements.html
    - https://leetcode.com/problems/remove-linked-list-elements/
    - https://www.lintcode.com/problem/remove-linked-list-elements/description
"""

from utils import ListNode
from utils.linked_list import generate_linked_list
import unittest


def remove_elements(head, val):
    """
    Remove all elements from a linked list of integers that have value val.

    :param head: head node of given linked list
    :type head: ListNode
    :param val: value to remove
    :type val: int
    :return: head node of removed linked list
    :rtype: ListNode
    """
    # basic case
    if head is None:
        return head

    # dummy head
    dummy = ListNode(None)
    dummy.next = head

    # traverse to remove nodes with given value
    curr = dummy
    while curr is not None:
        while curr.next is not None and curr.next.val == val:
            tmp = curr.next
            curr.next = curr.next.next
            del tmp
        curr = curr.next

    return dummy.next


class TestRemoveElements(unittest.TestCase):
    def test_remove_elements(self):
        def assert_operation(in_list, val, out_list):
            linked_list = generate_linked_list(in_list)
            head = remove_elements(linked_list.get_head(), val)
            linked_list.set_head(head)
            self.assertListEqual(out_list, linked_list.to_list())

        assert_operation([1, 2, 6, 3, 4, 5, 6], 6, [1, 2, 3, 4, 5])
        assert_operation([1, 1], 1, [])


if __name__ == '__main__':
    unittest.main()
