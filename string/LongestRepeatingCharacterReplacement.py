from collections import Counter
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxLength, largestCount = 0, 0
        counter = Counter()
        for index, char in enumerate(s):
            counter[char] += 1
            largestCount = max(largestCount, counter[char])
            if maxLength - largestCount >= k:
                counter[s[index - maxLength]] -= 1
            else:
                maxLength += 1
        return maxLength