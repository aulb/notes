from collections import Counter
import heapq

class Node:
    def __init__(self, word, freq):
        self.word = word
        self.freq = freq

    def __lt__(self, other):
        if self.freq == other.freq: return self.word > other.word
        return other.freq > self.freq

    def __repr__(self):
        return self.word + ' - ' + str(self.freq)


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counts = Counter(words) # HACK: sort the words first...
        heap = []
        for word in counts:
            heapq.heappush(heap, Node(word, counts[word]))
            if len(heap) > k:
                heapq.heappop(heap)

        # [coding - 1, love - 2, i - 2]
        # HACK: Use sorted to sort one last time
        return [node.word for node in sorted(heap)][::-1]
