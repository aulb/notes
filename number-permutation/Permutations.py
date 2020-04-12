class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.dfs(nums, [], result)
        return result

    def dfs(self, nums, path, result) -> None:
        if not nums:
            result.append(path)

        for i in range(len(nums)):
            self.dfs(
                nums[:i] + nums[i+1:], # nums.pop(i)
                path + [nums[i]], # [1,2,3], [1,3,2] ...
                result
            )
