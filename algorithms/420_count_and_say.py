"""
Count and Say
-------------

The count-and-say sequence is the sequence of integers with the first five
terms as following:
    1.     1
    2.     11
    3.     21
    4.     1211
    5.     111221
    6.     312211
    1 is read off as "one 1" or 11.
    11 is read off as "two 1s" or 21.
    21 is read off as "one 2, then one 1" or 1211.

Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say
sequence.

Note:
    Each term of the sequence of integers will be represented as a string.

Example 1:
    - Input: 1
    - Output: "1"

Example 2:
    - Input: 4
    - Output: "1211"

Reference:
    - https://algorithm.yuanbin.me/zh-hans/string/count_and_say.html
    - https://leetcode.com/problems/count-and-say/
    - https://www.lintcode.com/problem/count-and-say/
"""

import unittest


def count_and_say(n):
    """
    Count and say

    :param n: number
    :type n: int
    :return: said string
    :rtype: str
    """
    # basic case
    if n == 0:
        return ''
    elif n == 1:
        return '1'

    prev_seq = count_and_say(n - 1)
    curr_seq = ''
    cnt = 1
    for i in range(len(prev_seq)):
        if i + 1 < len(prev_seq) and prev_seq[i] == prev_seq[i + 1]:
            cnt += 1
            continue
        else:
            curr_seq += str(cnt)
            curr_seq += prev_seq[i]
            cnt = 1
    return curr_seq


class TestCountAndSay(unittest.TestCase):
    def test_count_and_say(self):
        self.assertEqual('1', count_and_say(1))
        self.assertEqual('1211', count_and_say(4))


if __name__ == '__main__':
    unittest.main()
