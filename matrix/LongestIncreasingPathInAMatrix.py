class Solution:
    """ Lookup intent: Whats the longest sequence from this tile?
        [9,9,4]      [1,1,2]
        [6,6,8]  ==> [2,2,1]
        [2,1,1]      [3,4,2]
    """
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not matrix: return 0
        longest_path_length = 1
        row, col = len(matrix), len(matrix[0])
        lookup = [[None] * col for _ in range(row)]

        def dfs(x, y):
            if not lookup[x][y]:
                lookup[x][y] = 1 + max(
                    dfs(x - 1, y) if x - 1 >= 0 and matrix[x][y] < matrix[x - 1][y] else 0,
                    dfs(x + 1, y) if x + 1 < row and matrix[x][y] < matrix[x + 1][y] else 0,
                    dfs(x, y - 1) if y - 1 >= 0 and matrix[x][y] < matrix[x][y - 1] else 0,
                    dfs(x, y + 1) if y + 1 < col and matrix[x][y] < matrix[x][y + 1] else 0
                )
            return lookup[x][y]

        for i in range(row):
            for j in range(col):
                longest_path_length = max(dfs(i, j), longest_path_length)

        return longest_path_length


class Solution2:
    def __init__(self):
        self.directions = [[1,0],[-1,0],[0,1],[0,-1]]

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if len(matrix) == 0 or len(matrix[0]) == 0: return 0
        highest = 0
        rowLen = len(matrix)
        colLen = len(matrix[0]) 
        visited = [[0 for _ in range(colLen)] for _ in range(rowLen)]
        for i in range(rowLen):
            for j in range(colLen):
                highest = max(self.visit(matrix, visited, i, j, rowLen, colLen), highest)
        return highest

    def visit(self, matrix, visited, i, j, rowLen, colLen):
        if visited[i][j] != 0 or visited[i][j] == -1: return visited[i][j]
        visited[i][j] = -1 # currently visited
        currentValue = matrix[i][j]
        longestLength = 1
        for direction in self.directions:
            newI = i + direction[0]
            newJ = j + direction[1]
            if self.isValidCoordinate(newI, newJ, rowLen, colLen) and matrix[newI][newJ] > currentValue:
                length = self.visit(matrix, visited, newI, newJ, rowLen, colLen)
                if length != -1:
                    longestLength = max(1 + length, longestLength)
        visited[i][j] = longestLength
        return longestLength

    def isValidCoordinate(self, i, j, rowLen, colLen):
        return i < rowLen and i >= 0 and j < colLen and j >= 0