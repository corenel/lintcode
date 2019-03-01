"""
Task Scheduler
--------------

Given a char array representing tasks CPU need to do. It contains capital
letters A to Z where different letters represent different tasks. Tasks
could be done without original order. Each task could be done in one
interval. For each interval, CPU could finish one task or just be idle.

However, there is a non-negative cooling interval n that means between
two same tasks, there must be at least n intervals that CPU are doing
different tasks or just be idle.

You need to return the least number of intervals the CPU will take to
finish all the given tasks.

Example:
    - Input: tasks = ["A","A","A","B","B","B"], n = 2
    - Output: 8
    - Explanation: A -> B -> idle -> A -> B -> idle -> A -> B.

Note:
    - The number of tasks is in the range [1, 10000].
    - The integer n is in the range [0, 100].

Reference:
    - https://algorithm.yuanbin.me/zh-hans/math_and_bit_manipulation/task_scheduler.html
    - https://leetcode.com/problems/task-scheduler/
    - https://www.lintcode.com/problem/task-scheduler/
"""

import unittest


def least_interval(tasks, n):
    """
    Return the least number of intervals the CPU will take to finish
    all the given tasks

    :param tasks: list of tasks
    :type tasks: list[str]
    :param n: non-negative cooling interval
    :type n: int
    :return: the least number of intervals to finish tasks
    :rtype: int
    """
    # basic case
    if len(tasks) == 0:
        return -1

    # counter for tasks
    coutner = {}
    for task in tasks:
        coutner[task] = coutner.get(task, 0) + 1

    # sort counter by value in descending order
    sorted_counter = sorted(coutner.items(),
                            key=lambda kv: kv[1],
                            reverse=True)

    # compute extra slots for idle
    max_freq: int = sorted_counter[0][1]
    idle_slots = n * (max_freq - 1)
    for task, count in sorted_counter[1:]:
        if count == max_freq:
            idle_slots -= count - 1
        else:
            idle_slots -= count

    return len(tasks) + idle_slots if idle_slots > 0 else len(tasks)


class TestTaskScheduler(unittest.TestCase):
    def test_task_scheduler(self):
        self.assertEqual(
            8,
            least_interval(['A', 'A', 'A', 'B', 'B', 'B'], 2))
        self.assertEqual(
            16,
            least_interval(['A', 'A', 'A', 'A', 'A', 'A',
                            'B', 'C', 'D', 'E', 'F', 'G'], 2))


if __name__ == '__main__':
    unittest.main()
