# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        The correct order is right left and node because
        1) We need to build the linked list from the back
        2) Should be inplace
        If we do left, right, curr then the order is not how they want it in this question
        """
        self.prev = None
        def traverse(node: TreeNode) -> None:
            if not node: return None
            traverse(node.right)
            traverse(node.left)
            node.right = self.prev
            node.left = None
            self.prev = node
        traverse(root)
