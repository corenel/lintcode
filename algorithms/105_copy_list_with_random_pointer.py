"""
Copy List with Random Pointer
-----------------------------

A linked list is given such that each node contains an additional random
pointer which could point to any node in the list or null.

Return a deep copy of the list.

Example 1:
    - Input: {"$id":"1","next":{"$id":"2","next":null,"random":{"$ref":"2"},"val":2},"random":{"$ref":"2"},"val":1}
    - Explanation:
        - Node 1's value is 1, both of its next and random pointer points to
          Node 2.
        - Node 2's value is 2, its next pointer points to null and its random
          pointer points to itself.

Note:
    You must return the copy of the given head as a reference to the cloned
    list.

Reference:
    - https://algorithm.yuanbin.me/zh-hans/linked_list/copy_list_with_random_pointer.html
    - https://leetcode.com/problems/copy-list-with-random-pointer/
    - https://www.lintcode.com/problem/copy-list-with-random-pointer/description
"""

from utils import ListNode, LinkedList
from utils.linked_list import generate_linked_list
import unittest


class Node(ListNode):

    def __init__(self, val, next=None, random=None):
        super().__init__(val)
        self.id = id(self)
        self.next = next
        self.random = random

    def __repr__(self):
        return super().__repr__() + ' id {}'.format(self.id)


def copy_random_list(head):
    """
    Copy given linked list containing nodes with random pointer

    :param head: head node of given linked list
    :type head: Node
    :return: head node of copied linked list
    :rtype: Node
    """
    if head is None:
        return head

    # shallow copy node
    # 0 -> new_0 -> 1 -> new_1 ...
    curr = head
    while curr is not None:
        new_node = Node(val=curr.val, next=curr.next, random=curr.random)
        curr.next = new_node
        curr = curr.next.next

    # modify random pointer
    curr = head
    while curr is not None:
        if curr.random is not None:
            curr.next.random = curr.random.next
        curr = curr.next.next

    # separate the original list and the copied linked list
    new_head = head.next
    curr = head
    while curr is not None:
        tmp = curr.next
        curr.next = curr.next.next
        if tmp.next is not None:
            tmp.next = tmp.next.next
        curr = curr.next

    return new_head


class TestCopyListWithRandomPointer(unittest.TestCase):
    def test_copy_list_with_random_pointer(self):
        node_1 = Node(1)
        node_2 = Node(2)
        node_1.next = node_2
        node_1.random = node_2
        node_2.random = node_2

        head_copied = copy_random_list(node_1)
        linked_list = LinkedList(head=head_copied)

        self.assertListEqual([1, 2], linked_list.to_list())
        self.assertIs(head_copied.next, head_copied.random)
        self.assertIs(head_copied.next, head_copied.next.random)


if __name__ == '__main__':
    unittest.main()
