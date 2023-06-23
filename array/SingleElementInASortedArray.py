class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            # 1,1,2,2,3,3,4,8,8
            # The numbers are in pairs of twos
            if mid % 2 == 1:
                mid -= 1
            # If mid not the same as the next, then its on the left
            if nums[mid] != nums[mid + 1]:
                right = mid
            # Everything up to mid is in a pair of twos, look on the right
            else:
                left = mid + 2
        return nums[left]