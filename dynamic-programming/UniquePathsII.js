/**
 * @param {number[][]} obstacleGrid
 * @return {number}
 */
const uniquePathsWithObstacles = obstacleGrid => {
  if (!obstacleGrid || !obstacleGrid.length || !obstacleGrid[0] || !obstacleGrid[0].length) return 0;
  const m = obstacleGrid.length;
  const n = obstacleGrid[0].length;
  // Arrays are mutable, filled as copies recommended: .fill(primitive values only)
  const lookup = new Array(m);

  for (let i = 0; i < m; i++) {
    if (!lookup[i]) lookup[i] = new Array(n);
    for (let j = 0; j < n; j++) {
      // [[1, 0]] pathway might be blocked from the start
      if (!i && !j) lookup[i][j] = !obstacleGrid[i][j];
      else if (!i) lookup[i][j] = !obstacleGrid[i][j] * lookup[i][j - 1];
      else if (!j) lookup[i][j] = !obstacleGrid[i][j] * lookup[i - 1][j];
      // Multiple by the tile itself because it might be an obstacle
      else lookup[i][j] = !obstacleGrid[i][j] * (lookup[i - 1][j] + lookup[i][j - 1]);
    }
  }
  return lookup[m - 1][n - 1];
};

/*
  // Multiple by the tile itself because it might be an obstacle
  else lookup[i][j] = !obstacleGrid[i][j] * (!obstacleGrid[i - 1][j] * lookup[i - 1][j] + !obstacleGrid[i][j - 1] * lookup[i][j - 1]);
*/
