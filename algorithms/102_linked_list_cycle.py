"""
Linked List Cycle
-----------------

Given a linked list, determine if it has a cycle in it.

To represent a cycle in the given linked list, we use an integer pos
which represents the position (0-indexed) in the linked list where tail
connects to. If pos is -1, then there is no cycle in the linked list.

Example 1:
    - Input: head = [3,2,0,-4], pos = 1
    - Output: true
    - Explanation: There is a cycle in the linked list,
      where tail connects to the second node.

Example 2:
    - Input: head = [1,2], pos = 0
    - Output: true
    - Explanation: There is a cycle in the linked list,
      where tail connects to the first node.

Example 3:
    - Input: head = [1], pos = -1
    - Output: false
    - Explanation: There is no cycle in the linked list.

Follow up:
    Can you solve it using O(1) (i.e. constant) memory?

Reference:
    - https://algorithm.yuanbin.me/zh-hans/linked_list/linked_list_cycle.html
    - https://leetcode.com/problems/linked-list-cycle/
    - https://www.lintcode.com/problem/linked-list-cycle/
"""

from utils import ListNode, LinkedList
from utils.linked_list import generate_linked_list
import unittest


def has_cycle(head):
    """
    Determine whether or not given linked list has a cycle

    :param head: head of first linked list
    :type head: ListNode
    :return: whether or not given linked list has a cycle
    :rtype: bool
    """
    if head is None:
        return False
    slow: ListNode = head
    fast: ListNode = head.next
    while fast is not None and fast.next is not None:
        # forward pointers
        fast = fast.next
        if fast.next is not None:
            fast = fast.next
        slow = slow.next
        # check if fast pointer catch up with the slow pointer
        if fast == slow:
            return True
    return False


class TestLinkedListCycle(unittest.TestCase):
    def test_linked_list_cycle(self):
        def assert_operation(val_list, pos=-1):
            linked_list = generate_linked_list(val_list)
            if pos >= 0:
                linked_list.at(len(val_list) - 1).next = linked_list.at(pos)
                self.assertTrue(has_cycle(linked_list.get_head()))
            else:
                self.assertFalse(has_cycle(linked_list.get_head()))

        assert_operation([3, 2, 0, -4], 1)
        assert_operation([1, 2], 0)
        assert_operation([], -1)
        assert_operation([1], -1)
        assert_operation([1, 2], -1)


if __name__ == '__main__':
    unittest.main()
