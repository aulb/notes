from collections import deque, Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s): return []
        dq = deque()
        lookup = Counter(p)
        count = len(p)
        result = []
        for index, char in enumerate(s):
            if len(dq) >= len(p):
                leftMostChar = dq.popleft()
                if leftMostChar in lookup:
                    lookup[leftMostChar] += 1
                    count += lookup[leftMostChar] > 0
            dq.append(char)
            if char in lookup:
                count -= lookup[char] > 0
                lookup[char] -= 1
            if count == 0: result.append(index - len(p) + 1)
        return result
