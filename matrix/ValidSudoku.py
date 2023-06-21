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

# Wtf? Above solution trippin
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".": continue
                if not (self.isRowValid(board, i, j) and self.isColValid(board, i, j) and self.isSubBoxValid(board, i, j)): return False
        return True

    def isRowValid(self, board, i, j):
        num = board[i][j]
        for colIndex in range(9):
            if colIndex == j: continue
            if board[i][colIndex] == num: return False
        return True

    def isColValid(self, board, i, j):
        num = board[i][j]
        for rowIndex in range(9):
            if rowIndex == i: continue
            if board[rowIndex][j] == num: return False
        return True

    def isSubBoxValid(self, board, i, j):
        num = board[i][j]
        startI = (i // 3) * 3
        startJ = (j // 3) * 3   
        for x in range(startI, startI + 3):
            for y in range(startJ, startJ + 3):
                if i == x and j == y: continue
                if board[x][y] == num: return False   
        return True         

### Set is a good friend
class Solution(object):
    def isValidSudoku(self, board):
        # a = [(0, '0'), ('1', 0), (0,0,'7'), (0,0,'7')]
        # print(set(a)) # {(0, '0'), ('1', 0), (0, 0, '7')}
        res = []
        for i in range(9):
            for j in range(9):
                element = board[i][j]
                if element != '.':
                    res += [(i, element), (element, j), (i // 3, j // 3, element)]
        return len(res) == len(set(res))