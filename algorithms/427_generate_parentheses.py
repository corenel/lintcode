"""
Generate Parentheses
--------------------

Given n pairs of parentheses, write a function to generate all
combinations of well-formed parentheses.

For example, given n = 3, a solution set is:
    [
      "((()))",
      "(()())",
      "(())()",
      "()(())",
      "()()()"
    ]

Reference:
    - https://leetcode.com/problems/generate-parentheses/
    - https://www.lintcode.com/problem/generate-parentheses/
"""

import unittest


def generate_parentheses(n):
    """
    Generate parentheses

    :param n: number of pairs of parentheses
    :type n: int
    :return: all combinations of well-formed parentheses
    :rtype: list[int]
    """
    result = []
    helper(n, n, '', result)
    return result


def helper(left, right, path, result) -> None:
    """

    :param left: number of remaining left parenthesis
    :type left: int
    :param right: number of remaining right parenthesis
    :type right: int
    :param path: current combination of parenthesis
    :type path: str
    :param result: result of all combinations
    :type result: list[str]
    """
    if left > right or left < 0 or right < 0:
        pass
    elif left == 0 and right == 0:
        result.append(path)
    else:
        helper(left - 1, right, path + '(', result)
        helper(left, right - 1, path + ')', result)


class TestGenerateParentheses(unittest.TestCase):
    def test_generate_parentheses(self):
        self.assertListEqual(
            [
                '((()))',
                '(()())',
                '(())()',
                '()(())',
                '()()()'
            ],
            generate_parentheses(3)
        )


if __name__ == '__main__':
    unittest.main()
