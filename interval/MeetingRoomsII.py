# Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

# For example,

# Given [[0, 30],[5, 10],[15, 20]],
# return 2.

# Naive: Sort by end date. Get all the non overlapping sets. Runtime: O(n^2)

# Solution by: https://www.programcreek.com/2014/05/leetcode-meeting-rooms-ii-java/
# Modified to my style. Basically use min heap.
# public int minMeetingRooms(int[][] intervals) {
#   Arrays.sort(intervals, Comparator.comparing((int[] itv) -> itv[0]));
#   if (size(intervals) < 1) return 0;

#   PriorityQueue<Integer> heap = new PriorityQueue<>();
#   heap.offer(intervals[0][1]);
#   int count = 1;
#   for (let i = 1; i < intervals.length;i++) {
#     if (itv[0] >= heap.peek()) {
#       heap.poll();
#     } else {
#       count++;
#     }
#     heap.offer(itv[1]);
#   }

#   return count;
# }
from queue import PriorityQueue

class Solution:
    def minMeetingRooms(self, intervals: List)-> int:
        if not intervals: return 0
        pq = PriorityQueue()
        pq.put(intervals[0][1])
        for i in range(1, len(intervals)):
            interval = intervals[i]
            # Top recorded endtime is more than incoming start time
            # Add a meeting room, otherwise just replace the endtime
            if pq.queue[0] <= interval[0]:
                pq.get()
            pq.put(interval[1])

        return len(pq.queue)

###
from typing import (
    List,
)
from lintcode import (
    Interval,
)

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
from queue import PriorityQueue

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """
    def min_meeting_rooms(self, intervals: List[Interval]) -> int:
        if not intervals: return 0
        intervals.sort(key=lambda interval: interval.start)
        pq = PriorityQueue()
        pq.put(intervals[0].end)
        for index in range(1, len(intervals)):
            currentInterval = intervals[index]
            # Which one ends first
            if currentInterval.start >= pq.queue[0]:
                pq.get()
            pq.put(currentInterval.end)
        return len(pq.queue)
    
###
class Solution:
  def minMeetingRooms(self, intervals: List[List[int]]) -> int:
    n = len(intervals)
    ans = 0
    starts = []
    ends = []

    for start, end in intervals:
      starts.append(start)
      ends.append(end)

    starts.sort()
    ends.sort()

    j = 0
    for i in range(n):
      if starts[i] < ends[j]:
        ans += 1
      else:
        j += 1

    return ans