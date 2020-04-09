class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        self.directions = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,0],[0,1],[1,-1],[1,0],[1,1]]
        self.m, self.n = len(board), len(board[0])
        def getMines(coord: List[int]) -> None:
            x, y = coord
            mines = 0
            for d in self.directions:
                i, j = x + d[0], y + d[1]
                if 0 <= i < self.m and 0 <= j < self.n:
                    if board[i][j] == 'M': mines += 1
            return mines
        x, y = click
        if board[x][y] == 'B' or board[x][y].isdigit(): return board
        if board[x][y] == 'M':
            board[x][y] = 'X'
            return board

        # This is the 'B' case
        def dfs(coord) -> None:
            x, y = coord
            if board[x][y] != 'E': return
            mines = getMines(coord)
            if mines:
                board[x][y] = str(mines)
                return
            board[x][y] = 'B'
            for d in self.directions:
                i, j = x + d[0], y + d[1]
                if 0 <= i < self.m and 0 <= j < self.n and board[i][j] == 'E':
                    dfs([i, j])
        dfs(click)
        return board
