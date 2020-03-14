/**
 * @param {number[]} A
 * @return {number[]}
 */
const sortedSquares = A => {
  if (!A || !A.length) return [];

  // Find index of 0 or first positive number
  let x = 0;
  for (let i = 0; i <= A.length; i++) {
    x = i;
    if (A[i] >= 0 || i === A.length) break;
  }

  const squared = new Array(A.length);
  let y = x - 1;
  for (let i = 0; i < squared.length; i++) {
    // If x < A.length + j >= 0
    if (x < A.length && y >= 0) {
      // compare, increment or decrement accordingly
      if (A[x] < Math.abs(A[y])) {
        squared[i] = A[x] ** 2;
        x++;
      } else {
        squared[i] = A[y] ** 2;
        y--;
      }
    } else if (x === A.length) {
      squared[i] = A[y] ** 2;
      y--;
    } else if (y === -1) {
      squared[i] = A[x] ** 2;
      x++;
    }
  }
  return squared;
};
