import random
class RandomizedSet:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.index = {} # Num index lookup
        self.nums = []


    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.index: return False
        # Append to last, and keep track of the index
        self.nums.append(val)
        self.index[val] = len(self.nums) - 1
        return True


    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.index: return False
        if len(self.nums) != 1:
            idxToOverwrite = self.index[val]
            self.nums[idxToOverwrite] = self.nums[-1]
            self.index[self.nums[-1]] = idxToOverwrite
        # Also remember to clear the index
        self.nums.pop()
        del self.index[val]
        return True


    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        return self.nums[random.randint(0, len(self.nums) - 1)]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
