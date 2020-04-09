# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # Solution one. O(n) runtime, O(n) space
    """
    [1,2,3,4,null,6,null,null,5], last element would be [5,9] length is 6
    """
    def isCompleteTree(self, root: TreeNode) -> bool:
        # Solution one, use counting
        # Number of nodes must be the last one in the array
        nodes = [(root, 1)]
        i = 0
        while i < len(nodes):
            node, v = nodes[i]
            i += 1
            if not node: continue
            if node.left: nodes.append((node.left, 2 * v))
            if node.right: nodes.append((node.right, 2 * v + 1))
        return nodes[-1][1] == len(nodes)

    """
    Another solution is to do a normal BFS. When we encounter a null, that means its not complete.
    """
