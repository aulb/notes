class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        left = 0
        sumSoFar = 0
        minLength = float("inf")
        for right, num in enumerate(nums, 1):
            sumSoFar += num
            if sumSoFar >= s:
                while left < right and sumSoFar >= s:
                    # Why inside... todo.
                    minLength = min(minLength, right - left)
                    sumSoFar -= nums[left]
                    left += 1

        return 0 if minLength == float("inf") else minLength
