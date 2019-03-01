"""
Linked List

https://algorithm.yuanbin.me/zh-hans/basics_data_structure/linked_list.html
"""

import unittest


class ListNode:

    def __init__(self, val):
        """
        Node for singly linked list

        :param val: value of this node
        :type val: Any
        """
        self.val = val
        self.next = None

    def __repr__(self):
        return 'Node {}'.format(self.val)


class DListNode:
    def __init__(self, val):
        """
        Node of doubly linked list

        :param val: value of this node
        :type val: Any
        """
        self.val = val
        self.next = self.prev = None


class LinkedList:

    def __init__(self, singly=True, head=None):
        """
        Linked list

        :param singly: whether or not this linked list is singly
        :type singly: bool
        :param head: head node
        :type head: ListNode or DListNode
        """
        super().__init__()
        self.singly = singly if head is None else isinstance(head, ListNode)
        self.dummy_head = self.generate_node(None)
        self.curr_node = self.dummy_head
        if head is not None:
            self.append(head)

    def generate_node(self, val):
        """
        Create node with given value

        :param val: given value
        :type val: Any
        :return: node
        :rtype: ListNode or DListNode
        """
        return ListNode(val) if self.singly else DListNode(val)

    def to_list(self):
        """
        Return list of node values

        :return: list of node values
        :rtype: list
        """
        return [node.val for node in self.traverse()]

    def get_head(self):
        """
        Get head node of linked list

        :return: head node
        :rtype: ListNode or DListNode
        """
        head = self.dummy_head.next
        # assert head is not None
        return head

    def set_head(self, head) -> None:
        """
        Set given node as head

        :param head: given node
        :type head: ListNode or DListNode
        """
        self.dummy_head.next = head

    def eliminate_circularity(self):
        """
        Remove circularity of linked list
        """
        curr = self.dummy_head.next
        while curr is not None:
            if curr.next == self.dummy_head.next:
                curr.next = None
                break
            curr = curr.next

    def has_circle(self):
        """
        Check whether or not this linked list has a circle by slow and fast pointer

        :return: whether or not this linked list has a circle
        :rtype: bool
        """
        slow = self.get_head()
        fast = self.get_head()
        while slow is not None and fast is not None:
            slow = slow.next
            fast = fast.next
            if fast is not None:
                fast = fast.next
            if fast == slow:
                return True
        return False

    def append(self, node):
        # initialize dummy head node
        if self.dummy_head.next is None:
            self.dummy_head.next = node
        # set next pointer for current node
        self.curr_node.next = node
        # set prev pointer for new node
        if not self.singly and self.curr_node is not self.dummy_head:
            node.prev = self.curr_node
        # switch current node to the new one
        self.curr_node = node

    def append_val(self, val):
        """
        Append node with given value

        :param val: given value
        :type val: Any
        """
        self.append(self.generate_node(val))

    def append_val_list(self, val_list):
        """
        Append nodes with given value list

        :param val_list: value list
        :type val_list: list
        """
        for val in val_list:
            self.append(self.generate_node(val))

    def remove(self, index):
        """
        Remove item by index

        :param index: index of node to pop
        :type index: int
        """
        assert index >= 0
        if self.singly:
            remove_list_node(curr=self.at(index), prev=self.at(index - 1))
        else:
            remove_list_node(curr=self.at(index), prev=None if index != 0 else self.dummy_head)
        self.eliminate_circularity()

    def reverse(self):
        """
        Reverse linked list

        :return: head node of reversed linked list
        :rtype: Union[ListNode, DListNode]
        """
        head = self.get_head()

        if self.singly:
            prev = None
            while head is not None:
                temp = head.next
                head.next = prev
                prev = head
                head = temp
            self.dummy_head.next = prev
            self.eliminate_circularity()
            return self.get_head()
        else:
            curr = None
            while head is not None:
                curr = head
                head = curr.next
                curr.next = curr.prev
                curr.prev = head
            self.dummy_head.next = curr
            self.eliminate_circularity()
            return self.get_head()

    def traverse(self):
        """
        Traverse linked list

        :return: list of nodes
        :rtype: List
        """
        node_list = []
        head = self.get_head()
        curr = head
        while curr is not None:
            node_list.append(curr)
            curr = curr.next
        return node_list

    def at(self, index):
        """
        Get node by index

        :param index: index of node
        :type index: int
        :return: desired node
        :rtype: ListNode or DListNode
        """
        if index < 0:
            return self.dummy_head

        head = self.get_head()
        curr = head
        cnt = 0
        while curr is not None:
            if cnt == index:
                return curr
            curr = curr.next
            cnt += 1

        raise IndexError

    def find_middle_node(self):
        """
        Find middle node by slow and fast pointer

        :return:
        :rtype:
        """
        slow = self.get_head()
        fast = self.get_head()

        # linked list only has one node
        if fast is not None and fast.next is None:
            return slow

        while slow is not None and fast is not None:
            fast = fast.next
            if fast is not None:
                fast = fast.next
            slow = slow.next

            if fast is not None and fast.next is None:
                break

        return slow

    def __repr__(self):
        return self.to_list()


def remove_list_node(curr, prev=None):
    if isinstance(curr, DListNode):
        if prev is None and curr.prev is not None:
            prev = curr.prev
        if prev is not None:
            prev.next = curr.next
            del curr
    elif isinstance(curr, ListNode) and prev is not None:
        prev.next = curr.next
        del curr
    else:
        raise RuntimeError('Invalid operation to delete node')


def generate_test_linked_list(size=5, singly=False):
    """
    Generate node list for test case

    :param size: size of linked list
    :type size: int
    :param singly: whether or not this linked list is singly
    :type singly: bool
    :return: value list and generated linked list
    """
    assert size >= 1
    val_list = [i for i in range(size)]
    node_list = LinkedList(singly=singly)
    node_list.append_val_list(val_list)

    return val_list, node_list


def generate_linked_list(val_list, singly=True):
    """
    Generate linked list with given values

    :param val_list: given list of values
    :type val_list: list
    :param singly: whether or not linked list is singly
    :type singly: bool
    :return: created linked list
    :rtype: LinkedList
    """
    linked_list = LinkedList(singly=singly)
    linked_list.append_val_list(val_list)
    return linked_list


class TestLinkedList(unittest.TestCase):

    def test_append_linked_list(self):
        val_list, snode_list = generate_test_linked_list(singly=True)
        _, dnode_list = generate_test_linked_list(singly=False)

        for node_list in (snode_list, dnode_list):
            self.assertListEqual(val_list, node_list.to_list())

    def test_reverse_linked_list(self):
        val_list, snode_list = generate_test_linked_list(singly=True)
        _, dnode_list = generate_test_linked_list(singly=False)

        for node_list in (snode_list, dnode_list):
            val_list_reversed = val_list[::-1]
            node_list_reversed = LinkedList(singly=node_list.singly, head=node_list.reverse())
            self.assertListEqual(val_list_reversed, node_list_reversed.to_list())

    def test_remove_node(self):
        original_val_list, snode_list = generate_test_linked_list(singly=True)
        _, dnode_list = generate_test_linked_list(singly=False)

        for node_list in (snode_list, dnode_list):
            val_list = original_val_list[:]
            # test removing node
            val_list.pop(2)
            node_list.remove(2)
            self.assertListEqual(val_list, node_list.to_list())
            # test removing head node
            val_list.pop(0)
            node_list.remove(0)
            self.assertListEqual(val_list, node_list.to_list())
            # test removing tail node
            node_list.remove(len(val_list) - 1)
            val_list.pop(-1)
            self.assertListEqual(val_list, node_list.to_list())
            self.assertEqual(None, node_list.traverse()[-1].next)

    def test_circle_linked_list(self):
        _, snode_list = generate_test_linked_list(singly=True)
        _, dnode_list = generate_test_linked_list(singly=False)

        for node_list in (snode_list, dnode_list):
            # no circle
            self.assertFalse(node_list.has_circle())
            # add circle manually
            node_list.traverse()[-1].next = node_list.get_head()
            self.assertTrue(node_list.has_circle())
            # eliminate circularity
            node_list.eliminate_circularity()
            self.assertFalse(node_list.has_circle())

    def test_find_middle_node(self):
        size_to_test = [1, 5, 10, 11]
        for size in size_to_test:
            val_list, snode_list = generate_test_linked_list(size=size, singly=True)
            _, dnode_list = generate_test_linked_list(size=size, singly=False)

            for node_list in (snode_list, dnode_list):
                self.assertEqual(val_list[len(val_list) // 2],
                                 node_list.find_middle_node().val)


if __name__ == '__main__':
    unittest.main()
