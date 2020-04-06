class Solution(object):
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix or not len(matrix) or not matrix[0]: return []
        self.result = []
        self.counter = 0
        def addResult(i, j):
            self.result.append(matrix[i][j])
            self.counter += 1
        row, col = len(matrix), len(matrix[0])
        maxIter = row * col
        """ a 3x4 example
        i 0 0 0 0
        j 0 1 2 3
        We finished row 0 rowStart += 1

        i 1 2
        j 3 3
        We finished the last column colEnd -= 1

        i 2 2 2
        j 2 1 0
        We finished the last row rowEnd -=  1

        i 1
        j 0
        We finished the first column colStart += 1

        Iteration one done.
        i 1 1
        j 1 2
        """
        rowStart, rowEnd = 0, row - 1
        colStart, colEnd = 0, col - 1

        while self.counter < maxIter:
            for j in range(colStart, colEnd + 1): # Right
                addResult(rowStart, j)
            rowStart += 1

            if self.counter >= maxIter: break
            for i in range(rowStart, rowEnd + 1): # Down
                addResult(i, colEnd)
            colEnd -= 1

            if self.counter >= maxIter: break
            for j in range(colEnd, colStart - 1, -1): # Left
                addResult(rowEnd, j)
            rowEnd -= 1

            if self.counter >= maxIter: break
            for i in range(rowEnd, rowStart - 1, -1): # Up
                addResult(i, colStart)
            colStart += 1
        return self.result
