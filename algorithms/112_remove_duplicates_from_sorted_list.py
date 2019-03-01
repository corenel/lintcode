"""
Remove Duplicates from Sorted List
----------------------------------

Given a sorted linked list, delete all duplicates such that each element
appear only once.

Example 1:
    - Input: 1->1->2
    - Output: 1->2

Example 2:
    - Input: 1->1->2->3->3
    - Output: 1->2->3

Reference:
    - https://algorithm.yuanbin.me/zh-hans/linked_list/remove_duplicates_from_sorted_list.html
    - https://leetcode.com/problems/remove-duplicates-from-sorted-list/
    - https://www.lintcode.com/problem/remove-duplicates-from-sorted-list/
"""

from utils import ListNode, LinkedList
import unittest


def delete_duplicates(head):
    """
    Remove all duplicates in given linked list

    :param head: head node of given linked list
    :type head: ListNode
    :return: head node of operated linked list
    :rtype: ListNode
    """
    if head is None:
        return head

    curr = head
    while curr.next is not None:
        if curr.val == curr.next.val:
            tmp = curr.next.next
            del curr.next
            curr.next = tmp
        else:
            curr = curr.next
    return head


class TestRemoveDuplicatesFromSortedList(unittest.TestCase):
    def test_remove_duplicates_from_sorted_list(self):
        def assert_operation(val_list, result_list):
            linked_list = LinkedList(singly=True)
            linked_list.append_val_list(val_list)
            delete_duplicates(linked_list.get_head())
            self.assertListEqual(result_list, linked_list.to_list())

        assert_operation([], [])
        assert_operation([1, 1, 2], [1, 2])
        assert_operation([1, 1, 2, 3, 3], [1, 2, 3])


if __name__ == '__main__':
    unittest.main()
