class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # Almost like a binary search, but a "search" O(m + n)
        # Start at either diagonal end but still in
        if not matrix or not len(matrix) or not matrix[0]: return False
        m, n = len(matrix), len(matrix[0])
        row, col = m - 1, 0
        while row >= 0 and col < n:
            if matrix[row][col] == target: return True
            if matrix[row][col] < target:
                col += 1
            else:
                row -= 1
        return False
