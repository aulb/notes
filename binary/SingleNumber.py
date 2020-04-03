from functools import reduce
# Naive: Use a hash, once the count for an element
# XOR: its commutative, its fast, same numbers will cancel
# Math! If a is missing then 2(a+b+c+...) - sum(nums) = a
# 2 * sum(set(nums)) - sum(nums) = a!
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # # Reduce to a single number by xor-ing
        # res = 0
        # for num in nums: res ^= num
        # return res

        """
        :type nums: List[int]
        :rtype: int
        """
        return reduce(lambda x, y: x ^ y, nums)
