from enum import IntEnum

class States(IntEnum):
    LIVE_CELL_DIES = 2
    DEAD_CELL_LIVES = 3

class Solution:
    directions = [
        [-1,-1],
        [-1,0],
        [-1,1],
        [0,-1],
        [0,1],
        [1,-1],
        [1,0],
        [1,1],
    ]

    def checkCell(self, board: List[List[int]], m: int, n: int, i: int, j: int) -> None:
        count = 0
        for direction in self.directions:
            x = i + direction[0]
            y = j + direction[1]
            if not self.isValidCoordinate(m, n, x, y): 
                continue
            if board[x][y] == 1 or board[x][y] == States.LIVE_CELL_DIES:
                count += 1
        
        if board[i][j] == 1:
            if count < 2 or count > 3: 
                board[i][j] = States.LIVE_CELL_DIES
        else:
            if count == 3: 
                board[i][j] = States.DEAD_CELL_LIVES


    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not len(board) or not len(board[0]): return
        m, n = len(board), len(board[0])
        # Rules:
        # 1) Cell with fewer than 2 live neighbors dies
        # 2) Cell with more than 3 live neighbors dies
        # 3) Any dead cell with 3 live neighbors becomes a live cell
        for i in range(m):
            for j in range(n):
                self.checkCell(board, m, n, i, j)
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == States.LIVE_CELL_DIES: board[i][j] = 0
                elif board[i][j] == States.DEAD_CELL_LIVES: board[i][j] = 1
    
    def isValidCoordinate(self, m: int, n: int, i: int, j: int):
        return m > i and i >= 0 and n > j and j >= 0
