class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        low, hi = 0, len(nums)
        while hi >= low:
            mid = low + (hi - low) // 2
            left = nums[mid - 1] if len(nums) > mid - 1 >= 0 else -float("inf")
            right = nums[mid + 1] if len(nums) > mid + 1 >= 0 else -float("inf")
            if nums[mid] > left and nums[mid] > right: return mid
            if left > nums[mid]:
                hi = mid - 1
            else:
                low = mid + 1
        return -1
