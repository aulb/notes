class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        if not target or not nums: return 0

        # Similar to coin change problem
        nums.sort()
        lookup = [0 for x in range(target + 1)]
        lookup[0] = 1 # Base case, if there is a way to hit 0, then its a valid combination just like coin change

        for i in range(target + 1):
            for num in nums:
                if num > i: break
                if num == i: lookup[i] += 1
                if num < i: lookup[i] += lookup[i - num]

        return lookup[-1]
