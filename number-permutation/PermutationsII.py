class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result, added = [], set()
        self.dfs(nums, [], result, added)
        return result

    def dfs(self, nums, path, result, added) -> None:
        if not nums:
            key = ".".join(str(x) for x in path)
            if key in added: return
            result.append(path)
            added.add(key)
        for i in range(len(nums)):
            self.dfs(nums[:i] + nums[i+1:], path + [nums[i]], result, added)
