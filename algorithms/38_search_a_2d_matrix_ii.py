"""
Search a 2D Matrix II
---------------------

Write an efficient algorithm that searches for a value in an m x n matrix.
This matrix has the following properties:

- Integers in each row are sorted in ascending from left to right.
- Integers in each column are sorted in ascending from top to bottom.

Example:
    - Consider the following matrix: [
      [1,   4,  7, 11, 15],
      [2,   5,  8, 12, 19],
      [3,   6,  9, 16, 22],
      [10, 13, 14, 17, 24],
      [18, 21, 23, 26, 30]]
    - Given target = 5, return true.
    - Given target = 20, return false.

Reference:
    - https://algorithm.yuanbin.me/zh-hans/binary_search/search_a_2d_matrix_ii.html
    - https://leetcode.com/problems/search-a-2d-matrix-ii/
    - https://www.lintcode.com/problem/search-a-2d-matrix-ii/description
"""

import unittest


def search_matrix_leetcode(matrix, target):
    """
    Search target in given 2D matrix

    :param matrix: given matrix
    :type matrix: list[list[int]]
    :param target: target number
    :type target: int
    :return: whether or not target is in given matrix
    :rtype: bool
    """
    if len(matrix) == 0 or len(matrix[-1]) == 0:
        return False
    row, col = 0, len(matrix[-1]) - 1
    while row < len(matrix) and col >= 0:
        if matrix[row][col] == target:
            return True
        elif matrix[row][col] < target:
            row += 1
        else:
            col -= 1
    return False


def search_matrix_lintcode(matrix, target):
    """
    Search target in given 2D matrix

    :param matrix: given matrix
    :type matrix: list[list[int]]
    :param target: target number
    :type target: int
    :return: number of occurrences
    :rtype: int
    """
    occur = 0
    if len(matrix) != 0 or len(matrix[-1]) != 0:
        row, col = 0, len(matrix[-1]) - 1
        while row < len(matrix) and col >= 0:
            if matrix[row][col] == target:
                occur += 1
                col -= 1
            elif matrix[row][col] < target:
                row += 1
            else:
                col -= 1
    return occur


class TestSearchA2DMatrixII(unittest.TestCase):
    def test_search_a_2d_matrix_ii_leetcode(self):
        matrix = [
            [1, 4, 7, 11, 15],
            [2, 5, 8, 12, 19],
            [3, 6, 9, 16, 22],
            [10, 13, 14, 17, 24],
            [18, 21, 23, 26, 30]
        ]
        self.assertTrue(search_matrix_leetcode(matrix, 5))
        self.assertFalse(search_matrix_leetcode(matrix, 20))

    def test_search_a_2d_matrix_ii_lintcode(self):
        self.assertEqual(1, search_matrix_lintcode([[3, 4]], 3))
        self.assertEqual(2, search_matrix_lintcode(
            [[1, 3, 5, 7],
             [2, 4, 7, 8],
             [3, 5, 9, 10]],
            3))


if __name__ == '__main__':
    unittest.main()
