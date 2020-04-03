from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        lookup, count = Counter(t), len(t)
        l = start = end = 0
        for r, char in enumerate(s, 1):
            # The reason why it enumerate(s, 1)
            # We don't wanna do start:end + 1 -> s = "a" and t = "ab" then result is "a"

            # char will start from the beginning
            # but r will start at 1 instead
            # Example: ADOBECODEBANC
            # r = 1:char = A, r = 2:char = D
            # if char not in lookup: continue # Why can't I skip?
            # We can't simply skip because we are using the condition lookup[s[l]] < 0
            # to increment l... It doesn't work with this implementation
            count -= lookup[char] > 0
            lookup[char] -= 1

            if count == 0:
                # only advance l if the lookup[s[l]] is below 0, meaning we have spares
                # is still desirable
                while l < r and lookup[s[l]] < 0:
                    lookup[s[l]] += 1
                    l += 1

                lookup[s[l]] += 1
                count += 1 # Remove "A"

                if end == 0 or r - l < end - start:
                    start, end = l, r

                l += 1 # Advance it after we capture the state
        return s[start: end]
