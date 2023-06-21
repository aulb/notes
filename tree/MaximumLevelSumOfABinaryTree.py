# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root: return -1
        levelSum = {}
        nodesAndLevel = [(root, 0)]
        while nodesAndLevel:
            node, level = nodesAndLevel.pop()
            levelSum[level] = levelSum.get(level, 0) + node.val
            if node.left: nodesAndLevel.append((node.left, level + 1))
            if node.right: nodesAndLevel.append((node.right, level + 1))
        print(levelSum)
        maxLevelSum = -float('inf')
        maxLevel = -1
        for level in levelSum:
            if levelSum[level] > maxLevelSum:
                maxLevel = level 
                maxLevelSum = levelSum[level]
        return maxLevel + 1