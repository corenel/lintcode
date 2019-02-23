"""
First Bad Version
-----------------

The code base version is an integer start from 1 to n. One day, someone
committed a bad version in the code case, so it caused this version and
the following versions are all failed in the unit tests. Find the first
bad version.

You can call isBadVersion to help you determine which version is the first
bad one. The details interface can be found in the code's annotation part.

Example:
    - Given n = 5:
        isBadVersion(3) -> false
        isBadVersion(5) -> true
        isBadVersion(4) -> true
    - Here we are 100% sure that the 4th version is the first bad version.

Challenge:
    You should call isBadVersion as few as possible.

Notice:
    Please read the annotation in code area to get the correct way to call
    isBadVersion in different language.

Reference:
    - https://algorithm.yuanbin.me/zh-hans/binary_search/first_bad_version.html
    - https://www.lintcode.com/problem/first-bad-version/

"""

import unittest


class SVNRepo:

    # You can use SVNRepo.isBadVersion(10) to check whether version 10 is a
    # bad version.
    @classmethod
    def isBadVersion(cls, id):
        """
        Run unit tests to check whether version `id` is a bad version
        return true if unit tests passed else false.

        :param id: index of version
        :type id: int
        :return: whether version `id` is a bad version
        :rtype: bool
        """
        pass


def find_first_bad_version(n):
    """
    Find first bas version

    :param n: number of versions
    :type n: int
    :return: first bad version
    :rtype: int
    """
    left = 0
    right = n - 1
    while left <= right:
        mid = left + (right - left) // 2
        if not SVNRepo.isBadVersion(mid):
            left = mid + 1
        else:
            right = mid - 1
    return left


class TestFirstBadVersion(unittest.TestCase):
    def test_first_bad_version(self):
        pass


if __name__ == '__main__':
    unittest.main()
