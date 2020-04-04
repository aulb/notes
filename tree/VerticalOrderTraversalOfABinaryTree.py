# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Node:
    def __init__(self, val, depth):
        self.val = val
        self.depth = depth

    def __lt__(self, other):
        if self.depth == other.depth: return self.val < other.val
        return other.depth > self.depth

    def __repr__(self):
        return str(self.val) + ' - ' + str(self.depth)


class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        vertOrder = {}
        def traverse(node, pos, depth):
            if not node: return
            if not vertOrder.get(pos, False):
                vertOrder[pos] = []
            vertOrder[pos].append(Node(node.val, depth))
            traverse(node.left, pos - 1, depth + 1)
            traverse(node.right, pos + 1, depth + 1)

        result = []
        traverse(root, 0, 0)
        minPos = min(vertOrder.keys())
        maxPos = max(vertOrder.keys())
        for i in range(minPos, maxPos + 1):
            nodes = sorted(vertOrder.get(i))
            result.append([node.val for node in nodes])
        return result
