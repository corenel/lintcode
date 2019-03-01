"""
Remove Duplicates from Sorted List II
-------------------------------------

Given a sorted linked list, delete all nodes that have duplicate numbers,
leaving only distinct numbers from the original list.

Example 1:
    Input: 1->2->3->3->4->4->5
    Output: 1->2->5

Example 2:
    Input: 1->1->1->2->3
    Output: 2->3

Reference:
    - https://algorithm.yuanbin.me/zh-hans/linked_list/remove_duplicates_from_sorted_list_ii.html
    - https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/
    - https://www.lintcode.com/problem/remove-duplicates-from-sorted-list-ii/
"""

from utils import ListNode, LinkedList
import unittest


def delete_duplicates(head):
    """
    Remove all duplicates in given linked list, leaving only distinct numbers

    :param head: head node of given linked list
    :type head: ListNode
    :return: head node of operated linked list
    :rtype: ListNode
    """
    if head is None:
        return head

    dummy_head = ListNode(None)
    dummy_head.next = head
    curr = dummy_head

    while curr.next is not None and curr.next.next is not None:
        if curr.next.val == curr.next.next.val:
            val = curr.next.val
            while curr.next is not None and curr.next.val == val:
                tmp = curr.next
                curr.next = curr.next.next
                del tmp
        else:
            curr = curr.next

    return dummy_head.next


class TestRemoveDuplicatesFromSortedListII(unittest.TestCase):
    def test_remove_duplicates_from_sorted_list_ii(self):
        def assert_operation(val_list, result_list):
            linked_list = LinkedList(singly=True)
            linked_list.append_val_list(val_list)
            head = delete_duplicates(linked_list.get_head())
            linked_list.set_head(head)
            self.assertListEqual(result_list, linked_list.to_list())

        assert_operation([], [])
        assert_operation([1, 2, 3, 3, 4, 4, 5], [1, 2, 5])
        assert_operation([1, 1, 1, 2, 3], [2, 3])


if __name__ == '__main__':
    unittest.main()
