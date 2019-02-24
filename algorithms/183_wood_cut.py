"""
Wood Cut
--------

Given n pieces of wood with length L[i] (integer array). Cut them into
small pieces to guarantee you could have equal or more than k pieces with
the same length. What is the longest length you can get from the n pieces
of wood? Given L & k, return the maximum length of the small pieces.

Note:
    - You couldn't cut wood into float length.
    - If you couldn't get >= k pieces, return 0.

Example:
    For L=[232, 124, 456], k=7, return 114.

Challenge:
    O(n log Len), where Len is the longest length of the wood.

Reference:
    - https://algorithm.yuanbin.me/zh-hans/binary_search/wood_cut.html
    - https://www.lintcode.com/problem/wood-cut/
"""

import unittest


def wood_cut(l, k):
    """
    Cur woods into k pieces with maximum length

    :param l: list of wood length
    :type l: list[int]
    :param k: number of pieces
    :type k: int
    :return: maximum cut length
    :rtype: int
    """
    if sum(l) < k:
        return 0

    left, right = 1, max(l)
    while left + 1 < right:
        mid = (left + right) // 2
        if sum([length // mid for length in l]) < k:
            right = mid
        else:
            left = mid

    if sum([length // left for length in l]) >= k:
        return left
    else:
        return right


class TestWoodCut(unittest.TestCase):
    def test_wood_cut(self):
        self.assertEqual(114, wood_cut([232, 124, 456], 7))


if __name__ == '__main__':
    unittest.main()
