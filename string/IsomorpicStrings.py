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

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        sMapping, tMapping = {}, {}
        si, ti = 0, 0
        while si < len(s):
            if sMapping.get(s[si], None) is None:
                sMapping[s[si]] = t[ti]
            else:
                if sMapping[s[si]] != t[ti]: return False    
            if tMapping.get(t[ti], None) is None:
                tMapping[t[ti]] = s[ti]
            else:
                if tMapping[t[ti]] != s[ti]: return False  
            si += 1
            ti += 1
        return True