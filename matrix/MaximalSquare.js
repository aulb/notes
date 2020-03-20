/**
 * @param {character[][]} matrix
 * @return {number}
 */
const maximalSquare = matrix => {
  if (!matrix || !matrix.length || !matrix[0] || !matrix[0].length) return 0;

  const m = matrix.length;
  const n = matrix[0].length;
  const lookup = new Array(m + 1).fill(0);
  for (let i = 0; i < m + 1; i++) lookup[i] = new Array(n + 1).fill(0);
  let max = 0;
  for (let i = 0; i < m; i++) {
    for (let j = 0; j < n; j++) {
      if (matrix[i][j] === "0") continue;
      lookup[i + 1][j + 1] = Math.min(lookup[i][j], lookup[i + 1][j], lookup[i][j + 1]) + 1;
      max = Math.max(lookup[i + 1][j + 1], max);
    }
  }
  return max ** 2;
};
