"""
Search a 2D Matrix
------------------

Write an efficient algorithm that searches for a value in an m x n matrix.
This matrix has the following properties:

- Integers in each row are sorted from left to right.
- The first integer of each row is greater than the last integer of
  the previous row.

Example 1:
    - Input: matrix = [
      [1,   3,  5,  7],
      [10, 11, 16, 20],
      [23, 30, 34, 50]],
      target = 3
    - Output: true

Example 2:
    - Input: matrix = [
      [1,   3,  5,  7],
      [10, 11, 16, 20],
      [23, 30, 34, 50]],
      target = 13
    - Output: false

Reference:
    - https://algorithm.yuanbin.me/zh-hans/binary_search/search_a_2d_matrix.html
    - https://leetcode.com/problems/search-a-2d-matrix/
    - https://www.lintcode.com/problem/search-a-2d-matrix/description
"""

import unittest


def search_matrix(matrix, target):
    """
    Search target in given 2D matrix

    :param matrix: given matrix
    :type matrix: list[list[int]]
    :param target: target number
    :type target: int
    :return: whether or not target is in given matrix
    :rtype: bool
    """
    m = len(matrix)
    if m == 0:
        return False

    n = len(matrix[-1])
    if n == 0:
        return False

    left = 0
    right = m * n - 1
    while left <= right:
        mid = (left + right) // 2
        mid_2d = convert_index(mid, m, n)
        if matrix[mid_2d[0]][mid_2d[1]] >= target:
            right = mid - 1
        else:
            left = mid + 1
    left_2d = convert_index(left, m, n)
    return 0 <= left < m * n and matrix[left_2d[0]][left_2d[1]] == target


def convert_index(idx, m, n):
    """
    Convert 1D index into 2D

    :param idx: 1D index
    :type idx: int
    :param m: number of rows
    :type m: int
    :param n: number of columns
    :type n: int
    :return: 2D index
    :rtype: tuple[int]
    """
    return idx // n, idx % n


class TestSearchA2DMatrix(unittest.TestCase):
    def test_search_a_2d_matrix(self):
        self.assertTrue(search_matrix(
            [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]],
            3
        ))
        self.assertFalse(search_matrix(
            [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]],
            13
        ))


if __name__ == '__main__':
    unittest.main()
