class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        self.colors = [0 for i in range(len(graph))]

        def dfs(node, color):
            if self.colors[node]: return self.colors[node] == color
            self.colors[node] = color
            for edge in graph[node]:
                if not dfs(edge, -color): return False
            return True

        for node in range(len(graph)):
            # We are not promised a connected graph
            # Always try to color it the same way one way when starting
            if not self.colors[node] and not dfs(node, 1): return False
        return True
