class Solution:
    def balancedStringSplit(self, s: str) -> int:
        if not s: return 0
        counter = 0
        balancedCounter = 0
        for c in s:
            counter = counter + (1 if c == "R" else -1)
            balancedCounter = balancedCounter + (counter == 0)
        return balancedCounter
