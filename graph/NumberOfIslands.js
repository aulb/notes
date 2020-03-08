/**
 * @param {character[][]} grid
 * @return {number}
 */
const numIslands = grid => {
  if (!grid || !grid.length || !grid[0] || !grid[0].length) return 0;
  const n = grid.length;
  const m = grid[0].length;

  let count = 0;
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < m; j++) {
      if (grid[i][j] === "0") continue;
      count++;
      drownIsland(grid, i, j);
    }
  }

  return count;
};

const drownIsland = (grid, i, j) => {
  // Guaranteed valid by above
  const n = grid.length;
  const m = grid[0].length;
  const visited = {};
  const toVisit = [[i, j]];

  while (toVisit.length) {
    const [x, y] = toVisit.shift();

    if (!visited[`${x}-${y}`]) {
      grid[x][y] = "0";
      visited[`${x}-${y}`] = true;

      if (y + 1 < m && grid[x][y + 1] === "1") toVisit.push([x, y + 1]);
      if (x + 1 < n && grid[x + 1][y] === "1") toVisit.push([x + 1, y]);
      if (y - 1 >= 0 && grid[x][y - 1] === "1") toVisit.push([x, y - 1]);
      if (x - 1 >= 0 && grid[x - 1][y] === "1") toVisit.push([x - 1, y]);    }
  }
};
