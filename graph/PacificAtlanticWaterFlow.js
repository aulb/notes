/**
 * @param {number[][]} matrix
 * @return {number[][]}
 */
const pacificAtlantic = matrix => {
  if (!matrix || !matrix.length || !matrix[0] || !matrix[0].length) return [];
  const m = matrix.length;
  const n = matrix[0].length;
  const results = [];
  const pVisited = {};
  const aVisited = {};

  for (let i = 0; i < m; i++) {
    dfs(matrix, i, 0, pVisited, m, n);
    dfs(matrix, i, n - 1, aVisited, m, n);
  }

  for (let j = 0; j < n; j++) {
    dfs(matrix, 0, j, pVisited, m, n);
    dfs(matrix, m - 1, j, aVisited, m, n);
  }

  for (let i = 0; i < m; i++) {
    for (let j = 0; j < n; j++) {
      if (pVisited[`${i}-${j}`] && aVisited[`${i}-${j}`]) results.push([i, j]);
    }
  }
  return results;
};

// This is a good walking method. It cleaned up the code a bit.
const WALK = [[-1, 0], [1, 0], [0, -1], [0, 1]];
const dfs = (matrix, i, j, visited, m, n) => {
  visited[`${i}-${j}`] = true;
  for (let idx = 0; idx < WALK.length; idx++) {
    const walk = WALK[idx];
    const x = i + walk[0];
    const y = j + walk[1];

    // Need to be equal or lesser to flow. If the caller is bigger then ignore.
    if (x < 0 || x >= m || y < 0 || y >= n || visited[`${x}-${y}`] || matrix[x][y] < matrix[i][j]) continue;
    dfs(matrix, x, y, visited, m, n);
  }
};
