class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        self.helper(n, {"c": 0, "o": 0}, res, "")
        return res

    def helper(self, n, counts, res, strSoFar):
        if counts["o"] == n and counts["o"] == counts["c"]: 
            res.append(strSoFar)
            return
        if counts["o"] < n: # We can still open
            self.helper(n, {"o": counts["o"] + 1, "c": counts["c"]}, res, strSoFar + "(")
        if counts["o"] > 0 and counts["o"] > counts["c"]: # We can also close
            self.helper(n, {"o": counts["o"], "c": counts["c"] + 1}, res, strSoFar + ")")

## With no dict
class Solution2:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        self.helper(n, 0, 0, res, "")
        return res

    def helper(self, n, left, right, res, strSoFar):
        if left == right and left == n:
            res.append(strSoFar)
            return
        if left < n: # We can still open
            self.helper(n, left + 1, right, res, strSoFar + "(")
        if left > 0 and left > right: # We can also close
            self.helper(n, left, right + 1, res, strSoFar + ")")
