# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root: return 0
        self.diameter = 1
        def depth(node):
            if not node: return 0
            l = depth(node.left)
            r = depth(node.right)
            self.diameter = max(self.diameter, l + r + 1)
            return max(l, r) + 1
        depth(root)
        return self.diameter - 1
