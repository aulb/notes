class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        longest = 0
        for x in nums:
            # Start of sequence (possibly)
            if x - 1 not in nums:
                # Find the end
                y = x + 1
                while y in nums:
                    y += 1
                longest = max(longest, y - x)
        return longest
