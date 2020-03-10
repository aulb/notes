# Merge Intervals
Sort by `start`. Merge by always taking highest `end`. Push when `prev.end` is lesser than `curr.start`.

# Non Overlapping Intervals
"Given a collection of intervals, find the maximum number of intervals that are non-overlapping." (the classic Greedy problem: Interval Scheduling)

# Meeting Rooms II
Sort by start time, use min heap to keep track of rooms available. Put end time only in the heap nodes.
[Explanations](http://tiancao.me/Leetcode-Unlocked/)
