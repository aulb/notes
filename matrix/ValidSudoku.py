class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        if not self.checkRow(board): return False
        if not self.checkCol(board): return False
        return self.checkPartialSquare(board)

    def checkRow(self, board):
        for row in board:
            check = {}
            for num in row:
                if num == ".": continue
                if num in check: return False
                check[num] = True
        return True

    def checkCol(self, board):
        return self.checkRow(zip(*board))

    def checkPartialSquare(self, board):
        size = 3
        for i in [0,1,2]:
            for j in [0,1,2]:
                partialBoard = list(zip(*board[i * size: (i + 1) * size]))[j * size: (j + 1) * size]
                if not self.check3x3(partialBoard): return False
        return True

    def check3x3(self, board):
        check = {}
        for row in board:
            for num in row:
                if num == ".": continue
                if num in check: return False
                check[num] = True
        return True
