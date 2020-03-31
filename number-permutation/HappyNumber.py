import functools
# Cycle lookup is an important part of this question. Whats the stopping condition?
class Solution:
    def isHappy(self, n: int) -> bool:
        cycleLookup = set()
        while True:
            if n == 1: return True
            if n in cycleLookup: return False
            cycleLookup.add(n)
            n = self.getResult(n)


    def getResult(self, n: int) -> int:
        result = 0
        for num in str(n):
            result += int(num) ** 2
        return result
