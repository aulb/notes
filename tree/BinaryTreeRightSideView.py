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


###
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class SolutionWrapper:
    def __init__(self, val: int, position: int):
        self.val = val
        self.position = position

    def __repr__(self):
        return f'{self.val}:{self.position}'

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # Isn't this just right only?
        # Nvm, for each level find the right most
        levels = []
        # DFS on left first, just left center right traversal works
        self.traverse(root, levels, 0, 0) 
        return [level.val for level in levels]

    def traverse(self, node: TreeNode, levels: List[TreeNode], level: int, position: int) -> None:
        if not node: return
        if len(levels) == level: # Not yet created
            levels.append(SolutionWrapper(node.val, position))
        self.traverse(node.left, levels, level + 1, position - 1)
        levels[level] = SolutionWrapper(node.val, position)
        # [1,2,3,null,5,6] can't use position in this case, do this traversal instead
        self.traverse(node.right, levels, level + 1, position + 1)


# 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # Isn't this just right only?
        # Nvm, for each level find the right most
        levels = []
        # DFS on left first, just left center right traversal works
        self.traverse(root, levels, 0) 
        return [level.val for level in levels]

    def traverse(self, node: TreeNode, levels: List[TreeNode], level: int) -> None:
        if not node: return
        if len(levels) == level: # Not yet created
            levels.append(node)
        self.traverse(node.left, levels, level + 1)
        levels[level] = node
        # [1,2,3,null,5,6] can't use position in this case, do this traversal instead
        self.traverse(node.right, levels, level + 1)
        