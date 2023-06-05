"""
The amortized is O(n) with deque. This is because the values in the queue is put in and pulled out once from the queue.
"""
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # [1,3,-1,-3,5,3,6,7] k = 3
        # [3,-1] => 3 i + 1 >= 3 (k), i = 2 so yes result.push(dq[0]) [1, 2]
        # [-1,-3] i = 3 [2, 3] i >= 3 (k): while dq[0] <= (i - k)

        # [1,3,1,2,0,5], 3
        if k >= len(nums): return [max(nums)]
        # The 0th element is the max
        dq = deque()
        maxes = []

        for i in range(len(nums)):
            # The left side is guaranteed to be the "oldest" index that survives
            if dq and dq[0] <= i - k:
                dq.popleft()

            num = nums[i]
            if len(dq) == 0:
                dq.append(i)
            else:
                # This guarantees the order of maximality. only the highest numbers survive
                while dq and num > nums[dq[-1]]:
                    dq.pop()
                dq.append(i)

            # Make sure we have the sliding window size before capturing numbers
            if i + 1 >= k:
                maxes.append(nums[dq[0]])

        return maxes
