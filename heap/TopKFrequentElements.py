# Top most frequent offline, using bucket sort!
from collections import Counter
class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums: return []
        result = []
        counts = Counter(nums)

        # Get bucket size
        bucketSize = max(counts.values()) # [1,1,1,2,2,3] => 3
        bucket = [None for _ in range(bucketSize + 1)] # [None, None, None, None]
        # Add one so its cleaner, no need to count values

        for element in counts:
            count = counts[element]
            if not bucket[count]: bucket[count] = [element]
            else: bucket[count].append(element)

        # Iterate backwards for each bucket
        counter = 0
        for index in range(len(bucket) - 1, -1, -1):
            if not bucket[index]: continue
            for element in bucket[index]:
                result.append(element)
                counter += 1
                if counter == k: return result

        return result
