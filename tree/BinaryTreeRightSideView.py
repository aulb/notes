# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        result = []
        def traverse(node: TreeNode, level: int) -> None:
            if not node: return None
            if level == len(result) + 1: result.append(node.val)
            traverse(node.right, level + 1)
            traverse(node.left, level + 1)
        traverse(root, 1)
        return result
