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
        # new interval at the start
        # new interval at the end
        # new interval in the middle no merge
        # new interval in the middle + merge one or more
        left, right = [], []
        for interval in intervals:
            cStart, cEnd = interval
            # curr [1, 3] new [4, 6]
            if cEnd < newInterval[0]:
                left.append(interval)
            # curr [7, 9] new [4, 6] 
            elif cStart > newInterval[1]:
                right.append(interval)
            # [1,3], [2,5]
            else:
                newInterval = [min(newInterval[0], cStart), max(newInterval[1], cEnd)]
        return left + [newInterval] + right

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        left, right = [], []
        for index, interval in enumerate(intervals):
            start, end = interval
            # We are trying to not care about the shit that doesn't matter
            # If these intervals aren't gonna be merged, why does it matter?
            # end time is lesser than new start time, go to the left
            if end < newInterval[0]:
                left.append(interval)
            # start time is more than the new end time, go to the right
            elif start > newInterval[1]:
                right.append(interval)
            # everything else gets merged
            else:
                newInterval = [min(start, newInterval[0]), max(end, newInterval[1])]
            # Becareful of newInterval, the value gets renewed everytime. 
            # We can clear this up by using a different variable.
        return left + [newInterval] + right