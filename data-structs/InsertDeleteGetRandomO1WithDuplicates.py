import random
from collections import defaultdict
class RandomizedCollection:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.index = defaultdict(set) # We keep track of index list
        self.nums = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        self.nums.append(val)
        self.index[val].add(len(self.nums) - 1)
        # If its the first one then true, otherwise its the duplicate
        return len(self.index[val]) == 1

    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        if val not in self.index: return False
        lastVal = self.nums[-1]
        if val == lastVal:
            self.index[val].discard(len(self.nums) - 1)
        else:
            idxToOverwrite = self.index[val].pop()
            self.nums[idxToOverwrite] = lastVal
            self.index[lastVal].discard(len(self.nums) - 1)
            self.index[lastVal].add(idxToOverwrite)
        if len(self.index[val]) == 0: del self.index[val]
        self.nums.pop()
        return True


    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        return self.nums[random.randint(0, len(self.nums) - 1)]


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
