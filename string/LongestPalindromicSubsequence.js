/**
 * @param {string} s
 * @return {number}
 */
const longestPalindromeSubseq = s => {
  if (!s) return '';

  const n = s.length;
  // Filling with zero so the algorithm is neat-er
  const lookup = new Array(n).fill(0);
  for (let i = 0; i < n; i++) lookup[i] = new Array(n).fill(0);

  let longestPalindrome = '';
  for (let length = 0; length < n; length++) {
    for (let i = 0; i + length < n; i++) {
      const j = i + length;
      if (i === j) lookup[i][j] = 1;
      else if (s[i] === s[j]) lookup[i][j] = lookup[i + 1][j - 1] + 2;
      else lookup[i][j] = Math.max(lookup[i + 1][j], lookup[i][j - 1])
    }
  }
  return lookup[0][n - 1];
};
