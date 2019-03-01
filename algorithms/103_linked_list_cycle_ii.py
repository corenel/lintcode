"""
Linked List Cycle II
--------------------

Given a linked list, return the node where the cycle begins. If there is no
cycle, return null.

To represent a cycle in the given linked list, we use an integer pos which
represents the position (0-indexed) in the linked list where tail connects
to. If pos is -1, then there is no cycle in the linked list.

Note: Do not modify the linked list.

Example 1:
    - Input: head = [3,2,0,-4], pos = 1
    - Output: tail connects to node index 1
    - Explanation: There is a cycle in the linked list, where tail connects to the second node.

Example 2:
    - Input: head = [1,2], pos = 0
    - Output: tail connects to node index 0
    - Explanation: There is a cycle in the linked list, where tail connects to the first node.

Example 3:
    - Input: head = [1], pos = -1
    - Output: no cycle
    - Explanation: There is no cycle in the linked list.

Follow up:
    Can you solve it without using extra space?

Reference:
    - https://algorithm.yuanbin.me/zh-hans/linked_list/linked_list_cycle_ii.html
    - https://leetcode.com/problems/linked-list-cycle-ii/
    - https://www.lintcode.com/problem/linked-list-cycle-ii/
"""

from utils import ListNode, LinkedList
from utils.linked_list import generate_linked_list
import unittest


def detect_cycle(head):
    """
    Detect the cycle in given linked list

    :param head: head of first linked list
    :type head: ListNode
    :return: cycle node
    :rtype: ListNode
    """
    if head is None:
        return None

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
            # move fast pointer to head
            # the next time when two pointers meet
            # their position is the cycle node
            fast = head
            slow = slow.next
            while slow != fast:
                fast = fast.next
                slow = slow.next
            return slow
    return None


class TestLinkedListCycle(unittest.TestCase):
    def test_linked_list_cycle(self):
        def assert_operation(val_list, pos=-1):
            linked_list = generate_linked_list(val_list)
            if pos >= 0:
                linked_list.at(len(val_list) - 1).next = linked_list.at(pos)
                self.assertEqual(linked_list.at(pos),
                                 detect_cycle(linked_list.get_head()))
            else:
                self.assertEqual(None,
                                 detect_cycle(linked_list.get_head()))

        assert_operation([3, 2, 0, -4], 1)
        assert_operation([1, 2], 0)
        assert_operation([], -1)
        assert_operation([1], -1)
        assert_operation([1, 2], -1)


if __name__ == '__main__':
    unittest.main()
