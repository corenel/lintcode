"""
Rotate Image
------------

You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Note:
    You have to rotate the image in-place, which means you have to modify
    the input 2D matrix directly. DO NOT allocate another 2D matrix and
    do the rotation.

Example 1:
    Given input matrix =
    [
      [1,2,3],
      [4,5,6],
      [7,8,9]
    ],
    rotate the input matrix in-place such that it becomes:
    [
      [7,4,1],
      [8,5,2],
      [9,6,3]
    ]

Example 2:
    Given input matrix =
    [
      [ 5, 1, 9,11],
      [ 2, 4, 8,10],
      [13, 3, 6, 7],
      [15,14,12,16]
    ],
    rotate the input matrix in-place such that it becomes:
    [
      [15,13, 2, 5],
      [14, 3, 4, 1],
      [12, 6, 8, 9],
      [16, 7,10,11]
    ]

Reference:
    - https://leetcode.com/problems/rotate-image/
"""

import unittest


def rotate(matrix) -> None:
    """
    Rotate matrix clockwise

    :param matrix: given matrix
    :type matrix: list[list[int]]
    """
    n = len(matrix)
    for i in range(n // 2):
        for j in range(i, n - 1 - i):
            matrix[j][n - 1 - i], matrix[n - 1 - i][n - 1 - j], matrix[n - 1 - j][i], matrix[i][j] = \
                matrix[i][j], matrix[j][n - 1 - i], matrix[n - 1 - i][n - 1 - j], matrix[n - 1 - j][i]


class TestRotateImage(unittest.TestCase):
    def test_rotate_image_1(self):
        def assert_inplace_operation(in_matrix, out_matrix):
            rotate(in_matrix)
            self.assertListEqual(out_matrix, in_matrix)

        assert_inplace_operation([
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ], [
            [7, 4, 1],
            [8, 5, 2],
            [9, 6, 3]
        ])
        assert_inplace_operation([
            [5, 1, 9, 11],
            [2, 4, 8, 10],
            [13, 3, 6, 7],
            [15, 14, 12, 16]
        ], [
            [15, 13, 2, 5],
            [14, 3, 4, 1],
            [12, 6, 8, 9],
            [16, 7, 10, 11]
        ])

    if __name__ == '__main__':
        unittest.main()
