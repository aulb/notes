class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        largest, previous = nums[0], nums[0]
        for index in range(1, len(nums)):
            # Keep adding, if 0 or negative, drop immediately
            previous = nums[index] + max(0, previous)
            largest = max(previous, largest)
        return largest