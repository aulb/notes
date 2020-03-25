"""
Goal:
- always want the max heap to have more element than the min heap
- adding number to max heap first, then immediately add to min heap
    - this way we are guaranteed to always have the greater half to be on the min heap
    - if we accidentally add too much to min heap, just simply pop the min heap and transfer over to the max heap
"""
# Better implementation, heap max implementation: just use -1 when pushing in
from heapq import *
class MedianFinder:
    def __init__(self):
        """
        initialize your data structure here.
        """
        # small, large => min_heap, max_heap
        # small/min_heap contains the largest half of all the elements
        # large/max_heap contains the smallest half of all the elements
        self.heaps = [], []

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        # Want max_heap to always have more element
        min_heap, max_heap = self.heaps

        """ # what is happening behind the scene
        # push to max_heap
        heappush(max_heap, -num)

        # pop from max_heap
        greatest_from_max_heap = -heappop(max_heap)

        # push to min_heap
        heappush(min_heap, greatest_from_max_heap)

        if len(min_heap) > len(max_heap):
            # get the lowest value from min heap
            lowest_from_min_heap = heappop(min_heap)

            # push to max heap
            heappush(max_heap, -lowest_from_min_heap)
        """
        heappush(max_heap, -heappushpop(min_heap, num))
        if len(max_heap) > len(min_heap):
            heappush(min_heap, -heappop(max_heap))


    def findMedian(self):
        """
        :rtype: float
        """
        min_heap, max_heap = self.heaps
        if not min_heap: return 0.0
        if len(min_heap) > len(max_heap): return float(min_heap[0])
        return (-max_heap[0] + min_heap[0]) / 2
