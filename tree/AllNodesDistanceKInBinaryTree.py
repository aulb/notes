# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        if not target: return
        # Transform into graph
        graph = {}
        def convertToGraphDFS(node, parent: int = None):
            if not node: return
            graph[node.val] = [child.val for child in (node.left, node.right) if child]
            convertToGraphDFS(node.left, node.val)
            convertToGraphDFS(node.right, node.val)
            if parent is not None: graph[node.val].append(parent) # don't do if parent (int = 0)

        convertToGraphDFS(root)
        print(graph)
        if target.val not in graph: return []

        visited = set()
        result = []
        def dfs(node: int, distance: int):
            if node in visited or distance > K: return
            if distance == K: result.append(node)
            visited.add(node)
            for edge in graph[node]:
                dfs(edge, distance + 1)
        dfs(target.val, 0)
        return result
