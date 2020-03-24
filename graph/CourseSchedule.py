from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites: return True
        # Adj list representation
        graph = defaultdict(list)
        visited = defaultdict(int)

        for course, prereq in prerequisites:
            graph[course].append(prereq)

        for course in range(numCourses):
            if not self.dfs(graph, visited, course): return False

        return True

    def dfs(self, graph: List[List[int]], visited: defaultdict(int), course: int) -> bool:
        if visited[course] == -1: return False # If its currently being visited, circular
        if visited[course] == 1: return True
        visited[course] = -1 # Being visited
        for prereq in graph[course]:
            if not self.dfs(graph, visited, prereq): return False
        visited[course] = 1
        return True
