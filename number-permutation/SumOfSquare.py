class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        # Two sum
        lookup = set()
        for i in range(int(c ** 0.5) + 1):
            if c - i ** 2 in lookup: return True
            # Special case for 1 + 1 = 2, 16 + 16 = 32, you get the point
            if i ** 2 + i ** 2 == c: return True
            lookup.add(i ** 2)

        return False
