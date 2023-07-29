# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def check(node: Optional[TreeNode]) -> Tuple[int, int]:
            if not node: return (0, 0)
            left, right = check(node.left), check(node.right)

            rob_current = node.val + left[1] + right[1]
            skip_robbing = max(left) + max(right)
            return (rob_current, skip_robbing)
        return max(check(root))
