"""
LRU Cache
---------

Design and implement a data structure for Least Recently Used (LRU) cache.
It should support the following operations: get and put.

- get(key) - Get the value (will always be positive) of the key if the key
  exists in the cache, otherwise return -1.
- put(key, value) - Set or insert the value if the key is not already present.
  When the cache reached its capacity, it should invalidate the least recently
  used item before inserting a new item.

Follow up:
    Could you do both operations in O(1) time complexity?

Example:

    - LRUCache cache = new LRUCache( 2 /* capacity */ );
    - cache.put(1, 1);
    - cache.put(2, 2);
    - cache.get(1);       // returns 1
    - cache.put(3, 3);    // evicts key 2
    - cache.get(2);       // returns -1 (not found)
    - cache.put(4, 4);    // evicts key 1
    - cache.get(1);       // returns -1 (not found)
    - cache.get(3);       // returns 3
    - cache.get(4);       // returns 4

Reference:
    - https://algorithm.yuanbin.me/zh-hans/linked_list/lru_cache.html
    - https://leetcode.com/problems/lru-cache/
    - https://leetcode.com/problems/lru-cache/
"""

import unittest
import collections


class Node(object):

    def __init__(self, key, value) -> None:
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache(object):

    def __init__(self, capacity) -> None:
        """
        Least Recently Used (LRU) cache by hash map and doubly linked list

        :param capacity: total capacity of LRU
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = {}
        self.head = Node(key=-1, value=-1)
        self.tail = Node(key=-1, value=-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        """
        Get the value (will always be positive) of the key if the key
        exists in the cache, otherwise return -1

        :param key: key
        :type key: int
        :return: corresponding key
        :rtype: int
        """
        if key not in self.cache:
            return -1

        # remove current node from current position
        curr = self.cache[key]
        curr.prev.next = curr.next
        curr.next.prev = curr.prev

        # move current node to the tail of linked list
        self.move_to_end(curr)

        return self.cache[key].value

    def put(self, key, value) -> None:
        """
        Set or insert the value if the key is not already present

        :param key: key
        :type key: int
        :param value: value
        :type value: int
        """
        if self.get(key) != -1:
            self.cache[key].value = value
            return

        # remove lru
        while len(self.cache) >= self.capacity:
            tmp = self.head.next
            self.cache.pop(tmp.key)
            self.head.next = self.head.next.next
            self.head.next.prev = self.head
            del tmp

        # append new node
        node = Node(key, value)
        self.cache[key] = node
        self.move_to_end(node)

    def move_to_end(self, node):
        """
        Move node to tail

        :param node: given node
        :type node: Node
        """
        node.prev = self.tail.prev
        node.prev.next = node
        self.tail.prev = node
        node.next = self.tail


class LRUCache2(object):

    def __init__(self, capacity):
        """
        Least Recently Used (LRU) cache by ordered list

        :param capacity: total capacity of LRU
        :type capacity: int
        """
        self.cache = collections.OrderedDict()
        self.capacity = capacity

    def get(self, key):
        """
        Get the value (will always be positive) of the key if the key
        exists in the cache, otherwise return -1

        :param key: key
        :type key: int
        :return: corresponding key
        :rtype: int
        """
        if key not in self.cache: return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key, value):
        """
        Set or insert the value if the key is not already present

        :param key: key
        :type key: int
        :param value: value
        :type value: int
        """
        if key in self.cache:
            del self.cache[key]
            self.cache[key] = value
        else:
            while len(self.cache) >= self.capacity:
                self.cache.popitem(False)
            self.cache[key] = value


class TestLRUCache(unittest.TestCase):
    def test_lru_cache(self):
        def assert_operation(lru_cache):
            cache = lru_cache(2)
            cache.put(1, 1)
            cache.put(2, 2)
            # returns 1
            self.assertEqual(1, cache.get(1))
            # evicts key 2
            cache.put(3, 3)
            # returns -1 (not found)
            self.assertEqual(-1, cache.get(2))
            # evicts key 1
            cache.put(4, 4)
            # returns -1 (not found)
            self.assertEqual(-1, cache.get(1))
            # returns 3
            self.assertEqual(3, cache.get(3))
            # returns 4
            self.assertEqual(4, cache.get(4))

        assert_operation(LRUCache)
        assert_operation(LRUCache2)


if __name__ == '__main__':
    unittest.main()
