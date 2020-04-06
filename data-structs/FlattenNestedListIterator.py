# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.lists = [[nestedList, 0]]


    def next(self) -> int:
        """
        :rtype: int
        """
        if not self.hasNext(): return None
        nestedList, i = self.lists[-1]
        self.lists[-1][1] += 1
        return nestedList[i].getInteger()


    def hasNext(self) -> bool:
        """
        :rtype: bool
        """
        while self.lists:
            nestedList, i = self.lists[-1]
            # Get rid of "fully visited" nestedList
            if i == len(nestedList):
                self.lists.pop()
                continue

            # If its an integer, done
            if nestedList[i].isInteger(): return True
            # Adding new list to the stack, increment the previous' nestedList's counter
            self.lists[-1][1] += 1
            self.lists.append([nestedList[i].getList(), 0])
        return False

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())

def printNestedArr(arr):
    result = []
    def helper(obj):
        if not isinstance(obj, list):
            result.append(obj)
            return
        for item in obj:
            if isinstance(item, list):
                helper(item)
            else:
                result.append(item)
        helper(arr)
        return result
