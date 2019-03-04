"""
Palindrome Linked List
----------------------

Given a singly linked list, determine if it is a palindrome.

Example 1:
    - Input: 1->2
    - Output: false

Example 2:
    - Input: 1->2->2->1
    - Output: true

Follow up:
    Could you do it in O(n) time and O(1) space?

Reference:
    - https://algorithm.yuanbin.me/zh-hans/linked_list/palindrome_linked_list.html
    - https://www.geeksforgeeks.org/function-to-check-if-a-singly-linked-list-is-palindrome/
    - https://leetcode.com/problems/palindrome-linked-list/
    - https://www.lintcode.com/problem/palindrome-linked-list/description
"""

from utils import ListNode, LinkedList
from utils.linked_list import generate_linked_list
import unittest


def is_palindrome(head):
    """
    Given a singly linked list, determine if it is a palindrome

    :param head: head node of given linked list
    :type head: ListNode
    :return: whether or not given linked list is palindrome
    :rtype: bool
    """
    if head is None or head.next is None:
        return True

    # find middle node
    slow = head
    fast = head.next
    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next

    # reverse right-half of linked list
    curr = slow.next
    slow.next = None
    prev = None
    while curr is not None:
        tmp = curr.next
        curr.next = prev
        prev = curr
        curr = tmp

    # check palindrome
    right_head = prev
    while right_head is not None and head is not None:
        if right_head.val != head.val:
            return False
        right_head = right_head.next
        head = head.next
    return True


class TestPalindromeLinkedList(unittest.TestCase):
    def test_palindrome_linked_list(self):
        def assert_operation(in_list, result):
            linked_list = generate_linked_list(in_list)
            if result:
                self.assertTrue(is_palindrome(linked_list.get_head()))
            else:
                self.assertFalse(is_palindrome(linked_list.get_head()))

        # assert_operation([1, 2], False)
        # assert_operation([1, 2, 2, 1], True)
        # assert_operation([1, 2, 2, 2, 1], True)
        assert_operation([1, 0, 3, 4, 0, 1], False)


if __name__ == '__main__':
    unittest.main()
