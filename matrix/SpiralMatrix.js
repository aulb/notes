/**
 * @param {number[][]} matrix
 * @return {number[]}
 */
const spiralOrder = matrix => {
  if (!matrix || !matrix.length || !matrix[0] || !matrix[0].length) return [];

  const m = matrix.length;
  const n = matrix[0].length;
  const result = new Array(m * n);
  let x = 0;
  let i = 0;
  let j = 0;
  let colMax = n - 1;
  let colMin = 0;
  let rowMax = m - 1;
  let rowMin = 0;
  while (x < m * n) {

  }

  console.log({result});
  return result;
};
