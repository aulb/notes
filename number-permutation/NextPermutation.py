class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 15876531
        # 16875531 swap (5,1) with (6,4)
        # 16135578 reverse (2::)
        swapIdx = -1
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                swapIdx = i
                break # they're not sorted

        # Already sorted in descending order (max number)
        if swapIdx == -1:
            nums[::] = nums[::-1]
            return

        closestMatchIdx = swapIdx
        for i in range(swapIdx + 1, len(nums)):
            if nums[i] <= nums[swapIdx]: break
            closestMatchIdx = i

        nums[swapIdx], nums[closestMatchIdx] = nums[closestMatchIdx], nums[swapIdx]
        nums[swapIdx + 1:] = nums[:swapIdx:-1]
