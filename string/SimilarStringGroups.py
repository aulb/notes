class Solution:
    def numSimilarGroups(self, A: List[str]) -> int:
        # Let len(A) ==> n
        # Let len(A[0]) ==> t
        if len(A) < 2: return len(A)
        # ["abc","abc"] this is possible
        # O(t)
        def isSimilar(s: str, t: str):
            res = 0
            for i, char in enumerate(s):

                res += char != t[i]
                if res > 2: return False
            return True # don't need to check == 2 or == 0 separately its either 2 or more

        # O(n^2) runtime
        def dfs(s):
            for i in range(len(A)):
                if not A[i]: continue
                # O(t)
                if isSimilar(s, A[i]):
                    copyS = A[i]
                    A[i] = None
                    dfs(copyS)

        res = 0
        # O(n^2) runtime
        for i in range(len(A)):
            if not A[i]: continue
            s = A[i]
            A[i] = None
            res += 1
            # O(n^2)
            dfs(s)
        # O(t * n^2)
        return res
