"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors
"""
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        cloned = {}
        def traverse(node: 'Node') -> None:
            if cloned.get(id(node)) or not node: return
            children = []
            cloned[id(node)] = Node(node.val, children)
            for child in node.neighbors:
                if cloned.get(id(child), False):
                    children.append(cloned[id(child)])
                    continue
                children.append(traverse(child))
            return cloned[id(node)]
        return traverse(node)
