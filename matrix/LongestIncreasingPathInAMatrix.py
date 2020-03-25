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
