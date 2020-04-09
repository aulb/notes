"""
If the edges given makes a cycle, its not a valid tree.
Trees do not have cycle.
1) We can use topological sort ( DFS ). Supplying the parent everytime
2) We can use union find on disjoint set. If it belongs on the same set, then theres a cycle.
"""
from collections import defaultdict
class Solution:
    def validTree(self, edges) -> bool:
        if not edges: return True
        # Adj list representation
        graph = defaultdict(list)
        visited = defaultdict(int)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        # Build O(edges)

        # It doesn't matter where we DFS from
        # If this returns true, it means that we hit a visited
        if self.dfs(graph, visited, edges[0][0], -1): return False
        return True

    def dfs(self, graph, visited: defaultdict(int), node: int, parent: int) -> bool:
        # O(vertex + edges)
        visited[node] = True
        for edge in graph[node]:
            # If its not parent and its not visited yet...
            if edge != parent and visited.get(edge, False): return True
            # not visited here to prevent inf loop
            if not visited.get(edge, False) and self.dfs(graph, visited, edge, node): return True
        return False

sol = Solution()
edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
invalidEdges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
invalidEdges2 = [[1, 2], [2, 3], [1, 3]]
print(sol.validTree(invalidEdges2))
