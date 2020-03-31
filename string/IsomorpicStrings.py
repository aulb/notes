class Solution:
    # Don't forget to check both ways "ab" "aa"
    def isIsomorphic(self, s: str, t: str) -> bool:
        return self.checkOneWay(s, t) and self.checkOneWay(t, s)


    def checkOneWay(self, s:str, t:str) -> bool:
        lookup = {}
        for i, c in enumerate(s):
            if not lookup.get(c, False):
                lookup[c] = t[i]
                continue
            if lookup[c] != t[i]: return False
        return True
