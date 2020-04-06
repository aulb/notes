# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        left, right = [], []
        for index, interval in enumerate(intervals):
            # curr [1,3] newInterval = [4,6]
            if interval[1] < newInterval[0]:
                left.append(interval)
            elif interval[0] > newInterval[1]:
                right.append(interval)
            # [1,3], [2,5]
            else:
                newInterval = [min(newInterval[0], interval[0]), max(newInterval[1], interval[1])]
        return left + [newInterval] + right
