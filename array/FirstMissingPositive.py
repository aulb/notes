class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        pass


    def firstMissingPositiveLinearSpace(self, nums: List[int]) -> int:
        # [7,8,9,11,12] => 1
        # [-1,2,3] => 1 first missing POSITIVE
        lookup = set(nums)
        i = 1
        while i in lookup: i += 1
        return i
