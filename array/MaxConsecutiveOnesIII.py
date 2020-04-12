from collections import deque
class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        # If 1 move right
        # If 0, decrement K -> max length is recorded each time for these two cases
        # If 0 but no more K -> have to detachfrom queue, count the maxSoFar from the index + 1 of it popped
        dq = deque() # Keep track of 0s
        maxLength = 0
        maxSoFar = 0
        for index, num in enumerate(A):
            if num: maxSoFar += 1
            else: # num == 0
                dq.append(index)
                if len(dq) <= K: maxSoFar += 1
                else:
                    lastZeroIndex = dq.popleft()
                    maxSoFar = index - lastZeroIndex
            maxLength = max(maxLength, maxSoFar)
        return maxLength
