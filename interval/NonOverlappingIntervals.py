class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals: return 0
        # Sorting by end time, why it works:
        end, count = None, 0
        for index, interval in enumerate(sorted(intervals, key=lambda x: x[1])):
            if index == 0: 
                # Assume no interval [2,2] < like this
                end = interval[1]
                continue
            if interval[0] >= end:
                end = interval[1]
            else:
                count += 1
        return count