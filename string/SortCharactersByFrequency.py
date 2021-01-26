from queue import PriorityQueue
from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        if not s: return ''
        c = Counter()
        maxFrequency = 0
        for char in s:
            c[char] += 1
            maxFrequency = max(maxFrequency, c[char])

        pq = PriorityQueue()
        for char in c: pq.put((self.getPriorityOrder(c[char], maxFrequency), char))

        result = ''
        for i in range(len(c)):
            freq, char = pq.get()
            result += self.getFrequency(freq, maxFrequency) * char

        return result

    def getPriorityOrder(self, frequency: int, maxFrequency: int) -> int:
        return maxFrequency - frequency + 1

    def getFrequency(self, priorityOrder: int, maxFrequency: int) -> int:
        return -(priorityOrder - 1 - maxFrequency)

# 01/25/2021 Use bucket sort: do hash map ofcourse to keep track, but make a bucket of frequencies
