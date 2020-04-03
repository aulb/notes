class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid or not len(grid) or not grid[0]: return -1
        empty, fresh, rotten = 0, 1, 2

        rows, cols = len(grid), len(grid[0])
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        # Find all the rotten ones
        rotten = [[i, j] for i in range(rows) for j in range(cols) if grid[i][j] == rotten]
        time = 0
        while True:
            newRotten = []
            for i, j in rotten:
                for x, y in directions:
                    # Walk that direction,
                    # if its not already rotten,
                    m, n = i + x, j + y
                    if 0 <= m < rows and 0 <= n < cols and grid[m][n] == fresh:
                        #  add to new, make rotten
                        newRotten.append([m,n])
                        grid[m][n] = rotten

            if not newRotten: break
            rotten = newRotten
            time += 1

        fresh = [[i, j] for i in range(rows) for j in range(cols) if grid[i][j] == fresh]
        return -1 if len(fresh) else time
