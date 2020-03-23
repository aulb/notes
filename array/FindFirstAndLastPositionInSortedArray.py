class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return [self.findEdge(nums, target), self.findEdge(nums, target, True)]

    def binarySearch(self, nums: List[int], target: int) -> int:
        if not nums: return -1
        l, r = 0, len(nums) - 1
        while l <= r:
            m = l + (r - l) // 2
            if nums[m] == target: return m
            if nums[m] > target: r = m - 1
            else: l = m + 1
        return -1

    def findEdge(self, nums: List[int], target: int, right: bool = False) -> int:
        prev = curr = self.binarySearch(nums, target)
        if prev == -1: return -1
        while True:
            if right:
                end = self.binarySearch(nums[curr + 1:], target)
            else:
                end = self.binarySearch(nums[:curr], target)

            if end == -1: return curr
            curr = curr + 1 + end if right else end
