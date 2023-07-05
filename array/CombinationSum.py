class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        self.dfs(candidates, target, res, [])
        return res

    def dfs(self, candidates, target, res, candidateCombo):
        if target < 0:
            return
        if target == 0:
            res.append(candidateCombo)
            return
        for index, candidate in enumerate(candidates):
            # candidates[index:] makes sure when we go to the next one we don't get duplicate
            self.dfs(candidates[index:], target - candidate, res, candidateCombo + [candidate])