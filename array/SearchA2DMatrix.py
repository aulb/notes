class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]: return False
        searchRow = self.binarySearchForRow(matrix, target)
        if searchRow == -1: return False

        rows = len(matrix)
        cols = len(matrix[0])
        l, h = 0, cols - 1
        while h >= l:
            m = l + (h - l) // 2
            # If the value is in between return
            if matrix[searchRow][m] == target: return True
            elif matrix[searchRow][m] > target: h = m - 1
            else: l = m + 1
        return False

    def binarySearchForRow(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        l, h = 0, rows - 1

        while h >= l:
            m = l + (h - l) // 2
            # If the value is in between return
            if matrix[m][0] <= target <= matrix[m][cols - 1]: return m
            elif matrix[m][0] > target: h = m - 1
            else: l = m + 1
        return -1
