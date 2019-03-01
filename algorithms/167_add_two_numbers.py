"""
Add Two Numbers
---------------

You are given two non-empty linked lists representing two non-negative
integers. The digits are stored in reverse order and each of their nodes
contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except
the number 0 itself.

Example:
    - Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
    - Output: 7 -> 0 -> 8
    - Explanation: 342 + 465 = 807.

Reference:
    - https://algorithm.yuanbin.me/zh-hans/linked_list/add_two_numbers.html
    - https://leetcode.com/problems/add-two-numbers/
    - https://www.lintcode.com/problem/add-two-numbers/description
"""

from utils import ListNode, LinkedList
from utils.linked_list import generate_linked_list
import unittest


def add_two_numbers(l1, l2):
    """
    Add two integers represented in linked lists

    :param l1: head of first linked list
    :type l1: ListNode
    :param l2: head of second linked list
    :type l2: ListNode
    :return: head of result linked list
    :rtype: ListNode
    """
    result_dummy = ListNode(None)
    result = result_dummy
    carry = 0
    while l1 is not None or l2 is not None or carry != 0:
        v1 = l1.val if l1 is not None else 0
        v2 = l2.val if l2 is not None else 0
        val = (v1 + v2 + carry) % 10
        carry = (v1 + v2 + carry) // 10
        result.next = ListNode(val)
        result = result.next
        if l1 is not None:
            l1 = l1.next
        if l2 is not None:
            l2 = l2.next
    return result_dummy.next


class TestPartitionList(unittest.TestCase):
    def test_partition_list(self):
        linked_list_1 = generate_linked_list([2, 4, 3])
        linked_list_2 = generate_linked_list([5, 6, 4])
        head = add_two_numbers(linked_list_1.get_head(),
                               linked_list_2.get_head())
        linked_list_3 = LinkedList(singly=True, head=head)
        self.assertListEqual([7, 0, 8], linked_list_3.to_list())


if __name__ == '__main__':
    unittest.main()
