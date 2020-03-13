/**
 * @param {number} m
 * @param {number} n
 * @return {number}
 */
const uniquePaths = (m, n) => {
  if (!m || !n) return 0;
  // Arrays are mutable, filled as copies recommended: .fill(primitive values only)
  const lookup = new Array(m);

  for (let i = 0; i < m; i++) {
    if (!lookup[i]) lookup[i] = new Array(n);
    for (let j = 0; j < n; j++) {
      // Can be achieved by moving down or right ONLY
      if (i === 0 || j === 0) lookup[i][j] = 1;
      else lookup[i][j] = lookup[i - 1][j] + lookup[i][j - 1];
    }
  }
  return lookup[m - 1][n - 1];
};
