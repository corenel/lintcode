"""
Partition List
--------------

Given a linked list and a value x, partition it such that all nodes less than
x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the
two partitions.

Example:
    - Input: head = 1->4->3->2->5->2, x = 3
    - Output: 1->2->2->4->3->5

Reference:
    - https://algorithm.yuanbin.me/zh-hans/linked_list/partition_list.html
    - https://leetcode.com/problems/partition-list/submissions/
    - https://www.lintcode.com/problem/partition-list/
"""

from utils import ListNode, LinkedList
import unittest


def partition(head, x):
    """
    Partition a given linked list with given number

    :param head: head node of given linked list
    :type head: ListNode
    :param x: given number
    :type x: int
    :return: head node of operated linked list
    :rtype: ListNode
    """
    if head is None:
        return head

    left_dummy = ListNode(None)
    right_dummy = ListNode(None)
    left = left_dummy
    right = right_dummy

    curr = head
    while curr is not None:
        if curr.val < x:
            left.next = curr
            left = left.next
        else:
            right.next = curr
            right = right.next
        curr = curr.next
    right.next = None
    left.next = right_dummy.next

    return left_dummy.next


class TestPartitionList(unittest.TestCase):
    def test_partition_list(self):
        def assert_operation(val_list, x, result_list):
            linked_list = LinkedList(singly=True)
            linked_list.append_val_list(val_list)
            head = partition(linked_list.get_head(), x)
            linked_list.set_head(head)
            self.assertListEqual(result_list, linked_list.to_list())

        # assert_operation([], 0, [])
        assert_operation([1, 4, 3, 2, 5, 2], 3, [1, 2, 2, 4, 3, 5])


if __name__ == '__main__':
    unittest.main()
