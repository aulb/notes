/**
 * @param {number[][]} matrix
 * @return {void} Do not return anything, modify matrix in-place instead.
 */
const setZeroes = matrix => {
  if (!matrix || !matrix.length || !matrix[0] || !matrix[0].length) {
    return;
  }

  let m = matrix.length;
  let n = matrix[0].length;
  let firstRowZero = matrix[0].some(num => num === 0);
  let firstColZero = false;
  for (let i = 0; i < m; i++) {
    firstColZero = firstColZero || !matrix[i][0];
  }

  // Mark
  for (let i = 1; i < m; i++) {
    for (let j = 1; j < n; j++) {
      if (!matrix[i][j]) {
        matrix[i][0] = 0;
        matrix[0][j] = 0;
      }
    }
  }

  // Zero out
  for (let i = 1; i < m; i++) {
    for (let j = 1; j < n; j++) {
      if (!matrix[i][0] || !matrix[0][j]) {
        matrix[i][j] = 0;
      }
    }
  }

  for (let i = 0; i < m; i++) {
    if (firstColZero) matrix[i][0] = 0;
  }

  for (let j = 0; j < n; j++) {
    if (firstRowZero) matrix[0][j] = 0;
  }
};
