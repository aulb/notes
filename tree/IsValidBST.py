# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root: return False
        # when we go left max is root.val
        # when we go right min is root.val
        # right -> min 5, max whatever
        # right - left -> min 5, max 4 < root.val
        # the min for the right will be whatever root.val
        return self.helper(root, -float('inf'), float('inf'))
    
    def helper(self, root, minVal, maxVal):
        if not root: return True
        if not (root.val > minVal and maxVal > root.val): return False
        return self.helper(root.left, minVal, root.val) and self.helper(root.right, root.val, maxVal)
