class Node:
    def __init__(self, x: int, minSoFar: int = None):
        self.val = x
        self.minSoFar = minSoFar


class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []


    def push(self, x: int) -> None:
        minSoFar = x if not self.stack else min(self.getMin(), x)
        self.stack.append(Node(x, minSoFar))


    def pop(self) -> None:
        if not self.stack: return
        topNode = self.stack.pop()
        return topNode.val


    def top(self) -> int:
        if not self.stack: return
        return self.stack[-1].val


    def getMin(self) -> int:
        if not self.stack: return
        return self.stack[-1].minSoFar


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
