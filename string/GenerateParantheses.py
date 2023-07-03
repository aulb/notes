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
